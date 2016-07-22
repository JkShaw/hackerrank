#!/bin/python

import sys

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
swapCount = 0

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

for i in range(0, n):
    numberOfSwaps = 0;
    
    for j in range(0, n-1):
        if (a[j] > a[j + 1]):
            swap(a, j, j+1)
            numberOfSwaps += 1
    swapCount += numberOfSwaps
    if (numberOfSwaps == 0):
        break

print "Array is sorted in " + str(swapCount) + " swaps."
print "First Element: " + str(a[0])
print "Last Element: " + str(a[-1])
