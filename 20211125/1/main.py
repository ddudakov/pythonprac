import sys

br = sys.stdin.buffer.read()
N = br[0]
a = br[1:]
ans = []
for i in range(N):
    ans.append(a[i*len(a)//N : (i+1)*len(a)//N])
res = br[0:1]
for i in sorted(ans):
    if i != b' ' and i != b'\n':
        res += i
sys.stdout.buffer.write(res)
