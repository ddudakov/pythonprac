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
print('#' * (H+2))
H_wtr = round(wtr/H)
if H_wtr*H < wtr:
    H_wtr += 1
H_gas = W - H_wtr
for i in range(H_gas):
    print('#' + '.'*H + '#')
for i in range(H_wtr):
    print('#' + '~'*H + '#')
print('#' * (H+2))

summ = wtr + gas
mx = max(wtr, gas)
    
print(('.'*round(gas/mx*20)).ljust(20), end = ' ')
print((str(gas) + '/' + str(summ)).rjust(len(str(mx)) + len(str(summ)) + 1))
print(('~'*round(wtr/mx*20)).ljust(20), end = ' ')
print((str(wtr) + '/' + str(summ)).rjust(len(str(mx)) + len(str(summ)) + 1))
