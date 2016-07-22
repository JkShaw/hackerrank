import numpy as np
n, m, p = map(int, raw_input().split())

npArr = []
for i in xrange(n):
    npArr.append(map(int, raw_input().split()))

mpArr = []
for i in xrange(m):
    mpArr.append(map(int, raw_input().split()))

print np.concatenate((npArr, mpArr), axis=0)
