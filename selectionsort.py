#!/usr/bin/python

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def selectionsort(A):
    for i in range(0, len(A)):
        Ismallest = i
        for j in range(i+1, len(A)):
            if A[j] < A[Ismallest]:
                Ismallest = j
        swap(A, i, Ismallest)



if __name__ == "__main__":
    A = [17, 9, 13, 8, 7, -5, 6, 11, 3, 4, 1, 2]
    selectionsort(A)
    print A
