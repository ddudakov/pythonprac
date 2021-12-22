par = eval(input())

def Pareto(*par):
    ans = []
    for p1 in par:
        s = False
        for p2 in par:
            if p1!=p2 and (p1[0] < p2[0] or p1[1] < p2[1]) and p1[0] <= p2[0] and p1[1] <= p2[1]: s = True

        if not s:
            ans.append(p1)
    return tuple(ans)

print(Pareto(*par))
