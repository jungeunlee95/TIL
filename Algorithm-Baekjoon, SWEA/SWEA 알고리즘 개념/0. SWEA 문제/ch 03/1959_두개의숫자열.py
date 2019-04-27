'''
N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된 숫자열 Bj (j=1~M) 가 있다.
아래는 N =3 인 Ai 와 M = 5 인 Bj 의 예이다.
Ai = [1,5,3]
Bj = [3,6,-7,5,4]

Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.
단, 더 긴 쪽의 양끝을 벗어나서는 안 된다.
Ai =    [1,5,3]
Bj = [3,6,-7,5,4]

서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.
위 예제의 정답은 아래와 같이 30 이 된다.
Ai =      [1,5,3]
Bj = [3,6,-7,5,4]
          -7 25 12  => 30

[제약 사항]
N 과 M은 3 이상 20 이하이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
두 번째 줄에는 Ai,
세 번째 줄에는 Bj 가 주어진다.

[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''
import sys
sys.stdin = open("1959_input","r")

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # n이 더 작게, a가 더 작게
    if n > m : n, m = m, n; a, b = b, a

    max1 =0
    for i in range(m-n+1):
        for j in range(m-n+1):
            sum1 = 0
            for k in range(n):
                sum1 += a[k] * b[i+k]
            if max1 < sum1 : max1 = sum1
    print(f"#{t} {max1}")


