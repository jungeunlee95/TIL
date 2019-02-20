import sys
sys.stdin = open("종이붙이기", "r")

def find(n):
    if n < 2:
        return 1
    else:
        return find(n-1)+2 * find(n-2)

T = int(input())
for t in range(1, T+1):
    a = int(input())
    n = a//10
    print(f"#{t} {find(n)}")