# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a = map(int,raw_input().split())
b = map(int,raw_input().split())
print ' '.join(str(i) for i in list(product(a,b)))
