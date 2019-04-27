import sys
sys.stdin = open("14889_input", "r")

def point(arr):
    global min
    a = b = 0
    for i in range(n//2):
        for j in range(n//2):
            if i != j:
                a += G[arr[i]][arr[j]]
    for i in range(n//2, n):
        for j in range(n//2, n):
            if i!=j:
                b += G[arr[i]][arr[j]]
    if a > b:
        a, b = b, a
    if b - a < min:
        min = b-a

def permutation(n, k):
    if k == n:
        return
    else:
        for i in range(k, n-1):
            arr[k], arr[i] = arr[i], arr[k]
            permutation(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]
        test = []
        for i in range(n//2):
            test.append(arr[i])
        if test not in result:
            result.append(test)
            point(arr)

n = int(sys.stdin.readline())
G = []
for i in range(n):
    G.append(list(map(int,sys.stdin.readline().split())))

min = 9999
arr = [i for i in range(n)]
result = []
permutation(len(arr), 0)

print(min)



