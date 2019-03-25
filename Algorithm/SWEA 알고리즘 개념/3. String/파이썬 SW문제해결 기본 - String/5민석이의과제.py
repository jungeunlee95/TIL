'''
민석이는 교수가 되었고, 이번에 처음으로 맡은 과목에 수강생이 N명이다.
민석이는 처음으로 과제를 내었다.
그리고 제출한 사람의 목록을 받았다.

수강생들은 1번에서 N번까지 번호가 매겨져 있고, 어떤 번호의 사람이 제출했는지에 대한 목록을 받은 것이다.
과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하는 프로그램을 작성하라.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 수강생의 수를 나타내는 정수 N(2≤N≤100)과
과제를 제출한 사람의 수를 나타내는 정수 K(1≤K≤N)가 공백으로 구분되어 주어진다.
두 번째 줄에는 과제를 제출한 사람의 번호 K개가 공백으로 구분되어 주어진다.
 번호는 1이상 N이하의 정수이며 같은 번호가 두 번 이상 주어지는 경우는 없다.

[출력]
각 테스트 케이스마다 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력한다.
'''
import sys
sys.stdin = open("5민석이의과제", "r")

# 1
# def my_sort(a):
#     for i in range(len(a)-1):
#         for j in range(len(a)-i-1):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a
#
# T = int(input())
# for t in range(1, T+1):
#     total, save = map(int, input().split())
#     nums = list(map(int, input().split()))
#
#     result = []
#     for i in range(1,total+1):
#         if i not in nums:
#             result.append(i)
#     result = my_sort(result)
#     print(f"#{t}", end=" ")
#     for i in result:
#         print(i, end=" ")
#     print()

# 2
T = int(input())
for t in range(1, T+1):
    total, save = map(int, input().split())
    nums = list(map(int, input().split()))
    result = [i for i in range(1, total+1)]

    # 과제 제출 한사람 0
    for i in range(save):
        result[nums[i]-1] = 0

    # 안한사람 출력
    print("#{}".format(t), end = " ")
    for i in range(total):
        if result[i]!= 0:
            print(result[i], end = " ")
    print()



