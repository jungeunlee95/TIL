import sys
sys.stdin = open("3_이진탐색", "r")

T = int(input())
def inorder(T):
    global num
    if T<=n:
        inorder(T * 2)
        tree[T]=num
        num+=1
        inorder(T * 2+1)

for t in range(1,T+1):
    n=int(input())
    tree=[0]*(n+1)

    num = 1
    inorder(1)
    print(f"#{t} {tree[1]} {tree[n//2]}")