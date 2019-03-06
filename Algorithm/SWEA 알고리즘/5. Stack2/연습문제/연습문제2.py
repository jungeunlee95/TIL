'''
4개의 알파벳 원소를 가진 배열의 모든 부분 집합 구하기
'''
# 1
# a = ['A', 'B', 'C', 'D']
# b = [0, 0, 0, 0]
# def powerset(k, n):
#     if(k == n):
#         result=[]
#         for i in range(n):
#             if(b[i] == 1):
#                 result.append(a[i])
#         print(result)
#     else:
#         b[k] = 0
#         powerset(k + 1, n);
#         b[k] = 1;
#         powerset(k + 1, n);
#
#
# powerset(0, 4)  # index, 원소의 개수

'''
{1,2,3,4,5,6,7,8,9,10}의 powerset중 원소의 합이 10인 부분집합
-백트래킹 사용
'''
# 2
# a = [1,2,3,4,5,6,7,8,9,10]
# b = [0] * len(a)
# def powerset(k, n):
#     if(k == n):
#         result=[]
#         for i in range(n):
#             if(b[i] == 1):
#                 result.append(a[i])
#         # print(result)
#         sum1 = 0
#         for j in range(len(result)):
#             sum1+=result[j]
#         if(sum1 == 10):
#             print(result)
#     else:
#         b[k] = 0
#         powerset(k+1, n);
#         b[k] = 1;
#         powerset(k + 1, n);
#
#
# powerset(0, len(a))  # index, 원소의 개수

# 3
a = [1,2,3,4,5,6,7,8,9,10]
b = [0] * len(a)

def powerset(k, n):
    if(k == n):
        result=[]
        for i in range(n):
            sum2 = 0
            if(b[i] == 1):
                if(sum2>10):
                    continue
                sum2+=a[i]
                result.append(a[i])
        # print(result)
        sum1 = 0
        for j in range(len(result)):
            sum1+=result[j]
        if(sum1 == 10):
            print(result)
    else:
        b[k] = 0
        powerset(k+1, n);
        b[k] = 1;
        powerset(k + 1, n);

powerset(0, len(a))  # index, 원소의 개수
