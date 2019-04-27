import sys
sys.stdin = open("11047_input", "r")

N, K  = map(int, input().split())
type = []
for i in range(N):
    type.append(int(input()))

cnt = 0
for i in range(len(type)-1, -1, -1):
    if K == 0 :
        break
    elif type[i] > K:
        continue
    else:
        while K >= type[i]:
            cnt += 1
            K = K - type[i]
print(cnt)