# 연습문제 2
# 10개의 정수를 입력 받아 부분 집합의 합이 0이 되는 것이 존재하는지 계산하는 함수

# 1 공집합 포함
# arr = [-3,3,-9,6,7,-6,1,5,4,-2]
# n = len(arr)
# cnt = 0
# for i in range(1<<n):
#     result = []
#     for j in range(n):
#         if i & (1<<j):
#             result.append(arr[j])
#     # print(result)
#     if(sum(result)==0):
#         cnt+=1
#             # print(arr[j])
# print(cnt)


# 2 공집합 포함X 
arr = [-3,3,-9,6,7,-6,1,5,4,-2]
sum = cnt = 0

for i in range(1,1<<len(arr)):
    for j in range(len(arr)):
        if i &(1<<j):
            sum += arr[j]

    if sum == 0 :
        cnt +=1
        print("cnt: ", cnt, end=", 배열:  ")
        for j in range(len(arr)):
            if i & (1<<j):
                print(arr[j], end=" ")
        print()
    sum = 0