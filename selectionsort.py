#!/usr/bin/python3

def swap(array, i, j):
    array[i],array[j] = array[j],array[i]

def selectionsort(array):
    for i in range(0, len(array)):
        Ismallest = i
        for j in range(i+1, len(array)):
            if array[j] < array[Ismallest]:
                Ismallest = j
        swap(array, i, Ismallest)

if __name__ == "__main__":
    array = [17, 9, 13, 8, 7, -5, 6, 11, 3, 4, 1, 2]
    selectionsort(array)
    print(array)