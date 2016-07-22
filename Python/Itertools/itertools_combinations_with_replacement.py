# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s, i = raw_input().split()
for j in list(combinations_with_replacement(sorted(s),int(i))):
    print ''.join(map(str,j))
