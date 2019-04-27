import sys
sys.stdin = open("5_노드의합","r")

# def postOrder(idx):
#     if idx>n:
#         return 0
#
#     if tree[idx]!=0:
#         return tree[idx]
#
#     else:
#         a=postOrder(2*idx)
#         b=postOrder(2*idx+1)
#         tree[idx]=a+b
#         return tree[idx]
#
# T = int(input())
# for t in range(1,T+1):
#     n,m,l=list(map(int,input().split()))
#
#     tree=[0]*(n+1)
#
#     for i in range(m):
#         a=list(map(int,input().split()))
#         tree[a[0]]=a[1]
#
#     postOrder(1)
#     print(f"#{t} {tree[l]}")


'''
리스트 범위를 n+2만큼 잡아
n=5, m=3, l=2
4 1
5 2
3 3 일때, 
           1  2  3  4  5
tree = [0, 0, 0, 3, 1, 2, 0]
N-M부터 숫자 넣어야함(5-3=2)
2번 인덱스는 자식 두개의 합을 넣어야함 

근데 마지막이 자식이 하나만 있을 수도 있으니까,(오른쪽자식이 존재 X)
index 를 N+2로 잡아줘야함!
'''
T = int(input())
for t in range(1, T+1):
    N, M, pos = map(int, input().split())
    tree = [0 for i in range(N+2)]

    for i in range(M):
        idx, val = map(int, input().split())
        tree[idx] = val

    for i in range(N-M, 1, -1):
        tree[i] = tree[i*2] + tree[i*2+1]

    print(f"#{t} {tree[pos]}")