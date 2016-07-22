n = input()
s = set(map(int, raw_input().split())) 
N = input()
for i in xrange(N):
    inp = raw_input().split()
    if len(inp) > 1:
        if inp[0]=='remove':
            s.remove(int(inp[1]))
        elif inp[0]=='discard':
            s.discard(int(inp[1]))
    elif inp[0]=='pop':
        s.pop()
print sum(s)
