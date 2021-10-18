m1 = []
m2 = []
m3 = []
strng = list(eval(input()))
n = len(strng)
i = 0
while i < n:
    m1.append(strng)
    m3.append([0]*n)
    i += 1
    if i < n: strng = list(eval(input()))
    
i = 0
strng = list(eval(input()))
while i < n:
    m2.append(strng)
    i += 1
    if i < n: strng = list(eval(input()))
    
for i in range(n):
    for j in range(n):
        for k in range(n):
            m3[i][j] += m1[i][k] * m2[k][j]

for ans in m3:
    print(ans)          
 
    


