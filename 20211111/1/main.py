class OrderedComplex(complex):
    def __lt__(self,other):
        return True if self.real < other.real and self.imag < other.imag else False
class OrderedComplexMul(OrderedComplex):
    def __matmul__(self,other):
        return self.real * other.real + self.imag * other.imag

import sys
exec(sys.stdin.read())
