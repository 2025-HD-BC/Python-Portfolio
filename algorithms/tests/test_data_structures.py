"""
Unit tests for data structures.

Run with: python -m unittest tests.test_data_structures
"""

import unittest
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from data_structures import LinkedList, BinarySearchTree, MinHeap, Graph


class TestLinkedList(unittest.TestCase):
    """Test cases for LinkedList."""
    
    def setUp(self):
        """Create a fresh linked list for each test."""
        self.ll = LinkedList()
    
    def test_append(self):
        """Test appending elements."""
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        self.assertEqual(self.ll.to_list(), [1, 2, 3])
        self.assertEqual(len(self.ll), 3)
    
    def test_prepend(self):
        """Test prepending elements."""
        self.ll.prepend(1)
        self.ll.prepend(2)
        self.assertEqual(self.ll.to_list(), [2, 1])
    
    def test_find(self):
        """Test finding elements."""
        self.ll.append(1)
        self.ll.append(2)
        self.assertTrue(self.ll.find(1))
        self.assertTrue(self.ll.find(2))
        self.assertFalse(self.ll.find(3))
    
    def test_delete(self):
        """Test deleting elements."""
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        
        self.assertTrue(self.ll.delete(2))
        self.assertEqual(self.ll.to_list(), [1, 3])
        
        self.assertFalse(self.ll.delete(5))
        self.assertEqual(len(self.ll), 2)


class TestBinarySearchTree(unittest.TestCase):
    """Test cases for BinarySearchTree."""
    
    def setUp(self):
        """Create a fresh BST for each test."""
        self.bst = BinarySearchTree()
    
    def test_insert_and_search(self):
        """Test inserting and searching."""
        values = [5, 3, 7, 1, 9, 4]
        for val in values:
            self.bst.insert(val)
        
        for val in values:
            self.assertTrue(self.bst.search(val))
        
        self.assertFalse(self.bst.search(10))
    
    def test_inorder_traversal(self):
        """Test inorder traversal returns sorted list."""
        values = [5, 3, 7, 1, 9, 4]
        for val in values:
            self.bst.insert(val)
        
        self.assertEqual(self.bst.inorder_traversal(), [1, 3, 4, 5, 7, 9])
    
    def test_find_min_max(self):
        """Test finding min and max values."""
        values = [5, 3, 7, 1, 9, 4]
        for val in values:
            self.bst.insert(val)
        
        self.assertEqual(self.bst.find_min(), 1)
        self.assertEqual(self.bst.find_max(), 9)
    
    def test_empty_tree(self):
        """Test operations on empty tree."""
        self.assertFalse(self.bst.search(1))
        self.assertIsNone(self.bst.find_min())
        self.assertIsNone(self.bst.find_max())
        self.assertEqual(self.bst.inorder_traversal(), [])


class TestMinHeap(unittest.TestCase):
    """Test cases for MinHeap."""
    
    def setUp(self):
        """Create a fresh heap for each test."""
        self.heap = MinHeap()
    
    def test_insert_and_peek(self):
        """Test inserting and peeking."""
        values = [5, 3, 7, 1, 9, 4]
        for val in values:
            self.heap.insert(val)
        
        self.assertEqual(self.heap.peek(), 1)
    
    def test_extract_min(self):
        """Test extracting minimum values."""
        values = [5, 3, 7, 1, 9, 4]
        for val in values:
            self.heap.insert(val)
        
        sorted_values = []
        while self.heap.size() > 0:
            sorted_values.append(self.heap.extract_min())
        
        self.assertEqual(sorted_values, [1, 3, 4, 5, 7, 9])
    
    def test_empty_heap(self):
        """Test operations on empty heap."""
        self.assertIsNone(self.heap.peek())
        self.assertIsNone(self.heap.extract_min())
        self.assertEqual(self.heap.size(), 0)


class TestGraph(unittest.TestCase):
    """Test cases for Graph."""
    
    def setUp(self):
        """Create a fresh graph for each test."""
        self.graph = Graph()
    
    def test_add_vertex_and_edge(self):
        """Test adding vertices and edges."""
        self.graph.add_vertex('A')
        self.graph.add_edge('A', 'B')
        
        self.assertIn('A', self.graph.graph)
        self.assertIn('B', self.graph.graph)
        self.assertIn('B', self.graph.graph['A'])
    
    def test_bfs(self):
        """Test breadth-first search."""
        edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]
        for v1, v2 in edges:
            self.graph.add_edge(v1, v2)
        
        bfs_result = self.graph.bfs('A')
        self.assertEqual(bfs_result[0], 'A')
        self.assertIn('B', bfs_result)
        self.assertIn('C', bfs_result)
        self.assertIn('D', bfs_result)
    
    def test_dfs(self):
        """Test depth-first search."""
        edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]
        for v1, v2 in edges:
            self.graph.add_edge(v1, v2)
        
        dfs_result = self.graph.dfs('A')
        self.assertEqual(dfs_result[0], 'A')
        self.assertIn('B', dfs_result)
        self.assertIn('C', dfs_result)
        self.assertIn('D', dfs_result)
    
    def test_directed_graph(self):
        """Test directed graph."""
        directed_graph = Graph(directed=True)
        directed_graph.add_edge('A', 'B')
        
        self.assertIn('B', directed_graph.graph['A'])
        self.assertNotIn('A', directed_graph.graph['B'])


if __name__ == '__main__':
    unittest.main()
