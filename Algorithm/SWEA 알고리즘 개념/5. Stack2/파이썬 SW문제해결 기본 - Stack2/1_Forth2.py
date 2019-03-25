import sys

sys.stdin = open("1_Forth", "r")

T = int(input())
for t in range(1, T+1):

    a = input().split()
    b = ['-', '+', '/', '*']
    stack = [0] * len(a)
    top = -1
    acnt = 0
    bcnt = 0
    for i in a:
        if(i == '.'):
            break
        if i in b :
            acnt += 1
            if i == '+':
                stack[top-1] = stack[top-1] + stack[top]
                top -= 1
            elif i == '-':
                stack[top-1] = stack[top-1] - stack[top]
                top -= 1
            elif i == '*':
                stack[top-1] = stack[top-1] * stack[top]
                top -= 1
            elif i == '/':
                stack[top-1] = stack[top-1] // stack[top]
                top -= 1
        else:
            bcnt+=1
            top += 1
            stack[top] = int(i)
    if(bcnt - acnt == 1):
        print(f"#{t} {stack[0]}")
    else:
        print(f"#{t} error")