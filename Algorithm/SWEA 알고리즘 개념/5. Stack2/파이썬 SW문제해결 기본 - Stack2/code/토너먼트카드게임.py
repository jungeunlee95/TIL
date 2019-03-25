def rsp_game(li, i, j):
    if j-i == 1 or j==i:
        return whowin(li, i, j)

    mid = (i+j)//2
    return whowin(li, rsp_game(li, i, mid), rsp_game(li, mid+1, j))

def whowin(li, a, b):
    if li[a] == li[b]:
        return a
    elif li[a] + 1 == li[b]:
        return b
    elif li[a] == 3 and li[b] == 1:
        return b
    elif li[b] + 1 == li[a]:
        return a
    elif li[b] == 3 and li[a] == 1:
        return a

T = int(input())

for t in range(T):
    N = int(input())
    li_N = list(map(int, input().split()))

    print(f"#{t+1} {rsp_game(li_N, 0, N-1) + 1}")