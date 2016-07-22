#!/bin/python

import sys


n1,n2,n3 = raw_input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = map(int,raw_input().strip().split(' '))
h2 = map(int,raw_input().strip().split(' '))
h3 = map(int,raw_input().strip().split(' '))

h1sum = sum(h1)
h2sum = sum(h2)
h3sum = sum(h3)

while(h1sum!=h2sum or h1sum!=h3sum):
    minheight = min(h1sum, h2sum, h3sum)
    if h1sum>minheight:
        h1sum -= h1.pop(0)
    elif h2sum>minheight:
        h2sum -= h2.pop(0)
    elif h3sum>minheight:
        h3sum -= h3.pop(0)
print h1sum
