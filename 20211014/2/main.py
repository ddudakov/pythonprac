from math import *

def scale(A, B, a, b, x):
    return (x-A)/(B-A)*(b-a) + a

def T(mat):
    n = []
    for i in range(len(mat[0])):
        n.append(''.join([mat[j][i] for j in range(len(mat))]))
    return n

H, W, A, B, *F = input().split(' ')
H = int(H)
W = int(W)
A = float(A)
B = float(B)
F = ''.join(F)

F = eval('lambda x: ' + F)
X = [scale(0, H, A, B, i) for i in range(H)]
Y = [F(x) for x in X]
my, My = min(Y), max(Y)
ans = []
for y in Y:
    strng = ' ' * int(scale(my, My, 0, W, y)) + '*'
    strng += ' ' * (W - len(strng))
    ans.append(strng)
ans = T(ans)
ans.reverse()
for l in ans:
    print(l)
    
    
