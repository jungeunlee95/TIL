import sys
sys.stdin = open("3_이진탐색", "r")

# 인 오더로 왼쪽 맨 아래(끝)부터 차례대로 삽입을 함
# global num 은 삽입할 데이터를 넣는거임 1부터 들어가야하니까!
T = int(input())
def inorder(T):
    global num
    if T<=n:  # 왼쪽, 오른쪽 자식이 없으면 return
        inorder(T * 2)  # 나의 왼쪽 자식의 idx는 자신의idx * 2
        tree[T]=num
        num+=1
        inorder(T * 2+1)  # 나의 오른쪽 자식의 idx는 자신의idx * 2 + 1

for t in range(1,T+1):
    n=int(input())
    tree=[0]*(n+1)

    num = 1
    inorder(1)
    print(f"#{t} {tree[1]} {tree[n//2]}")