# Exceptions----------------------------------------------------

for _ in range(int(input().strip())):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except Exception as e:
        print("Error Code:", e)

# Incorrect Regex-----------------------------------------------

