sum = 0
while a := int(input()):
    if sum <= 21 and a > 0:
        sum += a
    else:
        break
print(sum if sum>21 else a)
