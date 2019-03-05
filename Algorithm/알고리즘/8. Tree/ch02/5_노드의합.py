import sys
sys.stdin = open("5_노드의합","r")

def postOrder(idx):
    if idx>n:
        return 0

    if tree[idx]!=0:
        return tree[idx]

    else:
        a=postOrder(2*idx)
        b=postOrder(2*idx+1)
        tree[idx]=a+b
        return tree[idx]

T = int(input())
for t in range(1,T+1):
    n,m,l=list(map(int,input().split()))

    tree=[0]*(n+1)

    for i in range(m):
        a=list(map(int,input().split()))
        tree[a[0]]=a[1]

    postOrder(1)
    print(f"#{t} {tree[l]}")