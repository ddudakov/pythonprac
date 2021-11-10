import string
import operator
from collections import Counter

W = int(input())
text = ''
while line := input():
    text += line

txt = ""
for x in text.split(" "):
    if x.isalpha():
            txt += x + " "
    else:
        for p in string.punctuation:
            if p in x:
                x = x.replace(p, " ")
        txt += x + " "

words = txt.lower().split(" ")

while "" in words:
    words.remove("")

res = ""
for word in words:
    if len(word) == W:
        res += word + " "

cnt = Counter(res.split(" "))

sorted_tuples = sorted(cnt.items(), key=operator.itemgetter(1))[::-1]
mx = sorted_tuples[0][1]

j = 0
ans = ''
while sorted_tuples[j][1] == mx:
    ans += sorted_tuples[j][0] + " "
    j += 1
ans = sorted(ans.split(" "))

ans.remove("")

print(' '.join(ans))
