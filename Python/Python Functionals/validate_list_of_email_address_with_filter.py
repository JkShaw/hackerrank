# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
a = re.compile('^([a-zA-Z0-9_\-]+)@([a-zA-Z0-9]+)\.([a-zA-Z]{1,3})$')
emails = []
for i in range(input()):
    emails.append(raw_input())

print list(filter(lambda x: a.match(x), sorted(emails)))

