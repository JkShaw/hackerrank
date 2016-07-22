# Enter your code here. Read input from STDIN. Print output to STDOUT
a = raw_input()
b = raw_input()
count = 0
while a and b:
    pos = a.find(b)
    if pos >= 0:
        count += 1
        a = a[pos+1:]
    else:
        break
print count
