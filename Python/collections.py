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

# DefaultDict Tutorial------------------------------------------------------

from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(lambda: -1)

for i in range(1, n + 1):
    letter = input()
    d[letter] = d[letter] + ' ' + str(i) if letter in d else str(i)

for _ in range(m):
    print(d[input()])

# Collections.namedtuple()------------------------------------------------

from collections import namedtuple

N = int(input())

c = list(map(str, input().split()))

student = namedtuple('student', '{} {} {} {}'.format(c[0], c[1], c[2], c[3]))

students = list()
sumMarks = int()

for _ in range(N):
    i = list(map(str, input().split()))
    s = student(i[0], i[1], i[2], i[3])
    students.append(s)

for j in students:
    sumMarks += int(j.MARKS)

print(sumMarks / N)

# Collections.OrderedDict()--------------------------------------------------

from collections import OrderedDict

N = int(input().strip())
items = OrderedDict()

for _ in range(N):
    item, space, price = input().rpartition(' ')
    items[item] = items.get(item, 0) + int(price)

for item, price in items.items():
    print(item, price)
