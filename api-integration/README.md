# Weather Data Collector

A Python application demonstrating REST API integration by fetching and analyzing weather data.

## Overview

This project showcases:
- REST API integration with error handling
- JSON data processing
- Data persistence (SQLite database)
- Retry logic and rate limiting
- Command-line interface

## Features

- Fetch current weather data for multiple cities
- Store historical weather data in SQLite database
- Export data to JSON/CSV formats
- Robust error handling and logging
- Rate limiting to respect API quotas

## API Used

This example uses the [OpenWeatherMap API](https://openweathermap.org/api) (free tier).

**Note:** To run this with real data, you'll need to:
1. Sign up for a free API key at OpenWeatherMap
2. Set your API key: `export WEATHER_API_KEY="your_key_here"`

The script includes a demo mode that works without an API key.

## Requirements

See `requirements.txt` for dependencies.

## Usage

### Demo Mode (No API Key Required)
```bash
python weather_collector.py --demo
```

### With Real API
```bash
# Set your API key
export WEATHER_API_KEY="your_api_key_here"

# Fetch weather for cities
python weather_collector.py --cities "London,Paris,Tokyo"

# Export data
python weather_collector.py --export csv
```

## Sample Output

- `weather_data.db` - SQLite database with historical data
- `weather_export.json` - Exported weather data in JSON format
- `weather_export.csv` - Exported weather data in CSV format
