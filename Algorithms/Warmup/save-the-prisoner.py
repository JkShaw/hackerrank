# Enter your code here. Read input from STDIN. Print output to STDOUT
t = input()
for i in xrange(t):
    numPrisoner, numSweet, start = map(int, raw_input().strip().split())
    pos = (start + numSweet -1) % numPrisoner
    if pos==0:
        print numPrisoner
    else:
        print pos
