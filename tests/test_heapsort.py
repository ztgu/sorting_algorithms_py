import unittest

from hypothesis import given
import hypothesis.strategies as st

from heapsort import heap_sort


class TestHeapSort(unittest.TestCase):

    @given(st.lists(st.integers()))
    def test_correctly_sorted(self, unsorted):
        correctly_sorted = sorted(unsorted)

        # Heap Sort is in place
        heap_sort(unsorted)
        heap_sort_sorted = unsorted

        self.assertEqual(
            correctly_sorted,
            heap_sort_sorted
        )
