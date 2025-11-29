"""
Weather Data Collector

Demonstrates REST API integration, error handling, and data persistence
by fetching weather data from OpenWeatherMap API.

Author: Gert Coetser
Date: November 2025
"""

import requests
import json
import sqlite3
import csv
import time
import logging
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path
import argparse
import os


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class WeatherCollector:
    """Collects and stores weather data from OpenWeatherMap API."""
    
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    
    def __init__(self, api_key: Optional[str] = None, demo_mode: bool = False):
        """
        Initialize the WeatherCollector.
        
        Args:
            api_key: OpenWeatherMap API key
            demo_mode: If True, uses mock data instead of real API
        """
        self.api_key = api_key
        self.demo_mode = demo_mode
        self.db_path = Path("weather_data.db")
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'WeatherCollector/1.0'})
        
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Create database and tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS weather_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    city TEXT NOT NULL,
                    country TEXT,
                    temperature REAL,
                    feels_like REAL,
                    humidity INTEGER,
                    pressure INTEGER,
                    weather_condition TEXT,
                    weather_description TEXT,
                    wind_speed REAL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
        logger.info("✓ Database initialized")
    
    def _generate_mock_data(self, city: str) -> Dict:
        """
        Generate mock weather data for demo purposes.
        
        Args:
            city: City name
            
        Returns:
            Mock weather data dictionary
        """
        import random
        
        mock_data = {
            'name': city,
            'sys': {'country': 'XX'},
            'main': {
                'temp': round(random.uniform(10, 30), 2),
                'feels_like': round(random.uniform(10, 30), 2),
                'humidity': random.randint(40, 90),
                'pressure': random.randint(1000, 1030)
            },
            'weather': [{
                'main': random.choice(['Clear', 'Clouds', 'Rain', 'Snow']),
                'description': random.choice(['clear sky', 'few clouds', 'light rain', 'overcast'])
            }],
            'wind': {
                'speed': round(random.uniform(1, 15), 2)
            }
        }
        return mock_data
    
    def fetch_weather(self, city: str, max_retries: int = 3) -> Optional[Dict]:
        """
        Fetch weather data for a specific city.
        
        Args:
            city: City name
            max_retries: Maximum number of retry attempts
            
        Returns:
            Weather data dictionary or None if failed
        """
        if self.demo_mode:
            logger.info(f"📊 Fetching weather data for {city} (DEMO MODE)")
            time.sleep(0.5)  # Simulate API delay
            return self._generate_mock_data(city)
        
        if not self.api_key:
            logger.error("API key is required. Use --demo flag for demo mode.")
            return None
        
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        
        for attempt in range(max_retries):
            try:
                logger.info(f"📊 Fetching weather data for {city} (attempt {attempt + 1}/{max_retries})")
                response = self.session.get(
                    self.BASE_URL, 
                    params=params, 
                    timeout=10
                )
                response.raise_for_status()
                
                data = response.json()
                logger.info(f"✓ Successfully fetched data for {city}")
                return data
                
            except requests.exceptions.HTTPError as e:
                if response.status_code == 404:
                    logger.error(f"✗ City '{city}' not found")
                    return None
                elif response.status_code == 401:
                    logger.error("✗ Invalid API key")
                    return None
                elif response.status_code == 429:
                    logger.warning("⚠ Rate limit exceeded, waiting...")
                    time.sleep(2 ** attempt)
                else:
                    logger.error(f"✗ HTTP error: {e}")
                    
            except requests.exceptions.RequestException as e:
                logger.error(f"✗ Request failed: {e}")
                
            # Wait before retry (exponential backoff)
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
                logger.info(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
        
        logger.error(f"✗ Failed to fetch data for {city} after {max_retries} attempts")
        return None
    
    def parse_weather_data(self, raw_data: Dict) -> Dict:
        """
        Parse raw API response into structured format.
        
        Args:
            raw_data: Raw API response
            
        Returns:
            Parsed weather data dictionary
        """
        try:
            parsed = {
                'city': raw_data['name'],
                'country': raw_data['sys']['country'],
                'temperature': raw_data['main']['temp'],
                'feels_like': raw_data['main']['feels_like'],
                'humidity': raw_data['main']['humidity'],
                'pressure': raw_data['main']['pressure'],
                'weather_condition': raw_data['weather'][0]['main'],
                'weather_description': raw_data['weather'][0]['description'],
                'wind_speed': raw_data['wind']['speed']
            }
            return parsed
        except KeyError as e:
            logger.error(f"✗ Error parsing weather data: missing key {e}")
            return None
    
    def save_to_database(self, weather_data: Dict) -> bool:
        """
        Save weather data to SQLite database.
        
        Args:
            weather_data: Parsed weather data
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO weather_data 
                    (city, country, temperature, feels_like, humidity, pressure,
                     weather_condition, weather_description, wind_speed)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    weather_data['city'],
                    weather_data['country'],
                    weather_data['temperature'],
                    weather_data['feels_like'],
                    weather_data['humidity'],
                    weather_data['pressure'],
                    weather_data['weather_condition'],
                    weather_data['weather_description'],
                    weather_data['wind_speed']
                ))
                conn.commit()
            logger.info(f"✓ Saved data for {weather_data['city']} to database")
            return True
        except sqlite3.Error as e:
            logger.error(f"✗ Database error: {e}")
            return False
    
    def collect_weather_batch(self, cities: List[str]) -> List[Dict]:
        """
        Collect weather data for multiple cities.
        
        Args:
            cities: List of city names
            
        Returns:
            List of parsed weather data dictionaries
        """
        results = []
        
        for city in cities:
            raw_data = self.fetch_weather(city.strip())
            
            if raw_data:
                parsed_data = self.parse_weather_data(raw_data)
                
                if parsed_data:
                    self.save_to_database(parsed_data)
                    results.append(parsed_data)
                    
                    # Display results
                    self._display_weather(parsed_data)
            
            # Rate limiting: wait between requests
            time.sleep(1)
        
        return results
    
    def _display_weather(self, data: Dict) -> None:
        """
        Display weather data in a formatted way.
        
        Args:
            data: Parsed weather data
        """
        print("\n" + "="*50)
        print(f"🌍 {data['city']}, {data['country']}")
        print("="*50)
        print(f"🌡️  Temperature:    {data['temperature']}°C (feels like {data['feels_like']}°C)")
        print(f"💧 Humidity:       {data['humidity']}%")
        print(f"📊 Pressure:       {data['pressure']} hPa")
        print(f"☁️  Condition:      {data['weather_condition']} - {data['weather_description']}")
        print(f"💨 Wind Speed:     {data['wind_speed']} m/s")
        print("="*50)
    
    def export_data(self, format: str = 'json', limit: int = 100) -> None:
        """
        Export weather data from database to file.
        
        Args:
            format: Export format ('json' or 'csv')
            limit: Maximum number of records to export
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT city, country, temperature, feels_like, humidity, 
                           pressure, weather_condition, weather_description, 
                           wind_speed, timestamp
                    FROM weather_data
                    ORDER BY timestamp DESC
                    LIMIT ?
                """, (limit,))
                
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                
                if format == 'json':
                    data = [dict(zip(columns, row)) for row in rows]
                    output_path = Path("weather_export.json")
                    
                    with open(output_path, 'w') as f:
                        json.dump(data, f, indent=2, default=str)
                    
                    logger.info(f"✓ Exported {len(data)} records to {output_path}")
                
                elif format == 'csv':
                    output_path = Path("weather_export.csv")
                    
                    with open(output_path, 'w', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(columns)
                        writer.writerows(rows)
                    
                    logger.info(f"✓ Exported {len(rows)} records to {output_path}")
                
                else:
                    logger.error(f"✗ Unsupported export format: {format}")
                    
        except sqlite3.Error as e:
            logger.error(f"✗ Database error during export: {e}")


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(description='Weather Data Collector')
    parser.add_argument('--cities', type=str, help='Comma-separated list of cities')
    parser.add_argument('--export', type=str, choices=['json', 'csv'], help='Export data format')
    parser.add_argument('--demo', action='store_true', help='Run in demo mode (no API key needed)')
    
    args = parser.parse_args()
    
    # Get API key from environment or use demo mode
    api_key = os.getenv('WEATHER_API_KEY')
    
    if not api_key and not args.demo:
        logger.warning("⚠ No API key found. Running in DEMO mode.")
        logger.warning("  To use real data: export WEATHER_API_KEY='your_key_here'")
        args.demo = True
    
    # Create collector
    collector = WeatherCollector(api_key=api_key, demo_mode=args.demo)
    
    # Collect weather data
    if args.cities:
        cities = args.cities.split(',')
        print(f"\n🌤️  Weather Data Collector")
        print(f"{'='*50}\n")
        
        results = collector.collect_weather_batch(cities)
        
        print(f"\n✓ Collected data for {len(results)} cities")
    
    # Export data
    if args.export:
        collector.export_data(format=args.export)
    
    # Default demo
    if not args.cities and not args.export:
        print("\n🌤️  Weather Data Collector - Demo Mode")
        print(f"{'='*50}\n")
        default_cities = ['London', 'Paris', 'Tokyo', 'New York', 'Sydney']
        results = collector.collect_weather_batch(default_cities)
        print(f"\n✓ Demo complete! Collected data for {len(results)} cities")
        print("\nTry:")
        print("  python weather_collector.py --cities 'Berlin,Madrid'")
        print("  python weather_collector.py --export json")


if __name__ == "__main__":
    main()
