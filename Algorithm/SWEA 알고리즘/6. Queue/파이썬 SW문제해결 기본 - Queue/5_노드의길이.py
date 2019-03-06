import sys
sys.stdin = open("5_노드의길이", "r")

def BFS(S):
    q = []
    q.append(S)

    cnt = 0
    while q:
        for i in range(len(q)):
            S = q.pop(0)
            if not visited[S]:
                visited[S] = True
                for j in range(len(G[S])):
                    if not visited[G[S][j]]:
                        a = G[S][j]
                        q.append(a)
        cnt += 1
        if g in q: return cnt
    return 0

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())

    G = [[] for _ in range(V+1)]

    # 방향성 X
    for i in range(E):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    s, g = map(int, input().split())
    visited = [False]*(V+1)

    print(f"#{t} {BFS(s)}")




