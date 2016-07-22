
# Enter your code here. Read input from STDIN. Print output to STDOUT
s=raw_input()
for e in ['isalnum','isalpha','isdigit','islower','isupper']:
    print(any(getattr(c,e)() for c in s))
