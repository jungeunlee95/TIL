import sys
sys.stdin = open("3_이진탐색", "r")

T = int(input())
for t in range(1, T+1):
    a = int(input())

    b = [0,0]
    for i in range(1,11):
        for j in range(2**i):
            b.append(2+4*(j//2))

    print(f"#{t} {a//2+1} {b[a]}")
