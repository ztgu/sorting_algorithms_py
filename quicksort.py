#!/usr/bin/python2

from __future__ import print_function


def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def partition(array, start, end):
    """ quicksort partitioning, using end """
    pivot = array[end]
    L = start
    R = end
    while L < R:
        while array[L] < pivot:
            L += 1
        while array[R] > pivot:
            R -= 1
        swap(array, L, R)
        # avoid hanging on the same numbers
        if array[L] == array[R]:
            L += 1
    return R


def _quicksort(array, start, end):
    """ Recursive quicksort function """
    if start < end:
        split = partition(array, start, end)
        _quicksort(array, start, split-1)
        _quicksort(array, split+1, end)


def quicksort(array):
    _quicksort(array, 0, len(array)-1)
