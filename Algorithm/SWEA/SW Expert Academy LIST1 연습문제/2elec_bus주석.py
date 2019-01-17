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
                backup = p + k # 내가 이전에 충전했던 곳으로 돌아왔는지 확인하기 위한 변수
                for i in range(p+k-1, p-1, -1): # 최대거리(p+k)에 충전소가 없으니, 가장 최근에 충전했던(p)까지 충전기가 어디 있는지 봐야함
                    backup -=1 # 한칸씩 뒤로 갈때마다 체크
                    if station[i]==1: # 만약, 뒤로가서 충전기를 찾았으면 충전!
                        cnt+=1
                        p=i
                        break
                    if backup == p: # 근데.. 내가 찾은 그 충전기가 전에 이미 충전했던 곳이면? 0 끝.
                        cnt = 0
                        p=n
                        break
    print(f'#{tc} {cnt}')


