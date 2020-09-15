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
# not finished yet

from itertools import combinations

s = input().split()
k = int(s[1])
string = list(s[0])
string.sort()

myList = combinations(string, k)

for j in string:
    print(j)

for i in myList:
    result = str()
    for l in i:
        result += l
    print(result)

# itertools.combinations_with_replacement()-----------------------------------------

from itertools import combinations_with_replacement

inputs = input().split()
k = int(inputs[1])
string = list(inputs[0])
string.sort()

myList = combinations_with_replacement(string, k)

for i in myList:
    result = str()
    for j in i:
        result += j
    print(result)

#