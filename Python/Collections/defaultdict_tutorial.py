# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

d = defaultdict(list)
n, m = raw_input().split()
for i in xrange(int(n)):
    t = raw_input()
    d[t].append(i+1)
for i in xrange(int(m)):
    t = raw_input()
    if t in d:
        print ' '.join(map(str, d[t]))
    else:
        print -1

