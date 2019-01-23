"""
>문제
버스는 0번에서 종점 N번 정류장까지 이동, 
한번충전->최대 이동가능 정류장 수 K 
최소 몇 번의 충전을 해야 종점에 도착할 수 있는지출력

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력
출발지에는 항상 충전기가 설치되어 있음 but 충전횟수 포함 ㄴㄴ

>입력
ex)
3               ->test case
3 10 5          -> k, n, m  => k:한번충전으로 최대 이동거리, n:총 정류장 수, m:충전소 수
1 3 5 7 9       -> 어디 정류장에 충전소 있는지
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17


>출력
#과 노선번호, 빈칸, 최소 충전횟수 또는 0을 출력
"""

import sys
sys.stdin = open("input2.txt", "r")

T = int(input())
for tc in range(1, T+1):
    k, n, m = list(map(int, input().split()))
    c = list(map(int, input().split())) # 충전기가 설치된 곳  각각 인덱스의 차이 > k 면 0 출력
    station = [0]*(n+1) # 총 몇개의 정류장이 있는지 공간 만들기 ex)n=10 --> 0~10번지
    p, cnt, ck = 0, 0, 0 # p:현재위치, cnt:충전 수, ck: 얘는 가능한 앤가?

    for i in range(m):  # station에 충전기가 설치된 번지수에 1을 넣어줌
        station[c[i]] = 1

    for i in range(m-1):
        if(c[i+1]-c[i]>k): # 만약에 충전기가 설치된 정류장의 사이가, k보다 크면
            ck = 1          # 체크!
    if(ck==1):              # 체크가 1이면. cnt = 0으로 끝
        cnt = 0
    else:                   # 아니면 돌기 시작
        while(p+k<n):   # 내 위치 + 갈 수 있는 거리 < 총 거리
            if (p + k >= n): # 총 정류장을 넘으면 stop
                break
            elif(station[p+k]==1):  # 만약, 내가 갈 수 있는 만큼 왔는데(최대거리) 1이면(충전기가 있으면) 충전
                cnt+=1
                p=p+k
            else:   # 최대거리 왔는데 충전기 없으면 한칸씩 돌아가면서 충전기 찾아야함
                for i in range(p+k-1, p-1, -1): # 최대거리(p+k)에 충전소가 없으니, 가장 최근에 충전했던(p)까지 충전기가 어디 있는지 봐야함                  
                    if station[i]==1: # 만약, 뒤로가서 충전기를 찾았으면 충전!
                        cnt+=1
                        p=i
                        break
    print(f'#{tc} {cnt}')


# # 2 REVIEW
# T = int(input())
# for tc in range(1, T+1):
#     K,N,M= list(map(int, input().split()))
#     c = list(map(int, input().split())) 
#     stations = [0] * (N+1)
    
#     for i in range(M):
#         stations[c[i]] = 1

#     cnt = cur = 0 # cur:버스위치
#     while(True):
#         pre = cur # 이전위치는 내위치, 내위치 저장 왜냐면 다시 돌아오면 0 이니까
#         cur += K
#         if cur >= N:
#             break
#         if stations[cur] == 1:
#             cnt += 1
#         else:
#             for i in range(1, K+1):
#                 if stations[cur-i] == 1:
#                     cur -= i
#                     cnt += 1
#                     break
#             if cur == pre:
#                 cnt = 0
#                 break
#     print("#%d" % tc, cnt)

