import sys
sys.stdin = open("4366_정식이의은행업무","r")

def sum3(j):
    samB[i] = str(j)
    sum1 = 0
    for k in range(len(samB)):
        sum1 += int(samB[k]) * 3 ** (len(samB)-1-k)
    b2.append(sum1)

T = int(input())
for t in range(1, T+1):
    a = input()
    b = input()
    a2 = []
    b2 = []
    for i in range(len(a)):
        samA = list(a)
        if samA[i] == '1': samA[i] = '0'
        elif samA[i] == '0': samA[i] = '1'
        sum1 = 0
        for j in range(len(a)):
            sum1 += int(samA[j]) * 2 ** (len(a)-1-j)
        a2.append(sum1)

    for i in range(len(b)):
        samB = list(b)
        if samB[i] == '0':
            for j in range(1,3):
                sum3(j)
        elif samB[i] == '1':
            for j in range(0,3,2):
                sum3(j)
        elif samB[i] == '2':
            for j in range(0, 2):
                sum3(j)
    for i in range(len(a2)):
        if a2[i] in b2:
            print("#{} {}".format(t, a2[i]))
            break
