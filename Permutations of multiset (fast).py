import itertools
import math
multiset = input("Enter Multiset")
k = int(input("Enter k"))
s = 0
u = 0
p = 1
multi = []
# generate subsets
subsets0 = list(itertools.combinations(multiset, k))
# sort and set
subsets = list({tuple(sorted(x)) for x in subsets0})
# Count the total number of permutations
for f in subsets:
    for i in f:
        if i not in multi:
            y = f.count(i)
            p = p * math.factorial(y)
            multi.append(i)
    u = math.factorial(k) / p
    s = int(s + u)
    p = 1
    multi = []
print(s)
