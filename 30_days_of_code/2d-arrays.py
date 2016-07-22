#!/bin/python
import sys

arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)

startIndex = 0
maxSum = -sys.maxint -1

while(startIndex < 4):
    index = 0
    tempSum = 0
    mid = 1
    while index < 4:
        tempSum = sum(arr[startIndex][index:index+3])+sum(arr[startIndex+2][index:index+3])+arr[startIndex+1][mid]
        if tempSum > maxSum:
            maxSum = tempSum
        mid += 1
        index += 1
    startIndex += 1

print maxSum
