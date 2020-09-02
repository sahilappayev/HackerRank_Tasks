# List Comprehensions------------------------------------

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    myList = []

    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if (i + j + k) != n:
                    newList = [i, j, k]
                    myList.append(newList)

    print(myList)

# Find the Runner-Up Score!-------------------------------

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr.sort()
    arr.reverse()
    for i in range(len(arr)):
        if len(arr) > 1:
            if arr[i] != arr[i + 1]:
                print(arr[i + 1])
                break
        else:
            print(arr[i])

# Finding the percentage----------------------------------

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for key, value in student_marks.items():
        if key == query_name:
            sum = 0
            for i in value:
                sum += i
            average = sum / len(value)
            print("{:.2f}".format(average))

# Lists---------------------------------------------------

if __name__ == '__main__':
    N = int(input())

    myList = []

    for i in range(N):
        command = input().split()
        if command[0] == "insert":
            myList.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(myList)
        elif command[0] == "remove":
            myList.remove(int(command[1]))
        elif command[0] == "append":
            myList.append(int(command[1]))
        elif command[0] == "sort":
            myList.sort()
        elif command[0] == "pop":
            myList.pop()
        elif command[0] == "reverse":
            myList.reverse()

# Tuples---------------------------------------------------

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    myTuple = tuple(integer_list)
    myHash = hash(myTuple)
    print(myHash)

# Nested Lists---------------------------------------------

if __name__ == '__main__':
    myDict = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        myDict.setdefault(name, score)

    scoresSet = set(myDict.values())
    scoresList = list(scoresSet)
    scoresList.sort()

    names = []

    for key, value in myDict.items():
        if len(scoresList) > 1:
            if value == scoresList[1]:
                names.append(key)

    names.sort()
    for i in names:
        print(i)
