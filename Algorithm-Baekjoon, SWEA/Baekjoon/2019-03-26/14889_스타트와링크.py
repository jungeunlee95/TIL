import sys
import itertools
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

n = int(sys.stdin.readline())
G = []
for i in range(n):
    G.append(list(map(int,sys.stdin.readline().split())))

min = 9999
arr = [i for i in range(n)]
combination_members = itertools.combinations(arr, n//2)
for i in combination_members:
    print(i)


result = []

print(min)



