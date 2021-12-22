start, finish = eval(input())
print([i for i in range(start, finish) if i > 1 and all([i%j != 0 for j in range(2,i)]) ])
