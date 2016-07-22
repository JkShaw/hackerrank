#!/bin/python

import sys
import re

n = int(raw_input().strip())
b = bin(n)
m = re.findall(r"([1]+)", b)
if m is None:
    print '0'
else:
    print max(map(len, m))
