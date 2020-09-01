# !/bin/python3

# Sock Merchant---------------------------------------------------
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0;
    for item in set(ar):
        if (ar.count(item) > 0):
            pairs += (ar.count(item) // 2)

    return pairs

# Counting Valleys------------------------------------------------
# Complete the countingValleys function below.
def countingValleys(n, s):
    count = 0
    level = 0
    for i in s:
        if i == 'U':
            level +=1
        elif i == 'D':
            level -=1
        if (level == 0) and (i == 'U'):
            count += 1
    return count

# Jumping on the Clouds--------------------------------------------
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    if len(c) == 1:
        return 0
    if len(c) == 2:
        if c[1]==1:
            return 0
        else:
            return 1
    if c[2] == 1:
        return 1 + jumpingOnClouds(c[1:])
    if c[2] == 0:
        return 1 + jumpingOnClouds(c[2:])

