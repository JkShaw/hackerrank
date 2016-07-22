# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input(); data = map(int, raw_input().split())
if all([i>0 for i in data]): print any([str(i)==str(i)[::-1] for i in data])
else: print "False"
