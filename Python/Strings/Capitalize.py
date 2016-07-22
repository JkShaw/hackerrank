# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = raw_input()
#print ' '.join([t.capitalize() for t in s.strip().split()])
print ''.join([ x.capitalize() for x in re.split('(\W+)', s) ])
