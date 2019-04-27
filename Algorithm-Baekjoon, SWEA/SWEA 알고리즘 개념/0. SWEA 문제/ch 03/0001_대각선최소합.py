'''
배열크기 n * n
x 모양의 크기 k

대각선의 최소합 구하기
'''
import sys
sys.stdin = open("0001_input","r")
# 출력 >> #1 0
T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    G = []
    for i in range(n):
        G.append(list(map(int, input().split())))

    ans = 10000000
    for i in range((n-k)+1):
        for j in range((n-k)+1):
            right_sum = left_sum = 0
            min1 = 0
            for ii in range(k):
                left_sum += G[i+ii][ii+j]
                right_sum += G[i+ii][k-1-ii+j]
            if left_sum > right_sum : min1 = left_sum - right_sum
            else : min1 = right_sum - left_sum
            if ans > min1 : ans = min1

    if k == 1:
        ans = 10000000
        for i in range(n):
            for j in range(n):
                if G[i][j]<ans : ans = G[i][j]
    print("#{} {}".format(t, ans))
