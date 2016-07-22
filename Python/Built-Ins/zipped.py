# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int, raw_input().split())
inp = []
for i in xrange(x):
    data = map(float,raw_input().split())
    inp.append(data)

result = zip(*inp)
for i in result:
    print sum(i)*1.0/len(i)
