# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, raw_input().split())
data = []
for i in xrange(n):
    data.append(map(int, raw_input().split()))
k = input()
for i in sorted(data, key=lambda x:x[k]):
    print ' '.join([str(j) for j in i])
