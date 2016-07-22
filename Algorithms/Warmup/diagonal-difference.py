#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
   a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
   a.append(a_t)

if n > 0:
    i = 0
    leftSum = 0
    rightSum = 0
    while i < n:
        leftSum += a[i][i]
        rightSum += a[n-1-i][i]
        i += 1
    if leftSum > rightSum:
        print (leftSum - rightSum)
    else:
        print (rightSum - leftSum)
