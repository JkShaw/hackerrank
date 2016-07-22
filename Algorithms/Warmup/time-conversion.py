#!/bin/python

import sys


time = raw_input().strip()
list1 = time.split(':')
if list1[2][-2:] == 'PM':
    if list1[0] != '12':
        list1[0] = int(list1[0]) + 12
        list1[0] = str(list1[0])
if list1[2][-2:] == 'AM':
    if list1[0] == '12':
        list1[0] = '00'
list1[2] = list1[2][0:2]
print ":".join(list1)
