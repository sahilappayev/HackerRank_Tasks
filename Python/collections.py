# collections.Counter()---------------------------------------------

from collections import Counter

x = int(input().strip())
shoes = list(map(int, input().split()))
n = int(input().strip())
d = Counter(shoes)
sum = int()
for i in range(n):
    c = list(map(int, input().split()))
    if d[c[0]] > 0:
        d[c[0]] -= 1
        sum += c[1]
print(sum)

#