# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
numShoes = input()
shoes = map(int, raw_input().split())
numCust = input()
total = 0
item = Counter(shoes)
for i in xrange(numCust):
    size, price = raw_input().split()
    if item.get(int(size)) and item[int(size)] > 0:
        item[int(size)] -= 1
        total += int(price)
print total
