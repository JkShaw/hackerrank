# Enter your code here. Read input from STDIN. Print output to STDOUT
n, k = map(int, raw_input().split())
problems = map(int, raw_input().split())

special = 0
chapter = 0
index = 1

for problem in problems:
    for i in range(1, problem+1):
        if i==index:
            special += 1
        if i%k==0:
            index += 1
print special
