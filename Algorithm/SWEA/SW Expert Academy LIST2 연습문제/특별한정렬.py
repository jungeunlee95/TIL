'''
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
N개의 정수가 주어지면
가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
10 1 9 2 8 3 7 4 6 5
주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다.
'''
import sys
sys.stdin = open("특별한정렬", "r")

# 들어온 배열을 정렬하고 시작할거임
def my_sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

T = int(input())
for t in range(1,T+1):
    m = int(input())
    a = list(map(int, input().split()))

    my_sort(a)

    b = [0]*m   # 빈 배열 공간 만들어 놓고

    max1 = m-1  # 최대값의 index : 정렬된 a배열의 길이 - 1
    min1 = 0    # 최소값의 index : 절렬된 a배열의 0

    # 이제 a배열의 길이만큼 돌건데,
    for i in range(m):
        if(i==0 or i%2==0):    # 만약 b의 index가 0이거나, 짝수면 -> 최대값이 거꾸로 들어가야함
            b[i] = str(a[max1])  # b배열에 a배열의 최대값 인덱스를 넣음
            max1 -= 1            # 다음 b의 index부터는 다음 최대값을 넣어야함
        else:                   # b의 index가 홀수 ?  최소값이 순서대로 들어가야함
            b[i] = str(a[min1])
            min1+=1

    print(f'#{t}', end=" ")
    for i in range(10):
        print(b[i], end=" ")
    print()




