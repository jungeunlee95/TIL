def BFS(G, v): # G:그래프, v: 탐색 시작점
    queue.append(v)
    while 0 in visited:
        a = queue.pop(0)
        if visited[a-1] == 0:
            visited[a-1] = 1 # visited 체크
            result.append(a)
        for i in range(8):
            if G[a][i] == 1:
                queue.append(i)
        if(0 not in visited): break

a = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
G = [[0]*8 for _ in range(8)]

for i in range(0, len(a)-1, 2):
    G[a[i]][a[i + 1]] += 1
    G[a[i + 1]][a[i]] += 1


visited = [0] * 7
front = rear = None
queue = []
result = []
BFS(G, 1)
print(result)
