# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in xrange(input()):
    try:
        re.compile(raw_input())
        print True
    except re.error:
        print False
