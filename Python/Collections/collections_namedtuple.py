# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division
import collections

N = int(raw_input())
columns = ','.join(raw_input().split())
Student = collections.namedtuple('Student', columns)

sum = 0
for i in range(N):
    line = raw_input().split()
    student = Student(*line)
    sum += int(student.MARKS)

print sum / N

#from collections import namedtuple
#n, Student = input(), namedtuple('Student', raw_input())
#print "%.2f" %( sum([float(stud.MARKS) for stud in [Student(*raw_input().split()) for _ in xrange(n)]]) / n )
