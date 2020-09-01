# !/bin/python3

# Say "Hello, World!" With Python---------------
print("Hello, World!")

# Python If-Else--------------------------------
if __name__ == '__main__':
    n = int(input().strip())
    if n%2 == 1:
        print("Weird")
    else:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        else:
            print("Not Weird")

# Arithmetic Operators--------------------------
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a+b)
    print(a-b)
    print(a*b)

# Python: Division---------------------------------
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

# Loops--------------------------------------------
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

# Write a function----------------------------------
def is_leap(year):
    leap = False

    if (year >= 400 and (year % 4 == 0) and (year % 400 == 0 or year % 100 != 0)):
        leap = True
    elif (year < 400 and year % 4 == 0 and year % 100 != 0):
        leap = True
    return leap


year = int(input())
print(is_leap(year))

# Print function-------------------------------------
if __name__ == '__main__':
    n = int(input())

for i in range(1,n+1):
    print(i, end="")