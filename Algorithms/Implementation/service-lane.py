#!/bin/python

import sys


n,t = raw_input().strip().split(' ')
n,t = [int(n),int(t)]
width = map(int,raw_input().strip().split(' '))
for a0 in xrange(t):
    i,j = raw_input().strip().split(' ')
    i,j = [int(i),int(j)]
    min = width[i]
    for wid in range(i+1,j+1):
        if width[wid] < min:
            min = width[wid]
            if min == 1:
                break
    print min
        
