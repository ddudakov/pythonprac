from math import *

def Calc(s,t,u):
    def f(x):
        return eval(u, {"x":eval(s),"y":eval(t)})
    return f

s,t,u = eval(input())
x = eval(input())
F = Calc(s,t,u)
print(F(x))
