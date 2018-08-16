import unittest
from linked_list import *

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
        self.assertEqual(empty_list(), None)

    def test_add_error_large_index(self):
        self.assertRaises(IndexError, add, Pair(4, Pair(5, None)), 5, 6)
    def test_add_error_neg_index(self):
        self.assertRaises(IndexError, add, Pair(4, Pair(5, None)), -3, 10)
    def test_add_beginning(self):
        self.assertEqual(add(Pair(2, Pair(3, Pair(4, None))), 0, 1), Pair(1, Pair(2, Pair(3, Pair(4, None)))))
    def test_add_end(self):
        self.assertEqual(add(Pair(3, Pair(4, Pair(5, None))), 3, 6), Pair(3, Pair(4, Pair(5, Pair(6, None)))))
    def test_add_inside_list(self):
        self.assertEqual(add(Pair(1, Pair(2, Pair(4, Pair(5, None)))), 2, 3),
                         Pair(1, Pair(2, Pair(3, Pair(4, Pair(5, None))))))

    def test_length_empty(self):
        self.assertEqual(length(None), 0)
    def test_length_small(self):
        self.assertEqual(length(Pair(1, Pair(2, None))), 2)
    def test_length_medium(self):
        self.assertEqual(length(Pair(1, Pair(2, Pair(3, Pair(4, Pair(5, None)))))), 5)
    def test_length_large(self):
        self.assertEqual(length(Pair(2, Pair(3, Pair(4, Pair(5, Pair(6, Pair(7, Pair(8, Pair(9, None))))))))), 8)

    def test_get_error(self):
        self.assertRaises(IndexError, get, None, 3)
    def test_get_empty(self):
        self.assertRaises(IndexError, get, Pair(4, Pair(3, None)), -6)
    def test_get_first_index(self):
        self.assertEqual(get(Pair(12, Pair(3, Pair(-4, Pair(2, Pair(8, None))))), 0), 12)
    def test_get_middle_index(self):
        self.assertEqual(get(Pair(6, Pair(7, Pair(8, Pair(9, None)))), 2), 8)
    def test_get_last_index(self):
        self.assertEqual(get(Pair(4, Pair(6, Pair(3, Pair(10, Pair(2, Pair(19, None)))))), 5), 19)

    def test_set_error_empty(self):
        self.assertRaises(IndexError, set, None, 3, 4)
    def test_set_error_neg_index(self):
        self.assertRaises(IndexError, set, Pair(4, Pair(6, Pair(7, None))), -4, 8)
    def test_set_first_index(self):
        self.assertEqual(set(Pair(1, Pair(2, Pair(3, Pair(4, Pair(5, None))))), 0, 0),
                         Pair(0, Pair(2, Pair(3, Pair(4, Pair(5, None))))))
    def test_set_middle_index(self):
        self.assertEqual(set(Pair(1, Pair(2, Pair(3, Pair(4, None)))), 2, 5), Pair(1, Pair(2, Pair(5, Pair(4, None)))))
    def test_set_end_index(self):
        self.assertEqual(set(Pair(1, Pair(2, Pair(3, Pair(4, None)))), 3, 6), Pair(1, Pair(2, Pair(3, Pair(6, None)))))

    def test_remove_error_empty(self):
        self.assertRaises(IndexError, remove, None, 5)
    def test_remove_error_neg_index(self):
        self.assertRaises(IndexError, remove, Pair(2, Pair(3, Pair(4, None))), -8)
    def test_remove_first_index(self):
        self.assertEqual(remove(Pair(3, Pair(4, Pair(5, Pair(6, None)))), 0), (3, Pair(4, Pair(5, Pair(6, None)))))
    def test_remove_middle_index(self):
        self.assertEqual(remove(Pair(1, Pair(2, Pair(3, Pair(4, Pair(5, None))))), 2),
                         (3, Pair(1, Pair(2, Pair(4, Pair(5, None))))))
    def test_remove_end_index(self):
        self.assertEqual(remove(Pair(0, Pair(1, Pair(2, Pair(3, Pair(4, None))))), 4),
                         (4, Pair(0, Pair(1, Pair(2, Pair(3, None))))))

if __name__ == '__main__':
    unittest.main()
