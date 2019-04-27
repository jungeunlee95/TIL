'''
섬 크기와 배열이 주어짐, 최대 높이와 최대 섬
출력 >> #1 2 4
'''
import sys
sys.stdin = open("input","r")

# 최대 높이의 섬 찾는 함수
def findsum(x, y):
    global max1
    # 가로
    while True:
        if G[x][y] == 0: break
        if G[x][y] != 0:
            if max1 < G[x][y]: max1 = G[x][y]
            G[x][y] = 0
            y += 1


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    G = [[0] * (n + 1)]  # 위에 padding
    for i in range(n):
        G.append([0] + list(map(int, input().split())) + [0])  # 왼쪽,오른쪽 padding

    max1 = cnt = 0

    # 섬개수, 위,왼쪽이 0이면 새로운 섬!
    for i in range(n + 1):
        for j in range(n + 1):
            if G[i][j] != 0:
                if (G[i][j - 1] == 0 and G[i - 1][j] == 0): cnt += 1

    # 최대 높이 찾기
    for i in range(n + 1):
        for j in range(n + 1):
            if G[i][j] != 0:
                findsum(i, j)

    print("#{} {} {}".format(t, cnt, max1))
