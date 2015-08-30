import unittest

from hypothesis import given
import hypothesis.strategies as st

from insertionsort import insertionsort


class TestHeapSort(unittest.TestCase):

    @given(st.lists(st.integers()))
    def test_correctly_sorted(self, unsorted):
        correctly_sorted = sorted(unsorted)

        # Insertion Sort is in place
        insertionsort(unsorted)
        insertionsort_sorted = unsorted

        self.assertEqual(
            correctly_sorted,
            insertionsort_sorted
        )
