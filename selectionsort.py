#!/usr/bin/python2

from __future__ import print_function


def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def selectionsort(array):
    for i in range(0, len(array)):
        Ismallest = i
        for j in range(i+1, len(array)):
            if array[j] < array[Ismallest]:
                Ismallest = j
        swap(array, i, Ismallest)
