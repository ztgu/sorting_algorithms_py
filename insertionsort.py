#!/usr/bin/python2

def insertionsort(array):
    for i in range(0, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j-1], array[j] = array[j] , array[j-1]
            j -= 1

if __name__ == "__main__":
    array = [17, 9, 13, 8, 7, -5, 6, 11, 3, 4, 1, 2]
    insertionsort(array)
    print array

