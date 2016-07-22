#!/bin/python

import sys


n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))

equalElem = [abs(i-j) for i in xrange(n) for j in xrange(n) if i!=j and A[i]==A[j]]

if len(equalElem):
    print min(equalElem)
else:
    print -1
