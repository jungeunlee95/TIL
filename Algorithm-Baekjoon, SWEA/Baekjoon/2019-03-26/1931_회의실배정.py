import sys
sys.stdin = open("1931_input", "r")

# 1
N = int(input())
schedule = [[0, 0] for _ in range(N)]

for _ in range(N):
    schedule[_][0], schedule[_][1] = map(int, input().split())

schedule = sorted(schedule, key=lambda x: (x[1], x[0]))

end = 0
cnt = 0
for s in schedule:
    if s[0] >= end:
        cnt += 1
        end = s[1]

print(cnt)

# 2
# n = int(input())
# G = []
# for i in range(n):
#     G.append(list(map(int, input().split())))
# 
# num = 0
# first = 99999999999
# next = []
# for i in range(len(G)):
#     if G[i][1]<first:
#         first = G[i][1]
#         num = i
#     next.append(G[i][1])
# 
# cnt = 1
# b = []
# while True:
#     for j in range(n):
#         if G[j][0] >= first:
#             b.append(j)
#     if len(b) == 0 :
#         break
#     ran = 99999999999
#     for k in b:
#         if next[k] < ran:
#             ran = next[k]
# 
#     first = ran
#     b = []
#     cnt += 1
# 
# print(cnt)

