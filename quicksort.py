#!/usr/bin/python2

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
    return R

def _quicksort(array, start, end):
    """ Recursive quicksort function """
    if start < end:
        split = partition(array, start, end)
        _quicksort(array, start, split-1)
        _quicksort(array, split+1, end)

if __name__ == "__main__":
    array = [17, 9, 13, 8, 7, -5, 6, 11, 3, 4, 1, 2]
    _quicksort(array, 0, len(array)-1)
    print array

