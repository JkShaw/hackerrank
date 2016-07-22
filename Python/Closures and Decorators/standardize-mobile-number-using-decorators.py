# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
phones = []
for i in xrange(n):
    phones.append(raw_input())

def decorateMobileNumbers(func):
    def inner(*args):
        args = ['+91 ' + str(item[-10:-5]) + ' ' + str(item[-5:]) for item in args[0]]
        return func(args)
    return inner

@decorateMobileNumbers
def sortNumbers(phones):
    for i in sorted(phones):
        print i

sortNumbers(phones)

