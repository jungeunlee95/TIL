'''
숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.

"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"

0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.

예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.

[입력]

입력 파일의 첫 번째 줄에는 테스트 케이스의 개수가 주어진다.

그 다음 줄에 #기호와 함께 테스트 케이스의 번호가 주어지고 공백문자 후 테스트 케이스의 길이가 주어진다.

그 다음 줄부터 바로 테스트 케이스가 주어진다. 단어와 단어 사이는 하나의 공백으로 구분하며,
문자열의 길이 N은 100≤N≤10000이다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 정렬된 문자열을 출력한다.
'''
import sys
sys.stdin = open("input", "r")

# 1
# def swap(nums, j, j2):
#     nums[j], nums[j2] = nums[j2], nums[j]
# # dict 만들기
# num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# nums_dict = {}
# for i in range(len(num_list)):
#     nums_dict[num_list[i]] = i
#
# T = int(input())
# for t in range(1, T+1):
#     a = int(input().split()[1])
#     nums = input().split()
#
#     for i in range(a-1):
#         for j in range(a-i-1):
#             if nums_dict[nums[j]] > nums_dict[nums[j+1]]:
#                 swap(nums, j, j+1)
#
#     print(f'#{t}')
#     print(' '.join(nums))

# 2
def my_sort(nums):
    nums_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3,
               'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    result = [[], [], [], [], [], [], [], [], [], []]

    for i in range(len(nums)):
        result[nums_dict[nums[i]]].append(nums[i])
    return result

T = int(input())
for t in range(1, T+1):
    a = int(input().split()[1])
    nums = input().split()
    result = my_sort(nums)

    print(f'#{t}')
    for i in range(10):
        for j in range(len(result[i])):
            print(result[i][j], end=" ")
    print()

# 3
def my_sort(a, nums):
    num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    nums_dict = {}
    for i in range(len(num_list)):
        nums_dict[num_list[i]] = i

    result = [[] for _ in range(10)]  # [[], [], [], [], [], [], [], [], []]

    for i in range(a):
        result[nums_dict[nums[i]]].append(nums[i])

    for i in range(10):
        for j in range(len(result[i])):
            print(result[i][j], end=" ")
    print()


T = int(input())
for t in range(1, T+1):
    a = int(input().split()[1])
    nums = input().split()

    print(f'#{t}')
    result = my_sort(a, nums)

# 4
# def changer(inputList):
#     numList = [0] * 10
#     numDict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3,
#                'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
#     numName = list(numDict.keys())
#     for idx in inputList:
#         numList[numDict[idx]] += 1
#     for idx in range(0, 10):
#         if numList[idx] != 0:
#             for i in range(numList[idx]):
#                 print(str(numName[idx]) + " ", end=" ")
#     print("")
#
#
# T = int(input())
#
# for i in range(T):
#     TC, n = input().split()
#     inputList = input().split()
#     print(f'{TC}')
#     changer(inputList)