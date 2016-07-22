# Enter your code here. Read input from STDIN. Print output to STDOUT
e = input()
edata = set(map(int, raw_input().split()))
f = input()
fdata = set(map(int, raw_input().split()))

print len(edata.union(fdata))
