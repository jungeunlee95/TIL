'''
다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.
다음과 같은 5X5 배열에서 최댓값은 29이다.
a = [
    [4, 4, 3, 2, 1], -> 14
    [2, 2, 1, 6, 5], -> 16
    [3, 5, 4, 6, 7], -> 25
    [4, 2, 5, 9, 7], -> 27
    [8, 1, 9, 5, 6]  -> 29
 ↙ ↓  ↓ ↓ ↓ ↓↘
21  21  14 22 28 26  26
]

[제약 사항]
총 10개의 테스트 케이스가 주어진다.
배열의 크기는 100X100으로 동일하다.
각 행의 합은 integer 범위를 넘어가지 않는다.
동일한 최댓값이 있을 경우, 하나의 값만 출력한다.

[입력]
각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.
'''
import sys
sys.stdin = open("sc_Sum_input", "r")

# for t in range(10):
#     t = int(input())
#     a = []
#     for i in range(100):
#         arr1 = list(map(int, input().split()))
#         a.append(arr1)
#
#     def my_max(n):
#         result = n[0]
#         for i in n:
#             if i > result:
#                 result = i
#         return result
#
#     result = []
#     sum3 = sum4 = 0
#     for i in range(len(a)):
#         sum1 = 0
#         sum2 = 0
#         for j in range(len(a[0])):
#             sum1 += a[i][j]
#             sum2 += a[j][i]
#         result.append(sum1)
#         result.append(sum2)
#
#     num1 = int(len(a) - 1)
#     for i in range(len(a)):
#         sum3 += a[i][i]
#         sum4 += a[i][num1]
#         num1 -= 1
#     result.append(sum3)
#     result.append(sum4)
#
#
#     print(f'#{t} {my_max(result)}')

for t in range(10):
    t = int(input())
    a = []
    for i in range(100):
        arr1 = list(map(int, input().split()))
        a.append(arr1)

    result = []

    # 가로기준 합(sum1)과 세로기준 합(sum2)을 배열에 집어 넣음
    for i in range(len(a)):
        sum1 = sum2 = 0
        for j in range(len(a[0])):
            sum1 += a[i][j]
            sum2 += a[j][i]
        result.append(sum1)
        result.append(sum2)

    sum3 = sum4 = 0  # 대각선 합들 배열에 넣기
    num1 = int(len(a) - 1)  # 왼쪽아래로 내려가는 대각선은 [i]는 증가, [j]는 배열 길이에서 -1씩 줄어듬
    for i in range(len(a)):
        sum3 += a[i][i]
        sum4 += a[i][num1]
        num1 -= 1
    result.append(sum3)
    result.append(sum4)
    ans=max(result)

    print(f'#{t} {ans}')

