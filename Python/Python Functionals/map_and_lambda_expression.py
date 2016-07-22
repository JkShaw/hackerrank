# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()

first, second = 0, 1

i = 0
l = []
while i < n and i < 2:
    l.append(i)
    i += 1

while i < n:
    first, second = second, first+second
    l.append(second)
    i += 1
cube = lambda x: x*x*x
print list(map(cube, l))

