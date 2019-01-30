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
# a = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
# def my_abs(a):
#     if a >= 0 :
#         return a
#     else:
#         return -a
#
# def solution(i, j):
#     result = 0
#     result += ( my_abs((a[i-1][j] - a[i][j])) \
#      + my_abs((a[i][j-1] - a[i][j])) \
#      + my_abs((a[i][j+1]-a[i][j])) \
#      + my_abs((a[i+1][j]-a[i][j])) )
#     return result
#
# sum1 = 0
# for i in range(1, 4):
#     for j in range(1, 4):
#         sum1 += solution(i, j)
# print(sum1)

# 3
arr = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]

def calAbs(y,x):
    if y-x>0:return y-x
    else: return x-y

def isWall(x,y):
    if x < 0 or x >= 5 : return True
    if y < 0 or y >= 5 : return True
    return False

dx = [-1,0,1,0]
dy = [0,1,0,-1]

sum1 =0
for x in range(len(arr)):
    for y in range(len(arr[0])):
        for i in range(4):
            testX = x + dx[i]
            testY = y+dy[i]
            if isWall(testX, testY)==False:
                sum1 += calAbs(arr[x][y], arr[testX][testY])

print("sum = %d" % sum1)