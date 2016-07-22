# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
stamps = set()
for i in xrange(n):
    stamps.add(raw_input())
print len(stamps)
