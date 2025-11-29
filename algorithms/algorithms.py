"""
Algorithm Implementations

Classic algorithms with clear documentation and complexity analysis.

Author: Gert Coetser
Date: June 2025
"""

from typing import List, Any, Optional, Tuple
import time
from functools import wraps


def timer(func):
    """Decorator to measure execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {(end - start)*1000:.4f}ms")
        return result
    return wrapper


# ============================================================================
# SORTING ALGORITHMS
# ============================================================================

def quick_sort(arr: List[int]) -> List[int]:
    """
    Quick Sort implementation.
    
    Time Complexity: O(n log n) average, O(n²) worst case
    Space Complexity: O(log n) due to recursion
    
    Args:
        arr: List to sort
        
    Returns:
        Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    # Choose pivot (middle element)
    pivot = arr[len(arr) // 2]
    
    # Partition into three parts
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort and combine
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge Sort implementation.
    
    Time Complexity: O(n log n) all cases
    Space Complexity: O(n)
    
    Args:
        arr: List to sort
        
    Returns:
        Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Conquer (merge)
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """Helper function to merge two sorted lists."""
    result = []
    i = j = 0
    
    # Merge while both lists have elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def heap_sort(arr: List[int]) -> List[int]:
    """
    Heap Sort implementation.
    
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    
    Args:
        arr: List to sort
        
    Returns:
        Sorted list
    """
    arr = arr.copy()  # Don't modify original
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        _heapify(arr, i, 0)
    
    return arr


def _heapify(arr: List[int], n: int, i: int) -> None:
    """Helper function to maintain max heap property."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)


# ============================================================================
# SEARCHING ALGORITHMS
# ============================================================================

def binary_search(arr: List[int], target: int) -> int:
    """
    Binary Search implementation.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Args:
        arr: Sorted list to search
        target: Value to find
        
    Returns:
        Index of target or -1 if not found
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def linear_search(arr: List[Any], target: Any) -> int:
    """
    Linear Search implementation.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        arr: List to search
        target: Value to find
        
    Returns:
        Index of target or -1 if not found
    """
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


# ============================================================================
# DYNAMIC PROGRAMMING
# ============================================================================

def fibonacci(n: int) -> int:
    """
    Calculate nth Fibonacci number using dynamic programming.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        n: Position in Fibonacci sequence
        
    Returns:
        nth Fibonacci number
    """
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr


def longest_common_subsequence(s1: str, s2: str) -> int:
    """
    Find length of longest common subsequence between two strings.
    
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    
    Args:
        s1: First string
        s2: Second string
        
    Returns:
        Length of LCS
    """
    m, n = len(s1), len(s2)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    """
    0/1 Knapsack problem using dynamic programming.
    
    Time Complexity: O(n * capacity)
    Space Complexity: O(n * capacity)
    
    Args:
        weights: List of item weights
        values: List of item values
        capacity: Maximum weight capacity
        
    Returns:
        Maximum value achievable
    """
    n = len(weights)
    
    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Fill table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # Don't include item i
            dp[i][w] = dp[i - 1][w]
            
            # Include item i if it fits
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
    
    return dp[n][capacity]


# ============================================================================
# STRING ALGORITHMS
# ============================================================================

def is_palindrome(s: str) -> bool:
    """
    Check if string is a palindrome (ignoring spaces and case).
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        s: String to check
        
    Returns:
        True if palindrome, False otherwise
    """
    # Normalize: lowercase and remove non-alphanumeric
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    # Check if reads same forwards and backwards
    return cleaned == cleaned[::-1]


def find_pattern(text: str, pattern: str) -> List[int]:
    """
    Find all occurrences of pattern in text (naive string matching).
    
    Time Complexity: O(n * m)
    Space Complexity: O(k) where k is number of matches
    
    Args:
        text: Text to search in
        pattern: Pattern to search for
        
    Returns:
        List of starting indices where pattern is found
    """
    matches = []
    n, m = len(text), len(pattern)
    
    for i in range(n - m + 1):
        # Check if pattern matches at position i
        if text[i:i + m] == pattern:
            matches.append(i)
    
    return matches


def longest_palindromic_substring(s: str) -> str:
    """
    Find the longest palindromic substring.
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    
    Args:
        s: Input string
        
    Returns:
        Longest palindromic substring
    """
    if not s:
        return ""
    
    def expand_around_center(left: int, right: int) -> int:
        """Expand around center to find palindrome length."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    start = end = 0
    
    for i in range(len(s)):
        # Check odd-length palindromes (single center)
        len1 = expand_around_center(i, i)
        # Check even-length palindromes (double center)
        len2 = expand_around_center(i, i + 1)
        
        max_len = max(len1, len2)
        
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    
    return s[start:end + 1]


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def compare_sorting_algorithms(arr: List[int]) -> None:
    """Compare performance of different sorting algorithms."""
    print("\n" + "="*60)
    print("SORTING ALGORITHM COMPARISON")
    print("="*60)
    print(f"Array size: {len(arr)}\n")
    
    # Quick Sort
    arr_copy = arr.copy()
    start = time.perf_counter()
    quick_sort(arr_copy)
    end = time.perf_counter()
    print(f"Quick Sort:  {(end - start)*1000:.4f}ms")
    
    # Merge Sort
    arr_copy = arr.copy()
    start = time.perf_counter()
    merge_sort(arr_copy)
    end = time.perf_counter()
    print(f"Merge Sort:  {(end - start)*1000:.4f}ms")
    
    # Heap Sort
    arr_copy = arr.copy()
    start = time.perf_counter()
    heap_sort(arr_copy)
    end = time.perf_counter()
    print(f"Heap Sort:   {(end - start)*1000:.4f}ms")
    
    # Python's built-in sort (Timsort)
    arr_copy = arr.copy()
    start = time.perf_counter()
    arr_copy.sort()
    end = time.perf_counter()
    print(f"Timsort:     {(end - start)*1000:.4f}ms")
    
    print("="*60 + "\n")


if __name__ == "__main__":
    import random
    
    print("\nAlgorithms Demo\n" + "="*60)
    
    # Sorting demo
    print("\n1. Sorting:")
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"   Original: {arr}")
    print(f"   Quick Sort: {quick_sort(arr)}")
    print(f"   Merge Sort: {merge_sort(arr)}")
    print(f"   Heap Sort: {heap_sort(arr)}")
    
    # Binary Search demo
    print("\n2. Binary Search:")
    sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    print(f"   Array: {sorted_arr}")
    print(f"   Search for {target}: index {binary_search(sorted_arr, target)}")
    
    # Dynamic Programming demo
    print("\n3. Dynamic Programming:")
    print(f"   Fibonacci(10): {fibonacci(10)}")
    print(f"   LCS('ABCDGH', 'AEDFHR'): {longest_common_subsequence('ABCDGH', 'AEDFHR')}")
    
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 8
    print(f"   Knapsack (capacity={capacity}): {knapsack(weights, values, capacity)}")
    
    # String Algorithms demo
    print("\n4. String Algorithms:")
    print(f"   Is 'racecar' palindrome? {is_palindrome('racecar')}")
    print(f"   Is 'hello' palindrome? {is_palindrome('hello')}")
    
    text = "AABAACAADAABAAABAA"
    pattern = "AABA"
    print(f"   Find '{pattern}' in '{text}': {find_pattern(text, pattern)}")
    print(f"   Longest palindrome in 'babad': {longest_palindromic_substring('babad')}")
    
    # Performance comparison
    print("\n5. Performance Comparison:")
    large_arr = random.sample(range(1, 10001), 1000)
    compare_sorting_algorithms(large_arr)
    
    print("="*60 + "\n")
