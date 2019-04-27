'''
6자리 숫자에 대해서 baby-gin을 검사
<입력>
124783
667767
054060
101123
'''
# 1 배열이용

# 숫자
# num = 667767
# c = [0] * 12
#
# for i in range(6):
#     c[num%10] += 1
#     num //= 10

#문자열
num = '124783'
c = [0] * 12

for i in range(6):
    c[int(num[i])] += 1

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3:
        c[i] -= 3
        tri += 1
        continue
    if c[i]>=1 and c[i+1]>=1 and c[i+2] >= 1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2: print("Baby-gin이 맞습니다")
else: print("Baby-gin이 아닙니다")



# 2 순열
# def permutation(n, k):
#     global baby
#     if k == n:
#         print(a)
#     else:
#         for i in range(k, n-1):
#             a[k], a[i] = a[i], a[k]
#             permutation(n, k+1)
#             a[k], a[i] = a[i], a[k]
#
#             if a[0]==a[1] and a[0]==a[2] and a[3]==a[4] and a[3]==a[5]:
#                 baby += 1
#             if a[0]==a[1] and a[0]==a[2] and a[5] - a[4] == 1 and a[4] - a[3] == 1:
#                 baby += 1
#             if a[2] - a[1] == 1 and a[1] - a[0] == 1 and a[3] == a[4] and a[3] == a[5]:
#                 baby += 1
#             if a[2] - a[1] == 1 and a[1] - a[0] == 1 and a[5] - a[4] == 1 and a[4] - a[3] == 1:
#                 baby += 1
# baby = 0
# a = [1,2,4,7,8,3]
# permutation(len(a), 0)
#
# if baby > 0 :
#     print("Baby-gin이 맞습니다")
# else:
#     print("Baby-gin이 아닙니다")



# 3 완전검색이용
# a = '101123'
# baby = 0
# for i1 in range(6):
#     for i2 in range(6):
#         if i2 != i1 :
#             for i3 in range(6):
#                 if i3 != i1 and i3 != i2:
#                     for i4 in range(6):
#                         if i4 != i3 and i4 != i2 and i4 != i1:
#                             for i5 in range(6):
#                                 if i5 != i4 and i5 != i3 and i5 != i2 and i5 != i1:
#                                     for i6 in range(6):
#                                         if i6 != i5 and i6 != i4 and i6 != i3 and i6 != i2 and i6 != i1:
#                                             a = [int(a[i1]),int(a[i2]),int(a[i3]),int(a[i4]),int(a[i5]),int(a[i6])]
#                                             if a[0]==a[1] and a[0]==a[2] and a[3]==a[4] and a[3]==a[5]:
#                                                 baby += 1
#                                             if a[0]==a[1] and a[0]==a[2] and a[5] - a[4] == 1 and a[4] - a[3] == 1:
#                                                 baby += 1
#                                             if a[2] - a[1] == 1 and a[1] - a[0] == 1 and a[3] == a[4] and a[3] == a[5]:
#                                                 baby += 1
#                                             if a[2] - a[1] == 1 and a[1] - a[0] == 1 and a[5] - a[4] == 1 and a[4] - a[3] == 1:
#                                                 baby += 1
#
# if baby > 0: print("Baby-gin이 맞습니다")
# else: print("Baby-gin이 아닙니다")



# 4 itertools.permutations() 함수 사용
# import itertools
# a = [1,0,3,4,4,4]
# b = list(map(list,itertools.permutations(a)))
# baby = 0
# for i in b:
#     if a[0]==a[1] and a[0]==a[2] and a[3]==a[4] and a[3]==a[5]:
#         baby += 1
#     if a[0]==a[1] and a[0]==a[2] and a[5] - a[4] == 1 and a[4] - a[3] == 1:
#         baby += 1
#     if a[2] - a[1] == 1 and a[1] - a[0] == 1 and a[3] == a[4] and a[3] == a[5]:
#         baby += 1
#     if a[2] - a[1] == 1 and a[1] - a[0] == 1 and a[5] - a[4] == 1 and a[4] - a[3] == 1:
#         baby += 1
# if baby > 0: print("Baby-gin이 맞습니다")
# else: print("Baby-gin이 아닙니다")








