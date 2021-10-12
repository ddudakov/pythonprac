summ = 0
while a := int(input()):
    if summ <= 21 and a > 0:
        summ += a
    else:
        break
print(summ if summ>21 else a)
