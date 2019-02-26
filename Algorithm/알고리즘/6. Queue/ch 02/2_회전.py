'''
맨 앞의 숫자 times만큼 맨뒤로 보내기 반복
'''
import sys
sys.stdin = open("2_회전", "r")

T = int(input())
for t in range(1, T+1):
    n, times = map(int, input().split())
    nums = list(map(int, input().split()))

    for i in range(times):
        nums.append(nums.pop(0))
    print(f"#{t} {nums[0]}")