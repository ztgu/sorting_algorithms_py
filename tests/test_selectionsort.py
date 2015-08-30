import unittest

from hypothesis import given
import hypothesis.strategies as st

from selectionsort import selectionsort


class TestHeapSort(unittest.TestCase):

    @given(st.lists(st.integers()))
    def test_correctly_sorted(self, unsorted):
        correctly_sorted = sorted(unsorted)

        # Merge Sort is in place
        selectionsort(unsorted)
        selectionsort_sorted = unsorted

        self.assertEqual(
            correctly_sorted,
            selectionsort_sorted
        )
