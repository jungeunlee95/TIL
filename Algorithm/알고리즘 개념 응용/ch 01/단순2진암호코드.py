import sys
sys.stdin = open("단순2진암호코드", "r")
def B(i):
    output = ""
    for j in range(15, -1, -1):
        output += "1" if i & (1 << j) else "0"
    return output[12:]

keys = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111' ,'0001011']

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    G = []
    for i in range(N):
        G.append(input())
    result = []
    a = b = 0
    for i in range(N):
        for j in range(M-5):
            if G[i][j:j+7] in keys:
                a = i
                b = j
                break
    r = []
    for i in range(b, len(G[a]), 7):
        if G[a][i:i+7] in keys:
            r.append(keys.index(G[a][i:i+7]))

    sum1 = 0
    result = 0
    for i in range(len(r)):
        if i%2==0:
            sum1 += r[i]
        else: result+= r[i]
    result += sum1*3
    ans = 0
    if result % 10 == 0:
        for i in r:
            ans += i
    print("#{} {}".format(t, ans))

