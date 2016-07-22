# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
phoneDict = {}
for i in xrange(n):
    data = raw_input().strip().split()
    phoneDict[data[0]] = data[1]
for i in xrange(n):
    q = raw_input().strip()
    if q in phoneDict:
        print q + '=' + phoneDict[q]
    else:
        print 'Not found'
