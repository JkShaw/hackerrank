# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
inp = []
for i in xrange(n):
    data = raw_input().split()
    inp.append(data)

from operator import itemgetter
inp.sort(key=itemgetter(2))
for i in inp:
    if i[3] == 'M':
        print "Mr. " + i[0] + ' ' + i[1]
    else:
        print "Ms. " + i[0] + ' ' + i[1]
