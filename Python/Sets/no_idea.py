# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = raw_input().split()
arr = map(int, raw_input().strip().split())
a = set(map(int, raw_input().strip().split()))
b = set(map(int, raw_input().strip().split()))
happiness = 0
for i in arr:
    if len(a.intersection(set([i]))):
        happiness += 1
    elif len(b.intersection(set([i]))):
        happiness -= 1

print happiness
