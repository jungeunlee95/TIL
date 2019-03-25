import sys
sys.stdin = open("1242_암호코드스캔","r")

def B(i):
    output = ""
    for j in range(15, -1, -1):
        output += "1" if i & (1 << j) else "0"
    return output[12:]

keys1 = ['0001101', '0011001', '0010011', '0111101', '0100011',
        '0110001', '0101111', '0111011', '0110111', '0001011']

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    G = [input()+'0' for _ in range(N)]

    G2 = []
    for i in range(N):
        result = ''
        for j in range(M):
            if G[i][j] != '0':
                result += str(G[i][j])
            if G[i][j] == '0':
                if G[i][j+1] != '0' :
                    result += str(G[i][j])
                elif result != '' and result not in G2:
                    G2.append(result)
                    result = ''
    G3 = []
    answer = 0
    for i in G2:
        keys = keys1[:]
        result = ''
        for j in i:
            if j.isalpha():
                result += B(ord(j) - ord('A') + 10)
            else:
                result += B(int(j))

        if len(result) > 55:
            aa = len(result)
            cnt = int(str(int(aa)/56)[0])
            if cnt > 1:
                for ii in range(len(keys)):
                    num1 = ''
                    for jj in keys[ii]:
                        num1 += jj*cnt
                    keys[ii] = num1

            r = []
            while aa > 0:
                if result[aa-(7*cnt):aa] in keys:
                    r.append(keys.index(result[aa-(7*cnt):aa]))
                    aa-=(7*cnt)
                    continue
                aa-=1
            r.reverse()
            sum1 = ans1 = 0
            for i in range(len(r)):
                if i % 2 == 0: sum1 += r[i]
                else: ans1 += r[i]
            ans1 += sum1*3

            if ans1 % 10 == 0:
                for i in r:
                    answer += i
    if answer != 0 : print("#{} {}".format(t, answer))
    else : print("#{} 0".format(t))



