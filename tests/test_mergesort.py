import unittest

from hypothesis import given
import hypothesis.strategies as st

from mergesort import mergesort


class TestHeapSort(unittest.TestCase):

    @given(st.lists(st.integers()))
    def test_correctly_sorted(self, unsorted):
        correctly_sorted = sorted(unsorted)

        # Merge Sort is in place
        mergesort(unsorted)
        mergesort_sorted = unsorted

        self.assertEqual(
            correctly_sorted,
            mergesort_sorted
        )
