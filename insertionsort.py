#!/usr/bin/python

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def insertionsort(A):
    for i in range(0, len(A)):
        j = i
        while j > 0 and A[j-1] > A[j]:
            swap(A, j-1, j)
            j -= 1




if __name__ == "__main__":
    A = [17, 9, 13, 8, 7, -5, 6, 11, 3, 4, 1, 2]
    insertionsort(A)
    print A
