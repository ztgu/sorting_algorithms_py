#!/usr/bin/env python

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def heapify(A):
    """ Build heap """
    start = (len(A) - 2) / 2  # (1  2  [3]  4  5)
    while start >= 0:
        percDown(A, start, len(A) - 1)
        start -= 1

def percDown(A, start, end):
    """ Checks if structure is heap"""
    largest = 2 * start + 1
    while largest <= end:
        #                       left child < right child
        if (largest < end) and (A[largest] < A[largest + 1]):
            largest += 1
        #  biggest child > parent
        if (A[largest] > A[start]):
            swap(A, largest, start)
            start = largest
            largest = 2 * start + 1
        else: return

def HeapSort(A):
    # biggest to smallest
    heapify(A)
    end = len(A) - 1
    while end > 0:
        # Swap biggest with end node
        swap(A, end, 0)
        # Make sure first node is biggest
        percDown(A, 0, end - 1)
        end -= 1

if __name__ == "__main__":
    A = [2, 7, 1, -2, 56, 5, 3]

    HeapSort(A)

    print(A)

