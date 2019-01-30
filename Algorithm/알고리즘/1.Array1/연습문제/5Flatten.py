"""
>문제
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.

M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.

다음은 N=5, M=3이고 5개의 숫자 1 2 3 4 5가 배열 v에 들어있는 경우이다.

이웃한 M개의 합이 가장 작은 경우 1 + 2 + 3 = 6
이웃한 M개의 합이 가장 큰 경우 3 + 4 + 5 = 12
답은 12와 6의 차인 6을 출력한다.

>입력
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )

다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )

>출력
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
"""

'''
T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    M_ls = list(map(int, input().split()))
    position = 0
    count = 0
    while position < N:
        for i in M_ls:
            if i > position+K:
                continue
            else:
                position = i
                count += 1
                break
    print("#"+str(test_case), count)
while문에서 계속 돌아서 그런거같네요.

한번 충전시 position이 첫 정류장이 되고 만약 position+K보다 작은 다른 정류장이 없을시에 그 첫 정류장에서 
계속 머무르게 되는군요. 
문제 보시면 도착할 수 없을 시에는 0을 반환해야합니다. 그 부분을 빼먹으신 듯해요
'''
import sys
sys.stdin = open("input5.txt", "r")

# T = 10
# for tc in range(1,T+1):
#     a = int(input())
#     c = list(map(int, input().split()))
#     for i in range(a):
#         i1,i2 = c.index(max(c)), c.index(min(c))
#         c[i1] -= 1
#         c[i2] += 1
#     print(f'#{tc} {max(c)-min(c)}')
T = 10
for tc in range(1,T+1):
    a = int(input())
    c = list(map(int, input().split()))
    for i in range(a):
        i1,i2 = c.index(max(c)), c.index(min(c))
        c[i1] -= 1
        c[i2] += 1
    print(f'#{tc} {max(c)-min(c)}')
