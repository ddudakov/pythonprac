n = int(input())
a=b=c='-'
if n%25 == 0 and n%2 == 0:
    a='+'
if n%25 == 0 and n%2 == 1:
    b='+'
if n%8 == 0:
    c='+'
print("A",a,"B",b,"C",c)
