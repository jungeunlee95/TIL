import sys
sys.stdin = open("1_Contact","r")

def BFS(G, start):
    global result # 연락을 보낸 곳

    while queue: # queue에 빈값이 들어오면 끝!
        b = []  # 이전 연락처 저장할 곳
        for i in range(len(queue)):
            b.append(queue.pop(0))

        result = [] # result 공간 다시 연락을 보낼 곳

        # 이전 연락처들을 돌면서 다음 어디로 연락할 지
        for i in range(len(b)):
            if visited[b[i]] == 0: # 그 곳이 연락이 안간 곳이면 연락할 것
                visited[b[i]] = 1   # 방문 체크,
                result.append(b[i])   # 연락을 보낸 곳으로 저장
                for k in range(n+1):  # 연락을 보낸 곳에서 또 연락할 곳이 있는지 확인
                    if G[b[i]][k]== 1 and visited[k] == 0: # 연락할 곳이 있고, 아무도 연락 한 적 없으면
                            queue.append(k) # queue에 넣기
        # print(nextr)
        BFS(G, queue)
    return result


for tc in range(1, 11):
    n, a = map(int, input().split())
    contact_list = list(map(int, input().split()))

    # 노드 연결
    G = [[0]*(n+1) for _ in range(n+1)]

    # 방문해야 할 곳
    visited = [0] * (n + 1)

    # 가는 방향만 +
    for i in range(0, len(contact_list)-1, 2):
        G[contact_list[i]][contact_list[i+1]] += 1

    queue = []
    queue.append(a)
    result = []
    a = BFS(G, queue)
    print(f"#{tc} {max(a)}")


