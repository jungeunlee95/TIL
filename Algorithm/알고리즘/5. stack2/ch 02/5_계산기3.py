import sys
sys.stdin = open("5_계산기3", "r")

for t in range(1, 11):
    N = int(input())
    a = input()
    stack = [0] * 1000000
    sic = ['*', '+']
    top = -1
    result = ""

    for i in range(N):
        if( a[i] in sic ):
            if(stack[0]==0):
                top +=1
                stack[top] = a[i]
        elif(a[i] == '('):
            top+=1
            stack[top] = a[i]
        elif(a[i] == ')'):
            while( str(stack[top]) != '('):
                result += str(stack[top])
                stack[top] = 0
                top -= 1
            stack[top] = 0
            top -= 1
        elif( a[i] == '*'):
            if(stack[top] == '*'):
                result += str(stack[top])
                stack[top] = a[i]
            else:
                top += 1
                stack[top] = a[i]
        elif(a[i] == '+'):
            if(stack[top] == '('):
                top += 1
                stack[top] = a[i]
            else:
                result += str(stack[top])
                stack[top] = a[i]
        else:
            result += a[i]
        while top != -1:
            result += str(stack[top])
            stack[top] = 0
            top -= 1
    print(result)
    for i in range(len(result)):
        if result[i] == '+':
            a = stack[top]
            stack[top] = 0
            top -= 1
            b = stack[top]
            stack[top] = 0
            top -= 1
            stack
