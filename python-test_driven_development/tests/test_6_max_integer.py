#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_normal_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -3, -10, -1]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-5, 10, 2, -1]), 10)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_list_of_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_list_with_duplicates(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            max_integer(123)

    def test_list_with_strings(self):
        with self.assertRaises(TypeError):
            max_integer(["a", 1, 2])

