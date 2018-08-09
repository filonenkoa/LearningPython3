import unittest
import random
import sort
import time
import inspect

class TestQuickSort(unittest.TestCase):
    def test_small(self):
        array = [random.randint(-999, 999) for n in range(10)]
        self._general_test(array, inspect.stack()[0][3])

    def test_single(self):
        array = [8]
        self._general_test(array, inspect.stack()[0][3])

    def test_one_mil(self):
        array = [random.randint(-999, 999) for n in range(1000000)]
        self._general_test(array, inspect.stack()[0][3])

    def test_huge_values(self):
        array = [random.randint(-2147483648, 2147483647) for n in range(1000)]
        self._general_test(array, inspect.stack()[0][3])

    def _general_test(self, array: list, method_name):
        start = time.time()
        sort.quick_sort(array, 0, len(array)-1)
        end = time.time()
        self.assertEqual(array, sorted(array))
        print("{} | {} ms.".format(method_name, (end-start)))
      

if __name__ == '__main__':
    unittest.main()