# Polar Coordinates---------------------------------------------------------

import cmath

num = complex(input())

print(cmath.polar(num)[0])
print(cmath.polar(num)[1])

# Mod Divmod----------------------------------------------------------------

a = int(input().strip())
b = int(input().strip())

res = divmod(a, b)

for i in res:
    print(i)
print(res)

# Power - Mod Power------------------------------------------------------

a = int(input().strip())
b = int(input().strip())
m = int(input().strip())

print(pow(a, b))
print(pow(a, b, m))

# Integers Come In All Sizes-----------------------------------------------

a = int(input().strip())
b = int(input().strip())
c = int(input().strip())
d = int(input().strip())

print(pow(a, b) + pow(c, d))

# Triangle Quest-----------------------------------------------------------

for i in range(1, int(input())):
    print((10 ** i // 9) * i)

# Triangle Quest 2----------------------------------------------------------

for i in range(1, int(input()) + 1):
    print(((10 ** i - 1) // 9) ** 2)
