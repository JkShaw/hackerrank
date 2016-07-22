# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
print ''.join(c.lower() if c.isupper() else c.upper() for c in s)

