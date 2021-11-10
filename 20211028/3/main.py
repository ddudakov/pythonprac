from itertools import *

print(", ".join(sorted([ ans for ans in ["".join(item) for item in product(["T","O","R"], repeat=int(input())) ] if ans.count("TOR") == 2 ])))

