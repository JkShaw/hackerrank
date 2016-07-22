# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = raw_input()
result = re.split("[,.]", s)
for i in result:
    if i.isdigit():
        print i
