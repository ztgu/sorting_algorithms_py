#!/usr/bin/python3

def swap(array, i, j):
    array[i],array[j] = array[j],array[i]

def insertionsort(array):
    for i in range(0, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            swap(array, j-1, j)
            j -= 1

if __name__ == "__main__":
    array = [17, 9, 13, 8, 7, -5, 6, 11, 3, 4, 1, 2]
    insertionsort(array)
    print(array)