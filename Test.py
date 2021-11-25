#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        result = sum(1,2)
        self.assertEqual(result, 55)

if __name__ == '__main__':
    unittest.main()
