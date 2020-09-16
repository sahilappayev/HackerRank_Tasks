# sWAP cASE-----------------------------------------

def swap_case(s):
    return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# String Split and Join--------------------------------

def split_and_join(line):
    line = line.split(' ')
    return '-'.join(line)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# What's Your Name?--------------------------------------

def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a, b))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# Mutations-----------------------------------------------

def mutate_string(string, position, character):
    myStr = string[: position] + character + string[position + 1:]
    return myStr


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# Find a string----------------------------------------------

def count_substring(string, sub_string):
    lenStr = len(string)
    lenSub = len(sub_string)
    count = 0
    for i in range(lenStr - lenSub + 1):
        if string[i:(lenSub + i)] == sub_string:
            count += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

# String Validators-------------------------------------------

if __name__ == '__main__':
    s = input()


def any_alnum():
    for x in range(0, len(s)):
        if (s[x].isalnum()):
            return True
            break
    return False


def any_alpha():
    for j in range(0, len(s)):
        if (s[j].isalpha()):
            return True
            break
    return False


def any_digit():
    for i in range(0, len(s)):
        if (s[i].isdigit()):
            return True
            break
    return False


def any_lower():
    for k in range(0, len(s)):
        if (s[k].islower()):
            return True
            break
    return False


def any_upper():
    for l in range(0, len(s)):
        if (s[l].isupper()):
            return True
            break
    return False


print(any_alnum())
print(any_alpha())
print(any_digit())
print(any_lower())
print(any_upper())

# Text Alignment------------------------------------------------------

thickness = int(input())  # This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
        thickness * 6))

# Text Wrap--------------------------------------------------------------

import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# String Formatting-------------------------------------------------------

def print_formatted(number):
    l = len(str(bin(number))[2:])
    for i in range(1, number + 1):
        decS = str(i).rjust(l)
        octS = str(oct(i))[2:].rjust(l)
        hexS = str(hex(i))[2:].upper().rjust(l)
        binS = str(bin(i))[2:].rjust(l)

        print("{} {} {} {}".format(decS, octS, hexS, binS))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# Capitalize!-----------------------------------------------------------

def solve(s):
    strings = s.split(' ')

    newString = ''

    for i in strings:
        newString += i.capitalize() + ' '

    return newString.strip()


import os

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# Merge the Tools!---------------------------------------------

def merge_the_tools(string, k):
    strings = list()
    for i in range(int(len(string) / k)):
        start = i * k
        end = (i + 1) * k
        t = string[start:end]
        strings.append(t)

    for j in strings:
        u = str()
        for n in j:
            if n not in u:
                u += n
        print(u)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
