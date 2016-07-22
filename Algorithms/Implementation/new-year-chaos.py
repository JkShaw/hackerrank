#!/bin/python

import sys

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    queue = map(int,raw_input().strip().split(' '))
    # your code goes here
    
    
    lastIndex = len(queue) - 1
    swaps = 0
    swaped = False
    chaos = False
    
    # check if the queue is too chaotic
    for i, v in enumerate(queue):
        if (v - 1) - i > 2:
            chaos = True

    if chaos:
        print "Too chaotic"

    else:
        # bubble sorting to find the answer
        for i in xrange(0, lastIndex):
            for j in xrange(0, lastIndex-i):
                #comps += 1
                if queue[j] > queue[j+1]:
                    queue[j], queue[j+1] = queue[j+1], queue[j]
                    swaps += 1
                    swaped = True

            if swaped:
                swaped = False
            else:
                break
        print swaps
