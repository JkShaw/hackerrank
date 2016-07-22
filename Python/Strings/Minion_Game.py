# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input().strip()
countV = countC = 0
l = len(s)
for i in xrange(l):
    if s[i] in 'AEIOU':
        countV += l-i
    else:
        countC += l-i
if countV > countC:
    print 'Kevin', countV
elif countV < countC:
    print 'Stuart', countC
else:
    print 'Draw'
