#!/usr/bin/python

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def bubblesort(A):
    n = len(A)-1
    for i in range(0, len(A)):
        for j in range(0, n):
            if A[j] > A[j+1]:
                swap(A, j+1, j)
        n -= 1



if __name__ == "__main__":
    A = [17, 9, 13, 8, 7, -5, 6, 11, 3, 4, 1, 2]
    bubblesort(A)
    print A
