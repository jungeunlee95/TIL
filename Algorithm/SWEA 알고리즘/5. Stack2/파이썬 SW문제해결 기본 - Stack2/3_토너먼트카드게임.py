import sys
sys.stdin = open("3_토너먼트카드게임","r")

def devision(group):
    if(len(group) == 1):


for t in range(int(input())):
    n = int(input())
    value = list(map(int, input().split()))

    group = []
    for i in range(n):
        group.append([i+1, value[i]])

    winners = []
    while True:
        devision(group)




    print("#{} {}".format(t+1, group[0][0]))