# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s, i = raw_input().split()
result = []
s = sorted(s)
for j in range(1,int(i)+1):
    result.extend(list(combinations(s,j)))
for i in result:
    print ''.join(map(str,i))
