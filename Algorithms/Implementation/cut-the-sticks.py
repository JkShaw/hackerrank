#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

lengthOfCut = 0

while(any(i>0 for i in arr)):
    sticksCut = 0
    minVal = min([k for k in arr if k>0])
    for j in xrange(0,n):
        if arr[j]>0:
            sticksCut += 1
            arr[j] -= minVal
    print sticksCut
