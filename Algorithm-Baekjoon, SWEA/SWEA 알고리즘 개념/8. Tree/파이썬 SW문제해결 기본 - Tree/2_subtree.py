import sys
sys.stdin = open("2_subtree", "r")

def subtree(N):
    global cnt
    if len(G[N]) != 0:
        if len(G[N]) == 1:
            cnt += 1
            subtree(G[N][0])
        else:
            cnt += 2
            subtree(G[N][0])
            subtree(G[N][1])


T = int(input())
for t in range(1, T + 1):
    E, N = map(int, input().split())
    nodes = list(map(int, input().split()))

    G = [[] for i in range(E + 2)]
    for i in range(0, len(nodes), 2):
        G[nodes[i]].append(nodes[i+1])

    cnt = 1
    subtree(N)
    print(f"#{t} {cnt}")
