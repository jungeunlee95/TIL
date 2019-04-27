import sys
sys.stdin = open("Magnetic", "r")

for t in range(1,11):
    a = int(input())
    b = []
    for i in range(a):
        c = list(map(int, input().split()))
        b.append(c)

    result = 0
    for i in range(a):
        stack = [0] * (a+1)
        top = -1
        cnt = 0
        for j in range(a):
            if(b[j][i] != 0):
                if(b[j][i] == 2):
                    top += 1
                    stack[top] = 2
                elif(b[j][i] == 1):
                    if 2 in stack:
                        if(stack[top] == 2):
                            cnt+=1
                            stack = [0] * (a+1)
                            top = -1
        result += cnt
    print(f"#{t} {result}")

# 2
# for tc in range(1, 11):
#     input()
#     table = []
#     cnt = 0
#
#     for i in range(100):
#         table.append(input())
#
#     for i in range(0, 200, 2):
#         state = False
#         for j in range(100):
#             if table[j][i] != "0":
#                 if table[j][i] == '1':
#                     state = True
#                 elif table[j][i] == '2':
#                     if state:
#                         state = False
#                         cnt += 1
#     print(f"#{tc} {cnt}")


# 3
# for tc in range(10):
#     N = int(input())
#     table = []
#     for row in range(N):
#         table.append(list(map(int, input().split())))
#
#     count = 0  # 교착상태 개수
#     # 왼쪽 부터 차례로 돌면서
#     for i in range(N):
#         stack = 0  # 이걸 잘못 넣어서 아까 오류남
#         # 스택처럼 확인할 수 있도록
#         for j in range(N):
#             if table[j][i] == 1:
#                 stack = 1
#             elif table[j][i] == 2:
#                 if stack == 1:
#                     count += 1
#                     stack = 0
#     print("#{} {}".format(tc + 1, count))

