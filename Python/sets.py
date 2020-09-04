# Introduction to Sets---------------------------------------

def average(array):
    mySet = set(array)
    l = len(mySet)
    sum = 0
    for i in mySet:
        sum += i

    return (sum / l)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# Symmetric Difference----------------------------------------

m = input()
firstLine = input()
n = input()
secondLine = input()

a = set(firstLine.split())
b = set(secondLine.split())

firstSet = a.difference(b)
secondSet = b.difference(a)
newSet = firstSet.union(secondSet)

for i in sorted(newSet, key=int):
    print(i)

# No Idea!----------------------------------------------------

happiness = 0

l = list(map(int, input().split()))

arr = list(map(int, input().split()))

a = set(map(int, input().split()))
b = set(map(int, input().split()))

for i in arr:
    if (i in a):
        happiness += 1
    elif (i in b):
        happiness -= 1

print(happiness)

# Set .add()-------------------------------------------------

n = int(input().strip())

countries = None

for i in range(n):
    if countries == None:
        countries = {input().strip()}
    else:
        countries.add(input().strip())

print(len(countries))

# Set .discard(), .remove() & .pop()----------------------------

n = int(input())
s = set(map(int, input().split()))
N = int(input())
sum = 0

for i in range(N):
    c = input().split()

    if c[0] == 'pop':
        s.pop()
    elif c[0] == 'discard':
        s.discard(int(c[1]))
    elif c[0] == 'remove':
        s.remove(int(c[1]))

for i in s:
    sum += i
print(sum)

# Set .union() Operation-------------------------------------------

n = int(input())
ns = set(map(int, input().split()))

b = int(input())
bs = set(map(int, input().split()))

un = ns | bs

print(len(un))

# Set .intersection() Operation-------------------------------------

n = int(input())
ns = set(map(int, input().split()))

b = int(input())
bs = set(map(int, input().split()))

un = ns & bs

print(len(un))

# Set .difference() Operation---------------------------------------------

n = int(input())
ns = set(map(int, input().split()))

b = int(input())
bs = set(map(int, input().split()))

difs = ns - bs

print(len(difs))

# Set .symmetric_difference() Operation---------------------------------------

n = int(input())
ns = set(map(int, input().split()))

b = int(input())
bs = set(map(int, input().split()))

simDif = ns ^ bs

print(len(simDif))

# Set Mutations--------------------------------------------------------------

n = int(input())
A = set(map(int, input().split()))
N = int(input())
sum = 0

for i in range(N):
    c = input().split()
    s = set(map(int, input().split()))

    if c[0] == 'update':
        A.update(s)
    elif c[0] == 'intersection_update':
        A.intersection_update(s)
    elif c[0] == 'difference_update':
        A.difference_update(s)
    elif c[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(s)

for i in A:
    sum += i
print(sum)

# The Captain's Room----------------------------------------------------------------

# n = int(input())
# l = list(map(int, input().split()))
# s = set(l)
#
# for i in s:
#     if l.count(i) == 1:
#         print(i)

k = int(input())
l = list(map(int, input().split(" ")))
s = set(l)

sumList = sum(l)
sumSet = sum(s)

captainDif = (sumSet * k) - sumList

print(captainDif // (k - 1))

# Check Subset-----------------------------------------------------------------------

t = int(input())

for i in range(t):
    n = int(input())
    a = set(map(int, input().split()))

    n2 = int(input())
    b = set(map(int, input().split()))
    print(a.issubset(b))

# Check Strict Superset-----------------------------------------------------------------
# Not completed
A = set(map(int, input().split()))
n = int(input())
check = False
for i in range(n):
    s = set(map(int, input().split()))
    if A.issuperset(s) and len(A) > len(s):
        check = True
    else:
        check = False
print(check)
