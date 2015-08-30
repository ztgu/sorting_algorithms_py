import unittest

from hypothesis import given
import hypothesis.strategies as st

from bubblesort import bubblesort


class TestBubbleSort(unittest.TestCase):

    @given(st.lists(st.integers()))
    def test_correctly_sorted(self, unsorted):
        correctly_sorted = sorted(unsorted)

        # Bubblesort is in place
        bubblesort(unsorted)
        bubblesort_sorted = unsorted

        self.assertEqual(
            correctly_sorted,
            bubblesort_sorted
        )
