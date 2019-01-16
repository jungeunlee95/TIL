"""
강변에 빌딩들이 옆으로 빽빽하게 밀집한 지역이 있다.

이곳에서는 빌딩들이 너무 좌우로 밀집하여, 강에 대한 조망은 모든 세대에서 좋지만 왼쪽 또는 오른쪽 창문을 열었을 때
바로 앞에 옆 건물이 보이는 경우가 허다하였다.

그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때
조망권이 확보된다고 말한다.

빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.

아래와 같이 강변에 8채의 빌딩이 있을 때,
 연두색으로 색칠된 여섯 세대에서는 좌우로 2칸 이상의 공백이 존재하므로 조망권이 확보된다. 따라서 답은 6이 된다.

[제약 사항]

가로 길이는 항상 1000이하로 주어진다.

맨 왼쪽 두 칸과 맨 오른쪽 두 칸에는 건물이 지어지지 않는다. (예시에서 빨간색 땅 부분)

각 빌딩의 높이는 최대 255이다.

[입력]

입력 파일의 첫 번째 줄에는 테스트케이스의 길이가 주어진다. 그 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 조망권이 확보된 세대의 수를 출력한다.
"""
import sys
sys.stdin = open("input1.txt", "r")   #-->  같은 경로에 있으면 나 이파일에서 바로 읽어서 처리할게

# 1
# for test_case in range(1, 11):
#     a = int(input())
#     b = list(map(int,input().split()))
#     cnt =0
#     for i in range(2, len(b)-2):
#         result = [b[i-2], b[i-1], b[i+1], b[i+2]]
#         if(max(result)<b[i]):
#             cnt += b[i] - max(result)
#     if(test_case == 10):
#         print(f'#{test_case} {cnt}', end="")
#     else:
#         print(f'#{test_case} {cnt}')

# # 2
for test_case in range(1, 11):
    a = int(input())
    b = list(map(int,input().split()))
    cnt =0
    for i in range(2, len(b)-2):
        max_num = max(b[i-2], b[i-1], b[i+1], b[i+2])
        if(max_num<b[i]):
            cnt += b[i] - max_num
    # print(f'#{test_case} {cnt}')
    print(test_case,cnt)
# # 3
# def my_max(nums):
#     my_max = 0
#     for i in nums:
#         if(i>my_max):
#             my_max = i
#     return my_max

# for test_case in range(1, 11):
#     a = int(input())
#     b = list(map(int,input().split()))
#     cnt =0

#     for i in range(2, len(b)-2):
#         max_num = my_max([b[i-2], b[i-1], b[i+1], b[i+2]])
#         if(max_num<b[i]):
#             cnt += b[i] - max_num
#     print(f'#{test_case} {cnt}')





## 1 691
## 2 9092
## 3 8998
## 4 9597
## 5 8757
## 6 10008
## 7 10194
## 8 10188
## 9 9940
## 10 8684