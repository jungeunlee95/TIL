import sys
sys.stdin = open("연습문제1", "r")

# T = int(input())
# for t in range(1, 3):
#     a = input()
#     b = []
#     for i in range(0,len(a),7):
#         b.append(a[i:i+7][::-1])
#     result = [0] * len(b)
#     for i in range(len(b)):
#         for j in range(len(b[i])):
#             if j==0 and b[i][j] == '1':
#                     result[i] += 1
#             elif b[i][j] == '1':
#                 result[i] += 2**j
#     print(result)

T = int(input())
for tc in range(1, 3):
    arr = input()
    t = 0
    for i in range(len(arr)):
        t = t * 2 + int(arr[i])
        if(i+1)%7 == 0:
            print(t, end=' ')
            t = 0