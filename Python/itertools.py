# itertools.product()------------------------------------------------

from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in list(product(a, b)):
    print(i, '', end='')

# itertools.permutations()--------------------------------------------

from itertools import permutations

s = input().split()

per = list()

for i in list(permutations(s[0], int(s[1]))):
    elem = str()
    for j in i:
        elem += j
    per.append(elem)

per.sort()

for k in per:
    print(k)

# itertools.combinations()---------------------------------------------


