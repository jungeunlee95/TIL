import sys
sys.stdin = open("5185_이진수", "r")

def B(i):
    output = ""
    for j in range(15, -1, -1):
        output += "1" if i & (1 << j) else "0"
    return output[12:]

T = int(input())
for t in range(1, T+1):
    n, a = input().split()
    result = ''
    for i in a:
        if i.isalpha():
            result += B(ord(i) - ord('A') + 10)
        else:
            result += B(int(i))

    print("#{} {}".format(t, result))