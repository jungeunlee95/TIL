import sys

sys.stdin = open("1_Forth", "r")

T = int(input())
for t in range(1, T+1):

    a = input().split()
    b = ['-', '+', '/', '*']
    stack = [0] * len(a)
    top = -1

    for i in range(len(a)):
        if(len(a)==3 and a[1] in b and a[0] not in b):
            if(a[1]=='+'):
                print(f"#{t} {a[0]}")
                break
            elif (a[1] == '-'):
                print(f"#{t} -{a[0]}")
                break
            else:
                print(f"#{t} error")
                break

        if(a[i] == '.'):
            print(f"#{t} {stack[top]}")
            break
        if(a[i] not in b):
            top += 1
            stack[top] = int(a[i])
        else:
            if(top < 1):
                print(f"#{t} error")
                break
            else:
                num1 = stack[top]
                num2 = stack[top-1]
                stack[top - 1] = 0
                stack[top] = 0
                top -= 1
                if(a[i] == '+'):
                    stack[top] = num2 + num1
                elif (a[i] == '-'):
                    stack[top] = num2 - num1
                elif (a[i] == '/'):
                    stack[top] = num2 // num1
                elif (a[i] == '*'):
                    stack[top] = num2 * num1


