A = set(map(int, raw_input().split()))
N = input()

for i in xrange(N):
    if not A.issuperset(set(map(int, raw_input().split()))):
        print False
        break
else:
    print True
