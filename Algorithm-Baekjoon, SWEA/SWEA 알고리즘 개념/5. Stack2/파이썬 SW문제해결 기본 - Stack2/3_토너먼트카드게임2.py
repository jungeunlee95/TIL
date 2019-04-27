import sys
sys.stdin = open("3_토너먼트카드게임","r")

def play_game(a, b):
    if a[1] == 1:
        if b[1] == 1:
            if a[0] < b[0]:
                winner = a
            else:
                winner = b
        elif b[1] == 2:
            winner = b
        elif b[1] == 3:
            winner = a
    elif a[1] == 2:
        if b[1] == 1:
            winner = a
        elif b[1] == 2:
            if a[0] < b[0]:
                winner = a
            else:
                winner = b
        elif b[1] == 3:
            winner = b
    elif a[1] == 3:
        if b[1] == 1:
            winner = b
        elif b[1] == 2:
            winner = a
        elif b[1] == 3:
            if a[0] < b[0]:
                winner = a
            else:
                winner = b
    return winner


def devision(group, lst):
    if len(group) == 1:
        lst.append(*group)
        winners.append(*group)
        if len(lst) == 2:
            b = lst.pop(-1)
            a = lst.pop(-1)
            winners.pop()
            winners.pop()
            winner = play_game(a, b)
            winners.append(winner)

    else:
        cnt = len(group)
        pivot = (1+cnt) // 2
        tmp = list()
        for i in [group[:pivot], group[pivot:]]:
            devision(i, tmp)

for t in range(int(input())):
    n = int(input())
    value = list(map(int, input().split()))

    group = []
    for i in range(n):
        group.append([i+1, value[i]])

    winners = []
    while True:
        devision(group, [])
        group = winners.copy()
        winners.clear()
        if len(group) == 1:
            break
    print("#{} {}".format(t+1, *group[0]))