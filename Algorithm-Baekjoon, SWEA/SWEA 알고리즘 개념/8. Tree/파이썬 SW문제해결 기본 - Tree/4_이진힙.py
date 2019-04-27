import sys
sys.stdin = open("4_이진힙", "r")

def insert(n):
    # 일단 바로 뒤에 넣고, 최소힙이니까, 부모보다 작으면 계속 올라가야함
    G.append(nums[n])
    p = n # 내 위치를 p에 저장하고
    # 내 위치가 0보다 크면서 부모가 나보다 크면 바꿔야함
    while(p > 0 and G[p//2] > G[p]): # 만약 부모가 더 크면 => 부모와 위치 바꿔
        temp = G[p//2]
        G[p//2] = G[p]
        G[p] = temp
        p = p//2 # 그리고 이제 내위치가 부모위치, 그럼 또 그 위의 부모랑 비교해서 올라가야함

T = int(input())
for t in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.insert(0,0)
    G = [0]

    for i in range(1, n+1):
        # 리스트가 비어있으면 그냥 첫번째에 넣고
        if i == 1 :
            G.append(nums[i])
        # 아니면 앞의 노드들과 비교해서 넣어야함
        else: insert(i)

    sum1 = 0
    p = len(G)-1
    while  p > 0:
        sum1 += G[p//2]
        p = p//2
    print(f"#{t} {sum1}")



