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

