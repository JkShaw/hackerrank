# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

n = int(raw_input())
main = []
for i in range(n):
    name = raw_input()
    grade = float(raw_input())
    main.append([name,grade])

minGrade = sorted(set([g[1] for g in main]))[1]
result = []
for i in main:
    if i[1]==minGrade:
        result.append(i[0])
result = sorted(result)
for i in result:
    print i
