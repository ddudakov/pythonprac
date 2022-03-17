import textdistance
import multiprocessing as mp

def dist(s1, s2, typ):
	if typ == "L":
		return textdistance.levenshtein(s1, s2)
	elif typ == "D":
		return textdistance.damerau_levenshtein(s1, s2)
	else:
		return -1

str1 = input()
str2 = input()
str3 = input()
assert ' ' not in str1
assert ' ' not in str2
pool = mp.Pool(1)
proc = pool.apply_async(dist, (str1,str2,str3))
res = proc.get()
print(res)
