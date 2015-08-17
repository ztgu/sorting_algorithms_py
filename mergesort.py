#!/usr/bin/python

def _mergesort(A, start, end):
    """ Recursive mergesort function """

    # (1) Split
    mid = (start + end)/2
    if start < end:
        _mergesort(A, start, mid)
        _mergesort(A, mid+1, end)
    elif start == end: return

    # (2) Merging
    L = start; R = mid+1
    tmp_A = []
    while ( L <= mid and R <= end):
        if (A[L] < A[R]):
            tmp_A.append(A[L])
            L += 1
        else:
            tmp_A.append(A[R])
            R += 1

    # (3) Append remaining list
    if L <= mid:
        tmp_A += A[L:]
    else:
        tmp_A += A[R:]

    # (4) tmp_A to A
    i = 0;
    while (start <= end):
        A[start] = tmp_A[i]
        start += 1; i += 1;


def mergesort(A):
    _mergesort(A, 0, len(A)-1)


if __name__ == "__main__":

    A = [17, 9, 13, 8, 7, -5, 6, 11, 3, 4, 1, 2]

    mergesort(A)

    print A

