"""
Unit tests for algorithms.

Run with: python -m unittest tests.test_algorithms
"""

import unittest
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from algorithms import (
    quick_sort, merge_sort, heap_sort,
    binary_search, linear_search,
    fibonacci, longest_common_subsequence, knapsack,
    is_palindrome, find_pattern, longest_palindromic_substring
)


class TestSortingAlgorithms(unittest.TestCase):
    """Test cases for sorting algorithms."""
    
    def setUp(self):
        """Create test data."""
        self.unsorted = [64, 34, 25, 12, 22, 11, 90]
        self.sorted_arr = [11, 12, 22, 25, 34, 64, 90]
    
    def test_quick_sort(self):
        """Test quick sort."""
        result = quick_sort(self.unsorted)
        self.assertEqual(result, self.sorted_arr)
    
    def test_merge_sort(self):
        """Test merge sort."""
        result = merge_sort(self.unsorted)
        self.assertEqual(result, self.sorted_arr)
    
    def test_heap_sort(self):
        """Test heap sort."""
        result = heap_sort(self.unsorted)
        self.assertEqual(result, self.sorted_arr)
    
    def test_empty_array(self):
        """Test sorting empty array."""
        self.assertEqual(quick_sort([]), [])
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(heap_sort([]), [])
    
    def test_single_element(self):
        """Test sorting single element."""
        self.assertEqual(quick_sort([5]), [5])
        self.assertEqual(merge_sort([5]), [5])
        self.assertEqual(heap_sort([5]), [5])


class TestSearchingAlgorithms(unittest.TestCase):
    """Test cases for searching algorithms."""
    
    def setUp(self):
        """Create test data."""
        self.sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15]
        self.unsorted = [5, 2, 8, 1, 9]
    
    def test_binary_search_found(self):
        """Test binary search when element exists."""
        self.assertEqual(binary_search(self.sorted_arr, 7), 3)
        self.assertEqual(binary_search(self.sorted_arr, 1), 0)
        self.assertEqual(binary_search(self.sorted_arr, 15), 7)
    
    def test_binary_search_not_found(self):
        """Test binary search when element doesn't exist."""
        self.assertEqual(binary_search(self.sorted_arr, 10), -1)
        self.assertEqual(binary_search(self.sorted_arr, 0), -1)
    
    def test_linear_search_found(self):
        """Test linear search when element exists."""
        self.assertEqual(linear_search(self.unsorted, 8), 2)
        self.assertEqual(linear_search(self.unsorted, 5), 0)
    
    def test_linear_search_not_found(self):
        """Test linear search when element doesn't exist."""
        self.assertEqual(linear_search(self.unsorted, 10), -1)


class TestDynamicProgramming(unittest.TestCase):
    """Test cases for dynamic programming algorithms."""
    
    def test_fibonacci(self):
        """Test Fibonacci sequence."""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)
    
    def test_lcs(self):
        """Test longest common subsequence."""
        self.assertEqual(longest_common_subsequence("ABCDGH", "AEDFHR"), 3)
        self.assertEqual(longest_common_subsequence("AGGTAB", "GXTXAYB"), 4)
        self.assertEqual(longest_common_subsequence("", "ABC"), 0)
        self.assertEqual(longest_common_subsequence("ABC", ""), 0)
    
    def test_knapsack(self):
        """Test 0/1 knapsack problem."""
        weights = [2, 3, 4, 5]
        values = [3, 4, 5, 6]
        capacity = 8
        self.assertEqual(knapsack(weights, values, capacity), 10)
        
        weights = [1, 2, 3]
        values = [60, 100, 120]
        capacity = 5
        self.assertEqual(knapsack(weights, values, capacity), 220)


class TestStringAlgorithms(unittest.TestCase):
    """Test cases for string algorithms."""
    
    def test_is_palindrome(self):
        """Test palindrome detection."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome(""))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
    
    def test_find_pattern(self):
        """Test pattern matching."""
        text = "AABAACAADAABAAABAA"
        pattern = "AABA"
        result = find_pattern(text, pattern)
        self.assertEqual(result, [0, 9, 13])
        
        self.assertEqual(find_pattern("hello", "ll"), [2])
        self.assertEqual(find_pattern("hello", "xyz"), [])
    
    def test_longest_palindromic_substring(self):
        """Test finding longest palindromic substring."""
        self.assertIn(longest_palindromic_substring("babad"), ["bab", "aba"])
        self.assertEqual(longest_palindromic_substring("cbbd"), "bb")
        self.assertEqual(longest_palindromic_substring("a"), "a")
        self.assertEqual(longest_palindromic_substring(""), "")


if __name__ == '__main__':
    unittest.main()
