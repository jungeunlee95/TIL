import sys
sys.stdin = open("5_계산기3","r")
#
# testcases = 10
#
# for tc in range(testcases):
#     N = input()
#     inp = input()
#     stack = [0] * 10000
#     top = -1
#     post = ''
#     for i in range(len(inp)):
#         if inp[i] in '*/+-' and stack[0] == 0:
#             top += 1
#             stack[top] = inp[i]
#         elif inp[i] == '(':
#             top += 1
#             stack[top] = inp[i]
#         elif inp[i] == ')':
#             while stack[top] != '(':
#                 post += stack[top]
#                 stack[top] = 0
#                 top -= 1
#             stack[top] = 0
#             top -= 1
#         elif inp[i] == '*' or inp[i] == '/':
#             if stack[top] == '/' or stack[top] == '*':
#                 post += stack[top]
#                 stack[top] = inp[i]
#             else:
#                 top += 1
#                 stack[top] = inp[i]
#         elif inp[i] == '+' or inp[i] == '-':
#             if stack[top] == '(':
#                 top += 1
#                 stack[top] = inp[i]
#             else:
#                 post += stack[top]
#                 stack[top] = inp[i]
#         else:
#             post += inp[i]
#     while top != -1:
#         post += stack[top]
#         stack[top] = 0
#         top -= 1
#     print(post)
#     for i in range(len(post)):
#         if post[i] == '+':
#             stack[top - 1] = stack[top - 1] + stack[top]
#             top -= 1
#         elif post[i] == '-':
#             stack[top - 1] = stack[top - 1] - stack[top]
#             top -= 1
#         elif post[i] == '*':
#             stack[top - 1] = stack[top - 1] * stack[top]
#             top -= 1
#         elif post[i] == '/':
#             stack[top - 1] = int(stack[top - 1] / stack[top])
#             top -= 1
#         else:
#             top += 1
#             stack[top] = int(post[i])
#     print(f'#{tc + 1} {stack[0]}')



# 2
for tc in range(10):
    # input
    N = input()
    equation = input()

    # 1. 스택을 이용해서 후위 표기법으로 변경
    stack = [''] * int(N)
    post = ''
    top = -1

    # 우선순위 정리
    inner_priority = {'(': 0, '+': 1, '*': 2}
    outer_priority = {'(': 3, '+': 1, '*': 2}

    # 식의 각 토큰을 하나씩 확인하면서 스택에 넣는다.
    for token in equation:

        # 피연산자의 경우 후위 표기법으로 출력
        if token.isdigit():
            post += token

        # 연산자의 경우 스택에 쌓음
        else:
            # 닫는 괄호를 만나면 여는 괄호까지 스택에서 꺼내 후위표기법으로 이동
            if token == ")":
                while stack[top] != '(':
                    post += stack[top]
                    top -= 1
                top -= 1  # 마지막에 '(' 한 번 더 빼줌

            # 괄호 외 연산자들
            else:
                # 스택 내에 우선순위를 비교할 대상이 없는 경우, 본인이 앉음
                if top == -1:
                    top += 1
                    stack[top] = token
                    continue

                # 스택 내의 연산자와 현재 들어갈 토큰의 우선순위를 비교
                if inner_priority[stack[top]] < outer_priority[token]:
                    # 딱 눌러앉음
                    top += 1
                    stack[top] = token

                # 우선 순위가 높지 않은 경우
                else:
                    # 내가 앉을 수 있을 때까지 계속 비켜달라고 함
                    while inner_priority[stack[top]] >= outer_priority[token]:
                        post += stack[top]  # 후위표기법으로 계속 보내줌
                        top -= 1
                        # 더 이상 비켜달라고 할 대상이 없으면
                        if top == -1:
                            break  # while 문 탈출
                    # 내가 앉을 수 있게 되면 그때 스택에 토큰이 들어감
                    top += 1
                    stack[top] = token

    # 스택에 남은 것을 모두 후위 표기식으로 이동
    for res in range(top, -1, -1):
        post += stack[res]

    # 2. 스택을 이용해서 후위 표기법을 계산
    # 스택 초기화
    stack = [0] * len(post)
    top = -1

    # 저장한 후위 표기법을 돌면서 연산
    for token in post:

        # 피연산자의 경우 스택에 넣음
        if token.isdigit():
            top += 1
            stack[top] = int(token)

        # 연산자의 경우 스택을 이용해서 연산 (개수가 에러나는 경우는 없음)
        else:
            if token == "*":
                stack[top - 1] = stack[top - 1] * stack[top]
                top -= 1
            else:
                stack[top - 1] = stack[top - 1] + stack[top]
                top -= 1

    # output
    print("#{} {}".format(tc + 1, stack[0]))