from math import *

strng = 0
func = {}
while True:
    line = input().split()
    strng += 1
    if line[0].startswith(":"):
        name = line[0][1:]
        *var, out = line[1:]
        func[name] = [tuple(var), out]
    elif line[0] == "quit":
        print(eval(line[1]).format(len(func)+1, strng))
        break
    else:
        f, *val = line
        dct = {}
        for i in range(len(func[f][0])):
            dct[func[f][0][i]] = eval(val[i])
        print(eval(func[f][1], globals(), dct))
