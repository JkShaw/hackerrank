# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

k, m = raw_input().split()
sums = 0
arr = []
for i in xrange(int(k)):
    l = map(int, raw_input().split())
    n = l[0]
    arr.append(l[1:])

sumMax = 0
arrMax = None

for item in product(*arr):
    s = sum([x**2 for x in item]) % int(m)
    
    if s > sumMax:
        sumMax = s
        arrMax = item
print sumMax%int(m)
