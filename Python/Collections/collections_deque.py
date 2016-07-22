# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()
n = input()
for i in xrange(n):
    data = raw_input().split()
    if len(data) > 1:
        if data[0] == 'append':
            d.append(data[1])
        elif data[0] == 'appendleft':
            d.appendleft(data[1])
    else:
        if data[0] == 'pop':
            d.pop()
        else:
            d.popleft()
print ' '.join(d)
