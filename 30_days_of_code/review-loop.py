# Enter your code here. Read input from STDIN. Print output to STDOUT
t = input()
for i in range(t):
    data = raw_input().strip()
    even = ""
    odd = ""
    for i in range(len(data)):
        if i%2==0:
            even += str(data[i])
        else:
            odd += str(data[i])
    print even + ' ' + odd
