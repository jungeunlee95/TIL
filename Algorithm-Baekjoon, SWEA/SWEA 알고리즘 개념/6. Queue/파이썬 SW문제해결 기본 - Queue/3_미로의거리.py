import sys
sys.stdin = open("3_미로의거리", "r")

def check(x, y):
    if x < 0 or x > n-1 : return False
    if y < 0 or y > n - 1: return False
    if G[x][y] == 1 : return False
    return True

def findExit(queue):
    global cnt, find

    while queue:
        x, y = queue.pop(0)  # 이동할 위치 뽑기

        if G[x][y] == 2 :  find = 1  # 찾았으면 나오기
        elif G[x][y] != 1 :  # 벽이 아닐 경우,
            G[x][y] = 1      # visited 찍고
            for i in range(4): # 4방향 확인하며
                x2 = x + dx[i]
                y2 = y + dy[i]
                if check(x2, y2):
                    queue.append([x2, y2])  # 만약 갈 수 있는 곳이다? 이동할 위치에 넣어
                    cnt += 1                # cnt++
                    findExit(queue)         # 이동할 위치를 다시 호출
                    if find == 1: break     # 만약 찾고 나왔으면 끝
                    else: cnt -=1           # 못찾고 나왔으면 cnt--


T = int(input())
for t in range(1, T+1):
    n = int(input())
    G = [[] for _ in range(n)]
    for i in range(n):
        G[i] = list(map(int, input()))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = []      # 이동할 위치
    cnt = find = 0

    for i in range(n):
        for j in range(n):
            if G[i][j] == 3:
                queue.append([i, j])
                findExit(queue)

    if find == 1:
        print(f"#{t} {cnt-1}")
    else: print(f"#{t} 0")
