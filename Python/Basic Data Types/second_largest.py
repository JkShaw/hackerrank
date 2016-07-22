# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
num = map(int, raw_input().strip().split())

largest = max(num)
new = []
for i in num:
    if largest!=i:
        new.append(i)
print max(new)
