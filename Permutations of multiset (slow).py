import itertools
multiset = input("Enter Multiset")
k = int(input("Enter k"))
subsets = []
subsets1 = []
i = 0
j = 0
subset = []
# generate subsets
subsets0 = list(itertools.permutations(multiset, k))
g = len(subsets0)
# remove identical permutations
while i < g:
    subset = list(subsets0[i])
    subsets1.append(subset)
    i += 1
while j < g:
    x = subsets1[j]
    if x not in subsets:
        subsets.append(x)
    j += 1
KpM = len(subsets)
print(KpM)

