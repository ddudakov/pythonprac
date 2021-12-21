import random
l = [random.randint(1, 100) for i in range(9)]
l.insert(random.randint(0, len(l)), int(input()))
print(l)
