# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
n = input()
arr = raw_input().strip().split()
k = input()
num=0
den=0
for e in permutations(arr,k):
	den+=1
	num+='a' in e[:k]
print(num*1.0/den)
