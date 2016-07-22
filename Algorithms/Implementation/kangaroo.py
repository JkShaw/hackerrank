#!/bin/python

import sys


x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

if v1>v2:
    if x1>x2:
        print('NO')
    else:
        if (x2-x1)%(v1-v2) == 0:
            print 'YES'
        else:
            print 'NO'
elif v2>v1:
    if x2>x1:
        print 'NO'
    else:
        if (x1-x2)%(v2-v1) == 0:
            print 'YES'
        else:
            print 'NO'
else:
    if x1==x2:
        print 'YES'
    else:
        print 'NO'
