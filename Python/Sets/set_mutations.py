# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
s = set(map(int, raw_input().split()))
n = input()
for i in xrange(n):
    a, b = raw_input().strip().split()
    t = set(map(int, raw_input().split()))
    if a == 'intersection_update':
        s.intersection_update(t)
    elif a == 'update':
        s.update(t)
    elif a == 'symmetric_difference_update':
        s.symmetric_difference_update(t)
    elif a == 'difference_update':
        s.difference_update(t)
    else:
        pass
print sum(s)
