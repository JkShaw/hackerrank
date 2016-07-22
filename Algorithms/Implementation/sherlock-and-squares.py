# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/py
from math import *
 
if __name__ == '__main__':
    t = input()
    for _ in range(t):
        a, b = map(int, raw_input().split())
        a = ceil(sqrt(a))
        b = floor(sqrt(b))
        print int(b - a) + 1
        


