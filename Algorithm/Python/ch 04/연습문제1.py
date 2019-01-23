import random

# 1
# def my_abs(a):
#     if a >= 0 :
#         return a
#     else:
#         return -a
#
# # a = [[0]*5 for i in range(5)]
# # for i in range(5):
# #     for j in range(5):
# #         a[i][j] = random.randrange(1,7)
# a = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
#
# sum1 = 0
# for i in range(1,4):
#     for j in range(1,4):
#        sum1 += ( my_abs((a[i-1][j] - a[i][j])) \
#          + my_abs((a[i][j-1] - a[i][j])) \
#          + my_abs((a[i][j+1]-a[i][j])) \
#          + my_abs((a[i+1][j]-a[i][j])) )
# print(sum1)

# 2
a = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
def my_abs(a):
    if a >= 0 :
        return a
    else:
        return -a

def solution(i, j):
    result = 0
    result += ( my_abs((a[i-1][j] - a[i][j])) \
     + my_abs((a[i][j-1] - a[i][j])) \
     + my_abs((a[i][j+1]-a[i][j])) \
     + my_abs((a[i+1][j]-a[i][j])) )
    return result

sum1 = 0
for i in range(1, 4):
    for j in range(1, 4):
        sum1 += solution(i, j)
print(sum1)

