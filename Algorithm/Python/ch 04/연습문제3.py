a = [
    [9, 20, 2, 18, 11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 4, 16, 5, 6],
    [12, 13, 22, 23, 14]
]

# def selection_sort(a):
#     for i in range(len(a)-1):
#         min1 = i
#         for j in range(i+1, len(a)):
#             if a[min1] > a[j]:
#                 min1 = j
#         if min1 != i :
#             a[i], a[min1] = a[min1], a[i]
#     return a
#
# for i in a :
#     result = selection_sort(i)
#     print(result)

def selection_sort(a):
    for i in range(5):
        for j in range(5):
            print(a[i][j])
    # for i in range(len(a)-1):
    #     min1 = i
    #     for j in range(i+1, len(a)):
    #         if a[min1] > a[j]:
    #             min1 = j
    #     if min1 != i :
    #         a[i], a[min1] = a[min1], a[i]
    # return a

result = selection_sort(a)
# print(result)

