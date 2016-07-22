# Enter your code here. Read input from STDIN. Print output to STDOUT
data = {}
s = raw_input()
for i in s:
    if data.get(i):
        data[i] += 1
    else:
        data[i] = 1
i = 1
for elem in sorted(data.items(), key=lambda x: (-x[1], x[0])):
    print elem[0], elem[1]
    if i==3:
        break
    i += 1

