import sys
sys.stdin = open("행렬찾기", "r")

T = int(input())
for i in range(1, T+1):
    size = int(input())
    G = [[] for _ in range(size)]

    for i in range(size):
        G[i] = list(map(int, input().split()))

    result = []
    while True:
        for i in range(size):
            for j in range(size):
                if G[i][j] > 0:
                    a = i
                    while G[i][a] != 0:
                        G[i][a] = 0
                        a += 1
                    b = j+1
                    while G[b][j] != 0:
                        G[b][j] = 0
                        b += 1
                    result.append([b, a])
                    break
                if i == size-1 and j==size-1: break
        print(G)
    print(result)



# 1
TC = int(input().strip())


def bfs(lists, x, y):
    global chemical_cnt
    global front
    global rear

    chemical_cnt += 1

    x_cnt = 0
    y_cnt = 0

    # 아래쪽과 오른쪽 검사
    dx = [1, 0]
    dy = [0, 1]

    copy_x = x
    copy_y = y

    while True:
        if lists[x][y] != 0:
            x += dx[1]
            y += dy[1]
            y_cnt += 1
        else:
            break
        if x >= n or y >= n:
            break

    x = copy_x
    y = copy_y

    while True:
        if lists[x][y] != 0:
            x += dx[0]
            y += dy[0]
            x_cnt += 1
        else:
            break
        if x >= n or y >= n:
            break

    result_lists.append([y_cnt * x_cnt, x_cnt, y_cnt])

    x = copy_x
    y = copy_y

    lists[x][y] = 0
    rear += 1
    queue[rear] = [x, y]
    # BFS안해도 되지만 지우는걸 그냥 BFS로 해봄..
    while True:
        if front == rear:  # 큐 비어있으면 종료
            break
        else:
            for a in range(2):
                if x + dx[a] >= n or y + dy[a] >= n:
                    continue

                if lists[x + dx[a]][y + dy[a]] != 0:
                    lists[x + dx[a]][y + dy[a]] = 0
                    rear += 1
                    queue[rear] = [x + dx[a], y + dy[a]]

                    x += dx[a]
                    y += dy[a]
                    break
            else:
                front += 1
                x = queue[front][0]
                y = queue[front][1]


for tc in range(TC):
    n = int(input().strip())

    chemical_lists = [[0] for a in range(n)]

    for a in range(n):
        chemical_lists[a] = list(map(int, input().split()))

    chemical_cnt = 0

    front = -1
    rear = -1
    queue = [0] * n * n

    start_x = 0
    start_y = 0

    result_lists = []  # 행렬의 크기가 들어간다.
    # 바로 아래칸과 오른쪽만 검사하면된다

    for x in range(n):
        for y in range(n):
            if chemical_lists[x][y] != 0:
                bfs(chemical_lists, x, y)

    print(f"#{tc + 1} {chemical_cnt}", end=" ")
    result_lists.sort()
    for a in result_lists:
        print(f"{a[1]} {a[2]}", end=" ")
    print("")



# 2
# testcase = int(input())
#
# for tc in range(testcase):
#     # input
#     n = int(input())
#     array = [[] for _ in range(n)]
#     for row in range(n):
#         array[row] = list(map(int, input().split()))
#
#     # 사각형들의 행과 열을 저장할 배열
#     ans = []
#
#     # 모든 셀이 0이 될 때까지 진행
#     check = 0
#     while check == 0:
#         # 매번 새롭게 돌면서
#         for i in range(n):
#             for j in range(n):
#                 # 용기를 하나 만나면 오른쪽 끝과 아래 끝을 찾아감
#                 if array[i][j] > 0:
#                     # 상하 방면
#                     iindex = i
#                     while iindex < n + 1 and array[iindex][j]:
#                         iindex += 1
#                     # 좌우 방면
#                     jindex = j
#                     while jindex < n + 1 and array[i][jindex]:
#                         jindex += 1
#
#                     # 찾은 영역을 다 0으로 바꾸기
#                     for i2 in range(i, iindex):
#                         for j2 in range(j, jindex):
#                             array[i2][j2] = 0
#                     # 사각형의 끝 좌표들을 저장함
#                     ans.append([iindex - i, jindex - j])
#
#                 # 더 이상 찾을 수 있는 셀이 없으면 종료
#                 elif i == n - 1 and j == n - 1:
#                     check = 1
#                     break
#         if check == 1:
#             break
#
#     print('#{} {}'.format(tc + 1, len(ans)), end=" ")
#
#     # 버블 정렬
#     for i in range(len(ans)):
#         for j in range(0, len(ans) - 1 - i):
#             # 행과 열을 곱한 값이 작고,
#             if (ans[j][0] * ans[j][1]) > (ans[j + 1][0] * ans[j + 1][1]):
#                 j1backup = ans[j + 1][:]
#                 jbackup = ans[j][:]
#                 ans[j], ans[j + 1] = j1backup, jbackup
#
#             # 행이 작은 순서대로
#             elif (ans[j][0] * ans[j][1]) == (ans[j + 1][0] * ans[j + 1][1]):
#                 if ans[j][0] > ans[j + 1][0]:
#                     j1backup = ans[j + 1][:]
#                     jbackup = ans[j][:]
#                     ans[j], ans[j + 1] = j1backup, jbackup
#
#     # 정렬 결과대로 출력
#     for i in range(len(ans)):
#         for j in range(len(ans[0])):
#             print(ans[i][j], end=" ")
#     print()
