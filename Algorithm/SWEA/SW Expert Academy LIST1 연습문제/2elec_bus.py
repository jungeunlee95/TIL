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
    c = list(map(int, input().split())) 
    station = [0]*(n+1)
    p, cnt, ck = 0, 0, 0

    for i in range(m):
        station[c[i]] = 1

    for i in range(m-1):
        if(c[i+1]-c[i]>k):
            ck = 1
    if(ck==1):
        cnt = 0
    else:
        while(p<n):
            if (p + k >= n):
                break
            elif(station[p+k]==1):
                cnt+=1
                p=p+k
            else:
                backup = p + k
                for i in range(p+k-1, p-1, -1):
                    backup -=1
                    if station[i]==1:
                        cnt+=1
                        p=i
                        break
                    if backup == p:
                        cnt = 0
                        p=n
                        break
    print(f'#{tc} {cnt}')


