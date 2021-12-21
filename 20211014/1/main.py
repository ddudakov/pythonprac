from fractions import Fraction


def poli(s, w, a, b, par):
    A = Fraction("0")
    deg_a = a
    for i in range(a + 1):
        A += (s**deg_a) * Fraction(par[3+i])
        deg_a -= 1

    B = Fraction("0")
    deg_b = b
    for i in range(b + 1):
        B += (s**deg_b) * Fraction(par[3 + a+1 + 1 + i])
        deg_b -= 1
        if B == 0: 
            return False
    return A/B == w 

par = input().split(", ")
s = Fraction(par[0])
w = Fraction(par[1])
a = int(par[2])
b = int(par[3 + a+1])

print(poli(s, w, a, b, par))
