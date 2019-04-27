import sys
sys.stdin = open("1_사칙연산", "r")

def postorder(T):
    if len(G[T]) > 1:
        postorder(int(G[T][1]))
        postorder(int(G[T][2]))
        stack.append(G[T][0])
    else:
        stack.append(G[T][0])

T = 10
for t in range(1, T+1):
    a = int(input())
    G = [0 for _ in range(a + 1)]

    for _ in range(a):
        b = input().split()
        G[int(b[0])] = b[1:]

    stack = []
    postorder(1)
    top=-1
    for i in range(len(stack)):
        if stack[i] == '+':
            stack[top - 1] = stack[top - 1] + stack[top]
            top -= 1
        elif stack[i] == '-':
            stack[top - 1] = stack[top - 1] - stack[top]
            top -= 1
        elif stack[i] == '*':
            stack[top - 1] = stack[top - 1] * stack[top]
            top -= 1
        elif stack[i] == '/':
            stack[top - 1] = int(stack[top - 1] / stack[top])
            top -= 1
        else:
            top += 1
            stack[top] = int(stack[i])
    print(f'#{t} {stack[0]}')


