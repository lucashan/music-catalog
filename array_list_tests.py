import unittest
from array_list import *

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)

    def test_empty_list(self):
        self.assertEqual(empty_list(), List([None], 0, 1), None)

    def test_add_empty_valid(self):
        self.assertEqual(add(List([None], 0, 1), 0, 1), List([1], 1, 1))
    def test_add_empty_invalid(self):
        self.assertRaises(IndexError, add, List([None, None], 0, 2), 1, 4)
    def test_add_error_neg_index(self):
        self.assertRaises(IndexError, add, List([1, 2], 2, 2), -6, 2)
    def test_add_beginning(self):
        self.assertEqual(add(List([1, 2, 3, None], 3, 4), 3, 4), List([1, 2, 3, 4], 4, 4))
    def test_add_middle(self):
        self.assertEqual(add(List([1, 3, 4, None], 3, 4), 1, 2), List([1, 2, 3, 4], 4, 4))

    def test_length_empty(self):
        self.assertEqual(length(List([None], 0, 1)), 0)
    def test_length_small(self):
        self.assertEqual(length(List([1, 2, 3], 3, 3)), 3)
    def test_length_medium(self):
        self.assertEqual(length(List([1, 2, 3, 4, 5, 6, 7], 7, 7)), 7)
    def test_length_large(self):
        self.assertEqual(length(List([1, 3, 5, 7, 9, 11, 13, 15, 17], 9, 9)), 9)

    def test_get_empty(self):
        self.assertRaises(IndexError, get, List([None], 0, 1), 3)
    def test_get_error_neg_index(self):
        self.assertRaises(IndexError, get, List([1, 2, 3, 4], 4, 4), -5)
    def test_get_error_greater_index(self):
        self.assertRaises(IndexError, get, List([1, 2, 3, 4], 4, 4), 5)
    def test_get_first_index(self):
        self.assertEqual(get(List([1, 2, 3, 4, 5], 5, 5), 0), 1)
    def test_get_middle_index(self):
        self.assertEqual(get(List([2, 5, 12, 6, 8, 9, 13], 7, 7), 3), 6)
    def test_get_end_index(self):
        self.assertEqual(get(List([3, 6, 9, 10, 11, 14], 6, 6), 5), 14)

    def test_set_empty(self):
        self.assertRaises(IndexError, set, List([None], 0, 1), 3, 4)
    def test_set_error_neg_index(self):
        self.assertRaises(IndexError, set, List([1, 2, 3, 4], 4, 4), -4, 3)
    def test_set_error_greater_index(self):
        self.assertRaises(IndexError, set, List([1, 2, 3, 4], 4, 4), 4, 2)
    def test_set_first_index(self):
        self.assertEqual(set(List([1, 2, 3, 4, 5, None], 5, 6), 0, 0), List([0, 2, 3, 4, 5, None], 5, 6))
    def test_set_middle_index(self):
        self.assertEqual(set(List([1, 2, 3, 4, 5, None], 5, 6), 2, 0), List([1, 2, 0, 4, 5, None], 5, 6))
    def test_set_end_index(self):
        self.assertEqual(set(List([1, 2, 3, 4, 5], 5, 5), 4, 0), List([1, 2, 3, 4, 0], 5, 5))

    def test_remove_error_empty(self):
        self.assertRaises(IndexError, remove, List([None], 0, 1), 5)
    def test_remove_error_neg_index(self):
        self.assertRaises(IndexError, remove, List([1, 3, 5], 3, 3), -4)
    def test_remove_end_index(self):
        self.assertEqual(remove(List([1, 2, 3, 4, 5], 5, 20), 4), (5, List([1, 2, 3, 4, 5], 4, 20)))

if __name__ == '__main__':
    unittest.main()
