import sys
sys.stdin = open("중위순회", "r")

def preorder_traverse(T):
    if T != '' :
        T = int(T)
        preorder_traverse(G[T][1])
        result.append(G[T][0])
        preorder_traverse(G[T][2])


# 1
T = 10
for t in range(1, T+1):
    length = int(input())
    G = [[""]*4 for _ in range(length+1)]
    #     alpa. L,  R,  P(부모)
    # G = [['', '', '', ''],
    #      ['', '', '', ''], 1
    #      ['', '', '', ''], 2
    #      ['', '', '', ''], 3
    #      ['', '', '', ''], 4
    #      ['', '', '', ''], 5
    #      ['', '', '', ''], 6
    #      ['', '', '', ''], 7
    #      ['', '', '', ''], 8

    for i in range(length):
        a = list(input().split())
        if(len(a)==4):  # 4개면 왼쪽자식, 오른쪽자식에 P추가
            G[int(a[0])][0] = a[1]
            G[int(a[0])][1] = a[2]
            G[int(a[0])][2] = a[3]
            if(G[int(a[2])][3] == ''): G[int(a[2])][3] = a[0]
            if(G[int(a[3])][3] == ''): G[int(a[3])][3] = a[0]
        elif(len(a)==3): # 3개면 왼쪽 자식에만 P추가
            G[int(a[0])][0]= a[1]
            G[int(a[0])][1] = a[2]
            if(G[int(a[2])][3] == ''): G[int(a[2])][3] = a[0]
        else: # 아니면 그냥 내정보만
            G[int(a[0])][0]=a[1]

    T = 0
    # 출발지점 찾기 
    for i in range(1, len(G)):
        if(G[i][3] == ''):
            T = str(i)
            break
    # 문장 담을 배열 
    result = []
    preorder_traverse(T)
    # 출력
    print(f"#{t}", end = " ")
    for i in result:
        print(i, end="")
    print()


# 2
# T = 10
# for t in range(1, T+1):
#     length = int(input())
#     G = [[""]*4 for _ in range(length+1)]
#
#     for i in range(length):
#         a = list(input().split())
#         if(len(a)==4):  # 4개면 왼쪽자식, 오른쪽자식에 P추가
#             G[int(a[0])][0] = a[1]
#             G[int(a[0])][1] = a[2]
#             G[int(a[0])][2] = a[3]
#             if(G[int(a[2])][3] == ''): G[int(a[2])][3] = a[0]
#             if(G[int(a[3])][3] == ''): G[int(a[3])][3] = a[0]
#         elif(len(a)==3): # 3개면 왼쪽 자식에만 P추가
#             G[int(a[0])][0]= a[1]
#             G[int(a[0])][1] = a[2]
#             if(G[int(a[2])][3] == ''): G[int(a[2])][3] = a[0]
#         else: # 아니면 그냥 내정보만
#             G[int(a[0])][0]=a[1]
#
#     # 문장 담을 배열
#     result = []
#     preorder_traverse(1)
#
#     print(f'#{t} {"".join(result)}')


# 3
# def inord(root):
#     global tree
#     global ans
#     if root:
#         inord(tree[root][0])
#         ans += tree[root][2]
#         inord(tree[root][1])
# for tc in range(10):
#     N = int(input())
#
#     tree = [[0, 0, 0] for i in range(N + 1)]
#     ans = ''
#
#     for n in range(N):
#         s = input().split()
#         tree[int(s[0])][2] = s[1]
#         try:
#             tree[int(s[0])][0] = int(s[2])
#         except IndexError:
#             continue
#         try:
#             tree[int(s[0])][1] = int(s[3])
#         except IndexError:
#             continue
#
#     inord(1)
#
#     print('#{} {}'.format(tc + 1, ans))