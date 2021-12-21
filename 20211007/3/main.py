def Bisect(val, seq):
    if len(seq) >= 1:
        mid = (len(seq) - 1)//2
        if seq[mid] == val:
            return True
        elif seq[mid] < val:
            return Bisect(val,seq[mid+1:])
        else:
            return Bisect(val,seq[:mid])
    else:
        return False

a,b = eval(input())
print(Bisect(a,b))

