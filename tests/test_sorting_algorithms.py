from copy import copy
import unittest

from hypothesis import given
import hypothesis.strategies as st

from bubblesort import bubblesort
from heapsort import heap_sort
from insertionsort import insertionsort
from mergesort import mergesort
from quicksort import quicksort
from selectionsort import selectionsort


class SortingTestCase(unittest.TestCase):

    def test_bubblesort(self):
        self.sorting_algorithm_test(bubblesort)

    def test_heapsort(self):
        self.sorting_algorithm_test(heap_sort)

    def test_insertionsort(self):
        self.sorting_algorithm_test(insertionsort)

    def test_mergesort(self):
        self.sorting_algorithm_test(mergesort)

    def test_quicksort(self):
        self.sorting_algorithm_test(quicksort)

    def test_selectionsort(self):
        self.sorting_algorithm_test(selectionsort)

    @given(test_data=st.lists(st.integers()))
    def sorting_algorithm_test(self, algorithm, test_data):
        unsorted = copy(test_data)

        algorithm(test_data)
        sorted_with_algorithm = test_data

        self.equal_to_python_sort(unsorted, sorted_with_algorithm)
        self.lists_equal_length(unsorted, sorted_with_algorithm)
        self.lists_contain_every_element(unsorted, sorted_with_algorithm)

    def equal_to_python_sort(self, unsorted, sorted_with_algorithm):
        self.assertEqual(
            sorted(unsorted),
            sorted_with_algorithm
        )

    def lists_equal_length(self, unsorted, sorted_with_algorithm):
        self.assertEqual(
            len(unsorted),
            len(sorted_with_algorithm)
        )

    def lists_contain_every_element(self, unsorted, sorted_with_algorithm):
        for i in unsorted:
            self.assertIn(i, sorted_with_algorithm)
        for i in sorted_with_algorithm:
            self.assertIn(i, unsorted)
