W = int(input())
text = ''
while line := input().lower().strip():
    if line == '': break
    for char in line:
        if not (char.isalpha() or char.isspace()):
            line = line.replace(char, ' ')
    text += line + ' '
text = text.split()
dct = {}
mx = 0
for word in text:
    if len(word) == W:
        dct.setdefault(word, 0)
        dct[word] += 1
        if dct[word] > mx:
            mx = dct[word]
for k in sorted(dct.keys()):
    if dct[k] == mx:
        print(k, end = ' ')
