import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return (Complex(self.real + no.real, self.imaginary + no.imaginary))
        
    def __sub__(self, no):
        return (Complex(self.real - no.real, self.imaginary - no.imaginary))
        
    def __mul__(self, no):
        return (Complex(self.real * no.real - self.imaginary * no.imaginary, self.real * no.imaginary + self.imaginary * no.real))

    def __truediv__(self, no):
        product = self * Complex(no.real, -no.imaginary)
        sq = no.real**2 + no.imaginary**2
        return (Complex(product.real/sq, product.imaginary/sq))

    def mod(self):
        return (Complex((self.real**2 + self.imaginary**2)**0.5, 0))

    def __str__(self):
        return f'{self.real:.2f}{self.imaginary:+.2f}i'

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')