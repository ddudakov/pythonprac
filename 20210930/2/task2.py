start, finish = eval(input())
print([i for i in range(start, finish) if [j for j in range(2, i) if i%j == 0] == [] ])
