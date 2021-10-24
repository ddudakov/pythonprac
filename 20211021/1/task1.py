s = input().lower()
print(len({(x,y) for (x,y) in zip(s[:-1],s[1:]) if x.isalpha() and y.isalpha()}))
