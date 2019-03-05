import sys
sys.stdin = open("4_이진힙", "r")

def insert(n):
    G.append(nums[n])
    p = n
    while(p > 1 and G[p//2] > G[p]):
        temp = G[p//2]
        G[p//2] = G[p]
        G[p] = temp
        p = p//2

T = int(input())
for t in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.insert(0,0)
    G = [0]

    for i in range(1, n+1):
        if i == 1 :
            G.append(nums[i])
        else: insert(i)

    sum1 = 0
    p = len(G)-1
    while  p > 0:
        sum1 += G[p//2]
        p = p//2
    print(f"#{t} {sum1}")



