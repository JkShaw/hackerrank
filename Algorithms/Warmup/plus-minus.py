#!/bin/python

import sys
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
pos = 0
neg = 0
zer = 0
for i in arr:
    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1
    else:
        zer += 1
print pos*1.0/n
print neg*1.0/n
print zer*1.0/n

