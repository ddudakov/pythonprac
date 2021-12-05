import math

strng = 0
func = {}
while True:
    line = input().split()
    strng += 1
    if line[0][0] == ":":
        name = line[0][1:]
        *var, out = line[1:]
        func[name] = (out, var)
    elif line[0] == "quit":
        print(eval(line[1]).format(len(func)+1, strng))
        break
    else:
        val = [eval(line[i]) for i in range(1,len(line))]
        out, var = func[name]
        if len(var) != 0:
            loc = dict(zip(var, val))
        print(eval(out, math.__dict__, loc))
