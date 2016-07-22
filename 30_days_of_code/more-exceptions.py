#Write your code here
class Calculator:
    def power(self, p, q):
        if p < 0 or q < 0 :
                raise ValueError('n and p should be non-negative')
        try:
            import math
            return int(math.pow(p, q))
        except "nonNegativeError":
            print ""
            
