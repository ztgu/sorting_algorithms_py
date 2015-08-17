#!/usr/bin/python

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def partition(A, start, end):
    pivot = A[end]
    L = start
    R = end

    while L < R:
        while A[L] < pivot:
            L += 1
        while A[R] > pivot:
            R -= 1

        swap(A, L, R)

    return R

def _quicksort(A, start, end):
    """ Recursive quicksort function """

    if start < end:
        split = partition(A, start, end)
        _quicksort(A, start, split-1)
        _quicksort(A, split+1, end)

def quicksort(A):
    _quicksort(A, 0, len(A)-1)


if __name__ == "__main__":

    A = [17, 9, 13, 8, 7, -5, 6, 11, 3, 4, 1, 2]

    quicksort(A)

    print A

