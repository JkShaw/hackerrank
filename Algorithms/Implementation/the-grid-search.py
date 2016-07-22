#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in xrange(R):
       G_t = str(raw_input().strip())
       G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
       P_t = str(raw_input().strip())
       P.append(P_t)
    
    import re
    
    i = 0
    found = False
    while not found and i<R:
        results = [k for k in xrange(C) if G[i][k:].startswith(P[0])]
        #results = [m.start() for m in re.finditer('(?=temp)', G[i])]
        #print results
        for t in results:
            result = t
            if result!=-1:
                #look for rest of the pattern
                j = 1
                k = i + 1
                flag = True
                while j<r and k<R and result!=-1:
                    if G[k][result: result+c] !=P[j]:
                        flag = False
                        break
                    j += 1
                    k += 1
                if j==r and flag:
                    found = True
            if found:
                break
        i += 1
    
    if found:
        print 'YES'
    else:
        print 'NO'
