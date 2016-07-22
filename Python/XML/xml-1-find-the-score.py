# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
s = ''
for i in xrange(n):
    s += raw_input()

import xml.etree.ElementTree as etree
tree = etree.ElementTree(etree.fromstring(s))

count = 0

for element in tree.iter():
    count += len(element.attrib)
print count
