import sys

br = sys.stdin.buffer.read()
N = br[0]
first = br[0:1]
br = br[1:]

step = len(br)/N
if type(step) == float:
    step = int(step) + 1

ans = [first] + sorted([br[i:i+step] for i in range(0, step*N, step)])

for i in ans:
    if i != b' ' and i != b'\n':
        sys.stdout.buffer.write(i)
