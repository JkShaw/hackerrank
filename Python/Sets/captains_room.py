# Enter your code here. Read input from STDIN. Print output to STDOUT
k = input()
room = map(int,raw_input().split())
s = set(room)
print (sum(s)*k -sum(room)) / (k-1)

