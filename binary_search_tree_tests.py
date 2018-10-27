import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    def test_simple2(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.find_min(), None)
        self.assertEqual(bst.find_max(), None)
        self.assertFalse(bst.search(12))
        self.assertEqual(bst.tree_height(), None)
        bst.insert(12, 'thing')
        self.assertFalse(bst.search(10))
        bst.insert(-5, 'other')
        bst.insert(18, 'whatever')
        bst.insert(10, 'hm')
        self.assertEqual(bst.find_min(), (-5, 'other'))
        self.assertEqual(bst.tree_height(), 2)
        bst.insert(20, 'hello')
        bst.insert(-33, 'welcome')
        self.assertFalse(bst.search(25))
        self.assertTrue(bst.search(-33))
        self.assertEqual(bst.find_max(), (20, 'hello'))
        self.assertEqual(bst.inorder_list(), [-33, -5, 10, 12, 18, 20])
        self.assertEqual(bst.preorder_list(), [12, -5, -33, 10, 18, 20])
        self.assertEqual(bst.level_order_list(), [12, -5, 18, -33, 10, 20])
        bst.insert(-50,'ssss')
        bst.insert(100,'aaaa')
        self.assertEqual(bst.inorder_list(), [-50,-33, -5, 10, 12, 18, 20, 100])
        self.assertEqual(bst.preorder_list(), [12, -5, -33, -50, 10, 18, 20, 100])
        self.assertEqual(bst.level_order_list(), [12, -5, 18, -33, 10, 20, -50, 100])

if __name__ == '__main__': 
    unittest.main()
