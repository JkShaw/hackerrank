# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
cart = OrderedDict()

for i in xrange(input()):
    item = raw_input().split()
    if cart.get(' '.join(item[:-1])):
        cart[' '.join(item[:-1])] += int(item[-1])
    else:
        cart[' '.join(item[:-1])] = int(item[-1])

for k, v in cart.items():
    print k, v
