import sys
sys.stdin = open("5186_이진수2", "r")

T = int(input())
for t in range(1, T+1):
    a = input()
    b = int(a[2:])
    c = 10
    for i in range(len(a)-3):
        c *= 10
    ans = ''
    while True:
        if len(ans) > 12 :
            ans = 'overflow'
            break
        b *= 2
        if b >= c:
            ans += '1'
            b = int(str(b)[1:])
            if b == 0 : break
        else:
            ans += '0'
            if b == 0: break
    print("#{} {}".format(t, ans))