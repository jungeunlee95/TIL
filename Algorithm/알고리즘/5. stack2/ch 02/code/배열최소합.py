import sys
sys.stdin = open('배열최소합.txt','r')

def sel_num(N, i):
    global li_result
    global min_value
    for n in range(N):
        if li_result[n] == -1 and i < N:
            li_result[n] = li_N[n][i]
            if i == N - 1:
                if min_value > sum(li_result):
                    min_value = sum(li_result)
                li_result[n] = -1
                break
            elif sum(li_result) > min_value:
                li_result[n] = -1
                break
            sel_num(N, i + 1)
            li_result[n] = -1


T = int(input())

for t in range(T):
    N = int(input())
    li_N = []

    for n in range(N):
        li_N.append(list(map(int, input().split())))

    li_result = [-1] * N
    min_value = 999
    sel_num(N, 0)

    print(f"#{t + 1} {min_value}")