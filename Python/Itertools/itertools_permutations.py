# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s, l = raw_input().strip().split()
for i in sorted(list(permutations(s, int(l)))):
    print ''.join(map(str,i))
