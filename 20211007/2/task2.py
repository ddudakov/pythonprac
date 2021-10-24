def SUB(a,b):
    if type(a) == tuple:
        return tuple([i for i in a if i not in b])
    elif type(a) == list:
        return [i for i in a if i not in b]
    else:
        return a - b

a, b = eval(input())
print(SUB(a,b))
