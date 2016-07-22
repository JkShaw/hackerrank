import numpy as np
n, m = map(int, raw_input().split())
arr = []
for i in xrange(n):
    row = map(int, raw_input().split())
    arr.append(row)
npArr = np.array(arr)
print np.transpose(npArr)
print npArr.flatten()
