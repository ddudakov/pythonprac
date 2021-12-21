par = eval(input())

def Pareto(*par):
    ans = []
    for p1 in par:
        s = 0
        for p2 in par:
            if p1!=p2 and p1[0] <= p2[0] and p1[1] <= p2[1] and (p1[0] < p2[0] or p1[1] < p2[0]): s = 1

        if s == 0:
            ans.append(p1)
    return tuple(ans)

print(Pareto(*par))
