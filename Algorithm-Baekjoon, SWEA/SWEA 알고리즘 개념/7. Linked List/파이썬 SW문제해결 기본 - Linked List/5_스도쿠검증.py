import sys
sys.stdin = open("input", "r")


def checkOverlap(a):
    global check
    for i in a :
        if a.count(i) > 1:
            check += 1




T = int(input())
for t in range(1, T+1):
    data = [[]*9 for _ in range(9)]
    check = 0
    for i in range(9):
        data[i] = list(map(str, input().split()))

    # 가로
    for i in range(9):
        checkOverlap(data[i])

    # 세로
    for i in range(9):
        result = []
        for j in range(9):
            result.append(data[j][i])
        checkOverlap(result)

    # 3 * 3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            result = []
            for k in range(0, 3):
                for z in range(0, 3):
                    result.append(data[i+k][j+z])
            checkOverlap(result)

    if check == 0 : print(f"#{t} 1")
    else : print(f"#{t} 0")