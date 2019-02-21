import sys
sys.stdin = open('forth.txt','r')

T = int(input())

for t in range(T):
    susic = input().split()

    stack = []
    operator_cnt = 0
    num_cnt = 0
# try, export => If try make error, operate expert
# and when operate expert code, you can make error conditions

    try:
        for ss in susic:
            if ss == '+':
                operator_cnt += 1
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(str(a+b))
            elif ss == '-':
                operator_cnt += 1
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(str(a-b))
            elif ss == '*':
                operator_cnt += 1
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(str(a*b))
            elif ss == '/':
                operator_cnt += 1
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(str(a//b))
            elif ss == '.':
                if (num_cnt - operator_cnt) == 1:
                    print(f"#{t+1} {stack.pop()}")
                else:
                    print(f"#{t+1} error")
            else:
                num_cnt += 1
                stack.append(ss)
    except:
        print(f"#{t+1} error")