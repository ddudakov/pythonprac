n = int(input())

i=n
while i<n+3:
    j=n
    while j<n+3:
        p = i*j
        ans = p
        psum = 0
        while p > 0:
            psum += (p % 10)
            p //= 10
        if psum == 6:
            ans = ':=)'
        print(i, '*', j, '=', ans, sep='', end = '\n' if j == n+2 else ' ')
        j += 1
    i += 1


