"""
>문제 : SW Expert Academy LIST1 연습문제
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력

3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
"""
import sys
sys.stdin = open("input.txt", "r")

# def my_min(n):
#     result = n[0]
#     for i in n:
#         if i < result:
#             result = i
#     return result
#
# def my_max(n):
#     result = n[0]
#     for i in n:
#         if i > result:
#             result = i
#     return result

# 2
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    print("#{} {}".format(tc, max(nums)-min(nums)))

# 3
# def my_sub(n):
#     min1 = n[0]
#     max1 = n[0]
#     for i in n:
#         if i < min1 : min1 = i
#         if i > max1 : max1 = i
#     return max1-min1

# T = int(input())
# for tc in range(1,T+1):
#     n = int(input())
#     nums = list(map(int, input().split()))
#     a = my_sub(nums)
#     print(f'#{tc} {a}')