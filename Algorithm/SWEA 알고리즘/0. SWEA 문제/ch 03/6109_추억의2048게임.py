'''
2048이라는 추억의 게임을 아는가? 2048은 한 때 유명했던 1인용 게임으로, 격자 위에서 숫자가 적힌
타일들을 밀어서 합치고 최종적으로 2048을 만들어 내는 것이 목표인 게임이다.
한번 타일을 밀 때는 상하좌우를 정해서 밀어야 한다.
방향을 정하면 격자 위에 있는 모든 타일이 그 방향으로 밀린다.
만약 어떤 타일이 밀리는 방향에 다른 타일이 있고, 두 타일에 적힌 숫자가 같다면 두 타일은 합쳐져
새로운 하나의 타일이 되고 이 타일에 적힌 숫자는 합쳐진 숫자들의 합이 된다.
이렇게 합쳐져서 만들어진 새로운 타일은 숫자가 같은 다른 타일이 밀려와도 합쳐져서는 안 된다.
만약 같은 숫자가 적힌 타일이 세 개 이상 있을 때는 헷갈리는 경우를 없애기 위해
빨리 벽에 닿게 될 타일을 먼저 민다고
생각한다.

예를 들어 “2 2 4 2 2 2”가 적힌 타일들이 있을 때, 이 타일들을 왼쪽으로 밀면 결과는 “4 4 4 2 0 0”이 된다.
0은 타일이 없는 빈 칸을 나타낸다.

우리는 2048게임을 N×N 크기의 격자에서 하려고 한다.
현재 격자에 어떤 식으로 타일이 있는지 주어지고, 타일들을 이동시킬 방향이 주어질 때,
타일을 모두 이동시키고 나면 격자가 어떻게 변할 지 계산하는 프로그램을 작성하라.

[입력]
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1≤N≤20)과 하나의 문자열
S가 공백 하나로 구분되어 주어진다.

S는 “left”, “right”, “up”, “down”의 넷 중 하나이며
각각 타일들을 왼쪽, 오른쪽, 위쪽, 아래쪽으로 이동시키겠다는 뜻이다.

다음 N개의 줄의 i번째 줄에는 N개의 정수가 공백 하나로 구분되어 주어진다.
이 정수들은 0이거나 2이상 1024이하의 2의 제곱수들이다.
i번째 줄의 j번째 정수는 격자의 위에서 i번째 줄의 왼쪽에서 j번째에 있는 칸에 있는
타일에 어떤 정수가 적혀 있는지 나타내며,

0이면 이 칸에 타일이 없음을 의미한다.

[출력]
각 테스트 케이스마다 ‘#t’(t는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고 한 줄을 띄운 후,
N줄에 걸쳐 격자의 어떤 위치에 어떤 숫자가 적힌 타일이 있는지 입력 형식과 같은 형식으로 출력한다.
'''
import sys
sys.stdin = open("6109_input", "r")

# 1
# T = int(input())
# for t in range(1, T+1):
#     a, b = input().split()
#     N = int(a)
#     G = []
#     for i in range(N):
#         G.append(list(map(int, input().split())))
#
#     if b == "up":
#         for j in range(N):
#             for i in range(N):
#                 if G[i][j]!=0:
#                     top=i
#                     while top+1 != N:
#                         top+=1
#                         if G[top][j]==0:
#                             continue
#                         elif G[top][j]==G[i][j]:
#                             G[i][j]=G[i][j]*2
#                             G[top][j]=0
#                             break
#                         elif G[top][j]!=G[i][j]:
#                             if G[top][j]!=0:
#                                 break
#                             else:
#                                 G[i+1][j]=G[top][j]
#                                 G[top][j]=0
#                             break
#         for i in range(N):
#             for r in range(N - 1):
#                 if G[r][i] == 0:
#                     for k in range(r + 1, N):
#                         if G[k][i] != 0:
#                             G[r][i], G[k][i] = G[k][i], G[r][i]
#                             break
#     if b == "down":
#         for j in range(N):
#             for i in range(N-1,-1,-1):
#                 if G[i][j]!=0:
#                     top=i
#                     while top-1 != -1:
#                         top-=1
#                         if G[top][j]==0:
#                             continue
#                         elif G[top][j]==G[i][j]:
#                             G[i][j]=G[i][j]*2
#                             G[top][j]=0
#                             break
#                         elif G[top][j]!=G[i][j]:
#                             if G[top][j]!=0:
#                                 break
#                             else:
#                                 G[i-1][j]=G[top][j]
#                                 G[top][j]=0
#                             break
#         for i in range(N):
#             for j in range(N-1, -1, -1):
#                 if G[j][i] == 0 :
#                     for k in range(j-1, -1, -1):
#                         if G[k][i] != 0 :
#                             G[j][i], G[k][i] = G[k][i],G[j][i]
#                             break
#     if b == "left":
#         for i in range(N):
#             for j in range(N):
#                 if G[i][j]!=0:
#                     top=j
#                     while top+1 != N:
#                         top+=1
#                         if G[i][top]==0:
#                             continue
#                         elif G[i][top]==G[i][j]:
#                             G[i][j]=G[i][j]*2
#                             G[i][top]=0
#                             break
#                         elif G[i][top]!=G[i][j]:
#                             if G[i][top]!=0:
#                                 break
#                             else:
#                                 G[i][j+1]=G[i][top]
#                                 G[i][top]=0
#                             break
#         for i in range(N):
#             for j in range(N-1):
#                 if G[i][j] == 0:
#                     for k in range(j, N):
#                         if G[i][k] != 0 :
#                             G[i][j], G[i][k] = G[i][k], G[i][j]
#                             break
#     if b == "right":
#         for i in range(N):
#             for j in range(N-1,-1,-1):
#                 if G[i][j]!=0:
#                     top=j
#                     while top-1 != -1:
#                         top-=1
#                         if G[i][top]==0:
#                             continue
#                         elif G[i][top]==G[i][j]:
#                             G[i][j]=G[i][j]*2
#                             G[i][top]=0
#                             break
#                         elif G[i][top]!=G[i][j]:
#                             if G[i][top]!=0:
#                                 break
#                             else:
#                                 G[i][j-1]=G[i][top]
#                                 G[i][top]=0
#                             break
#         for i in range(N):
#             for j in range(N-1, 0, -1):
#                 if G[i][j] == 0:
#                     for k in range(j, -1, -1):
#                         if G[i][k] != 0:
#                             G[i][j], G[i][k] = G[i][k], G[i][j]
#                             break
#     print(f"#{t}")
#     for i in range(N):
#         for j in range(N):
#             print(G[i][j], end=" ")
#         print()



# 2
T = int(input())
for tc in range(T):
    N, direction = input().split()
    N = int(N)
    pan = []
    for _ in range(N):
        pan.append(list(map(int, input().split())))

    if direction == "up":
        for col in range(N):
            onlynum = []
            for row in range(N):
                if pan[row][col] == 0:
                    continue
                else:
                    onlynum.append(pan[row][col])
            # 숫자만 다 받아온 다음에 그 칼럼을 업데이트
            i = 0
            while i + 1 < len(onlynum):
                if onlynum[i] == onlynum[i + 1]:
                    onlynum[i + 1] *= 2
                    onlynum.pop(i)
                i += 1

            # 칼럼에 넣기
            for row in range(N):
                if row < len(onlynum):
                    pan[row][col] = onlynum[row]
                else:
                    pan[row][col] = 0

    elif direction == "down":
        for col in range(N):
            onlynum = []
            for row in range(N - 1, -1, -1):
                if pan[row][col] == 0:
                    continue
                else:
                    onlynum.append(pan[row][col])
            # 숫자만 다 받아온 다음에 그 칼럼을 업데이트
            i = 0
            while i + 1 < len(onlynum):
                if onlynum[i] == onlynum[i + 1]:
                    onlynum[i + 1] *= 2
                    onlynum.pop(i)
                i += 1

            # 칼럼에 넣기
            for row in range(N - 1, -1, -1):
                if N - 1 - row < len(onlynum):
                    pan[row][col] = onlynum[N - 1 - row]
                else:
                    pan[row][col] = 0

    elif direction == "left":
        for row in range(N):
            onlynum = []
            for col in range(N):
                if pan[row][col] == 0:
                    continue
                else:
                    onlynum.append(pan[row][col])
            # 숫자만 다 받아온 다음에 그 칼럼을 업데이트
            i = 0
            while i + 1 < len(onlynum):
                if onlynum[i] == onlynum[i + 1]:
                    onlynum[i + 1] *= 2
                    onlynum.pop(i)
                i += 1

            # 칼럼에 넣기
            for col in range(N):
                if col < len(onlynum):
                    pan[row][col] = onlynum[col]
                else:
                    pan[row][col] = 0

    elif direction == "right":
        for row in range(N):
            onlynum = []
            for col in range(N - 1, -1, -1):
                if pan[row][col] == 0:
                    continue
                else:
                    onlynum.append(pan[row][col])
            # 숫자만 다 받아온 다음에 그 칼럼을 업데이트
            i = 0

            while i + 1 < len(onlynum):
                if onlynum[i] == onlynum[i + 1]:
                    onlynum[i + 1] *= 2
                    onlynum.pop(i)
                i += 1

            # 칼럼에 넣기
            for col in range(N - 1, -1, -1):
                if N - 1 - col < len(onlynum):
                    pan[row][col] = onlynum[N - 1 - col]
                else:
                    pan[row][col] = 0

    print("#%d" % (tc + 1))
    for row in range(N):
        print(' '.join(list(map(str, pan[row]))))



