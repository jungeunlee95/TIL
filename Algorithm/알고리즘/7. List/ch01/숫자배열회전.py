'''
N x N 행렬이 주어질 때,
시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.

[제약 사항]
N은 3 이상 7 이하이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N이 주어지고,
다음 N 줄에는 N x N 행렬이 주어진다.

[출력]
출력의 첫 줄은 '#t'로 시작하고,
다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.
입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''
import sys
sys.stdin = open("숫자배열회전", "r")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    G = [[0] * N for i in range(N)]
    for i in range(N):
        G[i] = list(input().split())
   #       18   15   12    9    6   3
   #  270  ↓   ↓   ↓   ↓   ↓   ↓    180
   # G = [['6', '9', '4', '7', '0', '5'], ← 17
   #      ['8', '9', '9', '2', '6', '5'], ← 14
   #      ['6', '8', '5', '4', '9', '8'], ← 11
   #      ['2', '2', '7', '7', '8', '4'], ← 8
   #      ['7', '5', '1', '9', '7', '9'], ← 5
   #      ['8', '9', '3', '9', '7', '6']] ← 2
   #  90    ↑   ↑   ↑   ↑   ↑   ↑
   #        1    4    7    10   13   16
    '''
    90도: 
    1번 : [N-1][0], [N-2][0], [N-3][0], [N-4][0] ...
    2번 : [N-1][1], [N-2][1], [N-3][1], [N-4][1] ...
    
    180도
    1번 : [N-1][N-1], [N-1][N-2], [N-1][N-3], [N-1][N-4] ...
    2번 : [N-2][N-1], [N-2][N-2], [N-2][N-3], [N-2][N-4] ...
    
    270도
    1번 : [0][N-1], [1][N-1], [2][N-1], [3][N-1] ...
    2번 : [0][N-2], [1][N-2], [2][N-2], [3][N-2] ...
    '''

    print(f"#{t} ")
    for i in range(N):
        #        90, 180, 270
        result = [[], [], []]
        for j in range(N):
            result[0].append( G[N-j-1][i] )
            result[1].append( G[N-1-i][N-1-j] )
            result[2].append( G[j][N-1-i] )
        for i in range(3):
            for num in result[i]:
                print(num, end="")
            print(" ", end="")
        print()

# 2
# T = int(input())
# for tc in range(1, T + 1):
#     m = int(input())
#     mat = [[0] * m for i in range(m)]
#     for i in range(m):
#         aline = list(input().split())
#         mat[i] = aline
#
#     print(f"#{tc}")
#
#     for i in range(m):
#         result = [''] * 3
#         for j in range(m):
#             result[0] += mat[m - j - 1][i]
#             result[1] += mat[m - i - 1][m - j - 1]
#             result[2] += mat[j][m - i - 1]
#         print(' '.join(result))

# 3
# def rotate90(A, B):
#     for i in range(matN):
#         for j in range(matN):
#             B[j][matN-i-1] = A[i][j]
#
# TC = int(input())
# for tc in range(1, TC+1):
#     matN = int(input())
#     mat0 = [[0] * matN for _ in range(matN)]
#     mat1 = [[0] * matN for _ in range(matN)]
#     mat2 = [[0] * matN for _ in range(matN)]
#     mat3 = [[0] * matN for _ in range(matN)]
#
#     for i in range(matN):
#         mat0[i] = list(map(int, input().split()))
#
#     rotate90(mat0, mat1)
#     rotate90(mat1, mat2)
#     rotate90(mat2, mat3)
#
#     print("#%d"%tc)
#
#     for i in range(matN):
#         for j in range(matN):
#             print("%d"%mat1[i][j], end='')
#         print(end=' ')
#         for j in range(matN):
#             print("%d"%mat2[i][j], end='')
#         print(end=' ')
#         for j in range(matN):
#             print("%d"%mat3[i][j], end='')
#         print()

