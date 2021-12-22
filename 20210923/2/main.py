a = int(input())
summ = 0
while a > 0:
    summ += a
    if summ > 21:
        print(summ)
        break
    a = int(input())
else: print(a)
