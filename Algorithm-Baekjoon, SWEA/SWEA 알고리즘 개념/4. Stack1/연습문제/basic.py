# 아주 기본 구조
stack = [0] * 10
top = -1

for i in range(3):
    stack[top + 1] = i
    top += 1
print(stack)

for i in range(3):
    t = stack[top]
    top -= 1
    print(t)