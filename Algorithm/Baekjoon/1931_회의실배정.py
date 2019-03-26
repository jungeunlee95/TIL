import sys
sys.stdin = open("1931_input", "r")

n = int(input())
G = []
for i in range(n):
    G.append(list(map(int, input().split())))

num = 0
first = 99999999999
next = []
for i in range(len(G)):
    if G[i][1]<first:
        first = G[i][1]
        num = i
    next.append(G[i][1])

cnt = 1
b = []
while True:
    for j in range(n):
        if G[j][0] >= first:
            b.append(j)
    if len(b) == 0 :
        break
    ran = 99999999999
    for k in b:
        if next[k] < ran:
            ran = next[k]
    first = ran
    b = []
    cnt += 1

print(cnt)

