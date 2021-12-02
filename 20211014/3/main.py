first = input()
W = len(first) - 2
H = 0
wtr = 0
gas = 0
while True:
    strng = input()
    wtr += strng.count('~')
    gas += strng.count('.')
    if (first == strng): break
    H += 1
W, H = H, W
print('#' * (W+2))
for i in range(H):
    print('#', end='')
    if gas - i * W <= 0:
        print('~' * W, end='')
    else:
        print('.' * W, end='')
    print('#')
print('#' * (W+2))

summ = wtr + gas
indent = max(wtr, gas)
wpar = 1
gpar = 1
if gas < 10 and wtr >= 10:
    gpar += 1
elif wtr < 10 and gas >= 10:
    wpar += 1
    
print('.' * gas + ' ' * (indent - gas + gpar) + str(gas) + '/' + str(summ))
print('~' * wtr + ' ' * (indent - wtr + wpar) + str(wtr) + '/' + str(summ))
