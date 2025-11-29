# Algorithms & Data Structures

Implementation of common algorithms and data structures with comprehensive tests and documentation.

## Overview

This project demonstrates fundamental computer science concepts with clean, well-tested Python code:
- Custom data structure implementations
- Classic algorithm solutions
- Time and space complexity analysis
- Unit tests for all implementations

## Implementations

### Data Structures
1. **LinkedList** - Singly and doubly linked lists
2. **BinarySearchTree** - BST with insert, search, delete operations
3. **MinHeap** - Binary min-heap implementation
4. **Graph** - Graph representation with BFS and DFS

### Algorithms
1. **Sorting** - Quick Sort, Merge Sort, Heap Sort
2. **Searching** - Binary Search, BFS, DFS
3. **Dynamic Programming** - Fibonacci, Longest Common Subsequence, Knapsack
4. **String Algorithms** - Pattern matching, palindrome checks

## Features

- **Clean Code**: Well-documented, PEP 8 compliant
- **Type Hints**: Full type annotation for clarity
- **Unit Tests**: Comprehensive test coverage
- **Complexity Analysis**: Big O notation documented for each method
- **Educational**: Comments explain the reasoning

## Usage

### Run All Tests
```bash
python -m unittest discover tests
```

### Run Specific Tests
```bash
python -m unittest tests.test_data_structures
python -m unittest tests.test_algorithms
```

### Use as Module
```python
from data_structures import BinarySearchTree, LinkedList
from algorithms import quick_sort, binary_search

# Create a BST
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)

# Sort an array
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
```

## Time Complexity Summary

### Data Structures
- LinkedList: Insert O(1), Search O(n), Delete O(n)
- BST: Insert O(log n), Search O(log n), Delete O(log n) average case
- MinHeap: Insert O(log n), Extract Min O(log n), Get Min O(1)

### Algorithms
- Quick Sort: O(n log n) average, O(n²) worst
- Merge Sort: O(n log n) all cases
- Binary Search: O(log n)
