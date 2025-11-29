# Python Portfolio - Professional Code Examples

**Author:** Gert Coetser  
**Email:** gert@semper-fi.co.za  
**GitHub:** [2025-HD-BC](https://github.com/2025-HD-BC)

---

## 📋 Overview

This repository showcases production-quality Python code demonstrating expertise in algorithms, data structures, API integration, automation, and data analysis. Each project includes comprehensive documentation, error handling, and follows industry best practices.

---

## 🚀 Projects

### 1. **Algorithms** 📊
**File:** `algorithms/algorithms.py`

Comprehensive implementation of classic computer science algorithms with complexity analysis.

**Features:**
- **Sorting:** Quick Sort, Merge Sort, Heap Sort
- **Searching:** Binary Search, Linear Search  
- **Dynamic Programming:** Fibonacci, Longest Common Subsequence, Knapsack Problem
- **String Algorithms:** Palindrome Detection, Pattern Matching, Longest Palindromic Substring
- Performance comparison utilities

**Key Skills:** Algorithm design, complexity analysis, optimization

```python
# Example Usage
from algorithms import quick_sort, binary_search, fibonacci

sorted_list = quick_sort([64, 34, 25, 12, 22, 11, 90])
index = binary_search([1, 3, 5, 7, 9], 7)
fib_10 = fibonacci(10)
```

---

### 2. **Data Structures** 🔗
**File:** `algorithms/data_structures.py`

Clean implementations of fundamental data structures with full documentation.

**Implementations:**
- **LinkedList:** Singly linked list with append, prepend, find, delete
- **Binary Search Tree:** Insert, search, traversal operations
- **Min Heap:** Priority queue with insert and extract operations
- **Graph:** BFS and DFS traversal algorithms

**Key Skills:** Data structure design, memory management, algorithmic thinking

```python
# Example Usage
from data_structures import LinkedList, BinarySearchTree, Graph

ll = LinkedList()
ll.append(1)
ll.append(2)

bst = BinarySearchTree()
bst.insert(5)
print(bst.search(5))  # True
```

---

### 3. **Weather API Collector** 🌤️
**File:** `api-integration/weather_collector.py`

Production-grade REST API client with comprehensive error handling and data persistence.

**Features:**
- REST API integration with OpenWeatherMap
- Exponential backoff retry logic
- Rate limiting and error handling
- SQLite database persistence
- Demo mode for testing without API key
- CSV and JSON export capabilities

**Key Skills:** API integration, error handling, data persistence, logging

```bash
# Run with demo data
python weather_collector.py --demo --cities "London,Paris,Tokyo"

# Export collected data
python weather_collector.py --export json
```

**Technologies:** `requests`, `sqlite3`, `logging`, `argparse`

---

### 4. **Smart File Organizer** 📁
**File:** `automation/file_organizer.py`

Intelligent file organization system with duplicate detection and flexible categorization.

**Features:**
- Automatic file categorization by type
- Date-based organization
- MD5 duplicate file detection
- Customizable category rules via JSON
- Dry-run mode for safe preview
- Comprehensive logging

**Key Skills:** File I/O, automation, hash algorithms, JSON configuration

```bash
# Organize files by type
python file_organizer.py --source "C:\Downloads"

# Find duplicate files
python file_organizer.py --source "C:\Documents" --find-duplicates

# Preview changes (dry run)
python file_organizer.py --source "C:\Folder" --dry-run
```

**Technologies:** `pathlib`, `hashlib`, `json`, `shutil`

---

### 5. **Sales Data Analysis** 📈
**File:** `data-analysis/sales_analysis.py`

Complete data analysis pipeline with visualization and statistical insights.

**Features:**
- Automated data cleaning and preprocessing
- Monthly trend analysis
- Top product identification
- Regional performance analysis
- Professional visualizations (charts, graphs)
- Summary statistics and reports

**Key Skills:** Data analysis, pandas, matplotlib, statistical analysis

```python
# Run full analysis
from sales_analysis import SalesAnalyzer

analyzer = SalesAnalyzer()  # Uses sample data
analyzer.run_full_analysis()

# Or load your own data
analyzer = SalesAnalyzer("sales_data.csv")
analyzer.run_full_analysis()
```

**Technologies:** `pandas`, `matplotlib`, `seaborn`, `numpy`

**Outputs:**
- Sales trend charts
- Top products visualization
- Regional analysis graphs
- CSV summary reports

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/2025-HD-BC/Algorithms.git
cd Algorithms
```

2. **Create virtual environment (recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install requests pandas matplotlib seaborn numpy
```

---

## 🧪 Testing

Each module includes `if __name__ == "__main__":` blocks for demonstration:

```bash
# Test algorithms
python algorithms/algorithms.py

# Test data structures
python algorithms/data_structures.py

# Test weather collector (demo mode)
python api-integration/weather_collector.py --demo

# Test file organizer (safe dry-run)
python automation/file_organizer.py --source "." --dry-run

# Test sales analysis
python data-analysis/sales_analysis.py
```

---

## 💼 Skills Demonstrated

### Programming Concepts
- ✅ Object-Oriented Programming (OOP)
- ✅ Algorithm Design & Optimization
- ✅ Data Structures
- ✅ Error Handling & Logging
- ✅ File I/O & Data Persistence
- ✅ API Integration
- ✅ Data Analysis & Visualization

### Python Libraries
- **Core:** `pathlib`, `json`, `logging`, `argparse`, `datetime`
- **Data:** `pandas`, `numpy`
- **Visualization:** `matplotlib`, `seaborn`
- **Web:** `requests`
- **Database:** `sqlite3`
- **Security:** `hashlib`

### Best Practices
- ✅ Type hints for better code clarity
- ✅ Comprehensive docstrings
- ✅ PEP 8 code style
- ✅ Defensive programming
- ✅ Configuration management
- ✅ Logging and debugging
- ✅ DRY (Don't Repeat Yourself) principles

---

## 📊 Complexity Analysis

All algorithms include Big O notation for time and space complexity:

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Quick Sort | O(n log n) avg | O(log n) |
| Merge Sort | O(n log n) | O(n) |
| Binary Search | O(log n) | O(1) |
| Fibonacci (DP) | O(n) | O(1) |
| Graph BFS/DFS | O(V + E) | O(V) |

---

## 📧 Contact

**Gert Coetser**  
- **Email:** gert@semper-fi.co.za
- **GitHub:** [@2025-HD-BC](https://github.com/2025-HD-BC)

---

## 📄 License

This project is open source and available for review by potential employers. Please contact me for usage permissions.

---

## 🎯 Project Goals

This portfolio demonstrates:
1. **Clean, readable code** with proper documentation
2. **Real-world problem solving** with practical applications
3. **Software engineering best practices** including error handling, logging, and testing
4. **Diverse skill set** across algorithms, data analysis, API integration, and automation
5. **Professional code quality** suitable for production environments

---

*Last Updated: November 2025*
