#!/usr/bin/python2

def _mergesort(array, start, end):
    """ Recursive mergesort function """
    # split
    mid = (start + end)/2
    if start < end:
        _mergesort(array, start, mid)
        _mergesort(array, mid+1, end)
    elif start == end: return

    # merging Left and Right array
    L = start; R = mid+1
    tmp_array = []
    while ( L <= mid and R <= end):
        if (array[L] < array[R]):
            tmp_array.append(array[L])
            L += 1
        else:
            tmp_array.append(array[R])
            R += 1

    # append remaining list, Left array
    if L <= mid:
        tmp_array += array[L:]
    else:
        tmp_array += array[R:]

    # tmp_array to array
    i = 0;
    while (start <= end):
        array[start] = tmp_array[i]
        start += 1; i += 1;

if __name__ == "__main__":
    array = [17, 9, 13, 8, 7, -5, 6, 11, 3, 4, 1, 2]
    _mergesort(array, 0, len(array)-1)
    print array

