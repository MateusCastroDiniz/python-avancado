from math_op import *
from bubble_sort_tests.bubble_sort import bubble_sort
from searches.binary_search_op import binary_search
import unittest


class TestsUnits(unittest.TestCase):
    def test_addition_op(self):
        math_addition_result = addition_operation(1, 2, 3)
        print(math_addition_result)
        self.assertEqual(math_addition_result, 6)

    def test_subtraction_op(self):
        math_subtraction_result = subtraction_op(3, 1)
        print(math_subtraction_result)
        self.assertEqual(math_subtraction_result, 2)

    def test_binary_search(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        to_find = 2
        binary_search_result = binary_search(array, to_find, 0, (len(array)-1))
        print(binary_search_result)
        self.assertEqual(binary_search_result, None)

    def test_bubble_search(self):
        random_list = [15, 32, 21, 1, 4]
        bubble_sort_result = bubble_sort(random_list)
        print(bubble_sort_result)
        self.assertEqual(bubble_sort_result, [1, 4, 15, 21, 32])



if __name__ == '__main__':
    unittest.main()
