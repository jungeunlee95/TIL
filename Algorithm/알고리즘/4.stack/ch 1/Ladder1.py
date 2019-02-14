import sys
sys.stdin = open("Ladder1", "r")

for i in range(10):
    t = int(input())
    a = [[0] * 100 for _ in range(100)]

    for i in range(100):
        a[i] = list(map(int, input().split()))

    x = y = 0

    for i in range(100):
        for j in range(100):
            if(a[i][j] == 2):
                x = i
                y = j

    while(x > 0):
        if(y==0):
            if(a[x][y+1] == 1):
                a[x][0] = 0
                y = y+1
            else : x=x-1
            continue
        if(y==99):
            if(a[x][y-1] == 1):
                a[x][99] = 0
                y = y-1
            else : x=x-1
            continue

        if(a[x][y-1] == 1):
            a[x][y]=0
            y = y-1

        if(a[x-1][y] == 1):
            a[x][y] = 0
            x = x-1

        if(a[x][y+1] == 1):
            a[x][y] = 0
            y = y+1

    if(x == 0 ):print(f"#{t} {y}")


# 2
# import sys
# sys.stdin = open("input.txt", "r")
#
# def check(x, y):
#     if x < 0 or x > 99 : return False
#     if y < 0 or y > 99 : return False
#
#     if mat[x][y] : return True
#     else : return False
#
# def solve( ):
#     s = 0
#     while True:
#         if mat[99][s] == 2: break
#         s += 1
#
#     x = 99
#     y = s
#     d = 0       # -1(왼쪽), 0(위), 1(오른쪽)
#
#     while x != 0 :
#         if   ((d == 0 or d == -1) and check(x, y - 1)) : d = -1; y -= 1
#         elif ((d == 0 or d ==  1) and check(x, y + 1)) : d =  1; y +=1
#         else :	d = 0; x -= 1
#
#     return y;
#
#
# for tc in range(1, 11):
#     input()
#     mat = [0] * 100
#     for i in range(100):
#         mat[i] = list(map(int, input().split()))
#
#     print('#%d'%tc, solve( ))
