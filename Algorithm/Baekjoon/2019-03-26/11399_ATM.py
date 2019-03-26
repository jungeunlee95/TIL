import sys
sys.stdin = open("11399_input", "r")

n = int(input())
G = list(map(int,input().split()))

G.sort()

total=0
result=[]
for i in G:
    total+=i
    result.append(total)

print(sum(result))