#!/bin/python

import sys


N = int(raw_input().strip())
B = map(int,raw_input().strip().split(' '))
count = 0
possible = True

for i in range(0,N):
    if B[i]%2!=0 and (i+1)<N:
        B[i] += 1
        B[i+1] += 1
        count += 2
    elif B[i]%2!=0 and (i+1)>=N:
        possible = False
        break

if possible:
    print count
else:
    print 'NO'
