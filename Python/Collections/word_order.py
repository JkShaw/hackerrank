# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict, Counter

diction = OrderedDict()
n = input()
for i in xrange(n):
    s = raw_input()
    if diction.get(s):
        diction[s] += 1
    else:
        diction[s] = 1
print len(diction)
print ' '.join([str(val) for val in diction.values()])
