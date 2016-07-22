# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, num):
        real = self.real + num.real
        imaginary = self.imaginary + num.imaginary
        return Complex(real, imaginary)
    
    def __sub__(self, num):
        real = self.real - num.real
        imaginary = self.imaginary - num.imaginary
        return Complex(real, imaginary)
    
    def __mul__(self, num):
        real = self.real * num.real - self.imaginary * num.imaginary
        imaginary = self.real * num.imaginary + self.imaginary * num.real
        return Complex(real, imaginary)

    def __div__(self, num):
        x = float(num.real ** 2 + num.imaginary ** 2)
        y = self * Complex(num.real, -num.imaginary)
        real = y.real / x
        imaginary = y.imaginary / x
        return Complex(real, imaginary)
    
    def mod(self):
        real = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return Complex(real, 0)
    
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+%.2fi" % (self.real, 0.00)
        elif self.real == 0 and self.imaginary >= 0:
            result = "%.2f+%.2fi" % (0.00, self.imaginary)
        elif self.real == 0:
            result = "%.2f%.2fi" % (0.00, self.imaginary)
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
    
C = map(float, raw_input().split())
D = map(float, raw_input().split())
x = Complex(*C)
y = Complex(*D)
final = [x+y, x-y, x*y, x/y, x.mod(), y.mod()]
print '\n'.join(map(str, final))
