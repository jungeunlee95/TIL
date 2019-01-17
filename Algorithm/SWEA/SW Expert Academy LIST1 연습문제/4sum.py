"""
>문제 : SW Expert Academy LIST1 연습문제
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력
ex) 1,2,3,10,9,8,7,6,5,4
-->최소값 1+2+3 = 6
-->최대값 10+9+8 = 27
---> 27 - 6 = 21 출력

입력)
3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176

"""
import sys
sys.stdin = open("input4.txt", "r")

T = int(input())
for tc in range(1,T+1):
    a, b = list(map(int,input().split()))
    c = list(map(int, input().split()))
    max1=0
    min1=sum(c)
    for i in range(a-(b-1)):
        t = 0
        for j in range(b):
            t += c[i+j]
        if(t>max1):
            max1=t
        if(t<min1):
            min1=t
    print(f'#{tc} {max1 - min1}')

