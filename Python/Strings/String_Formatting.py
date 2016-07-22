# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
width = len('{:b}'.format(n))
for i in xrange(1, n+1):
    print str.rjust(str(i), width),\
        str.rjust('{:o}'.format(i), width),\
        str.rjust('{:X}'.format(i), width),\
        str.rjust('{:b}'.format(i), width)
