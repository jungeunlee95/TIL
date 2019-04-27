'''
선택 정렬 함수를 재귀적 알고리즘으로 작성
'''
# 1
def SelectionSort(n):
    if n == len(a)-1 :
        return 0
    else:
        min = n
        for i in range(n+1, len(a)):
            if a[i] < a[min]: min = i
        a[min], a[n] = a[n], a[min]
        SelectionSort(n+1)

# 2
def SelectionSort2(n):
    if len(a) == 1 :
        return a
    else:
        min_idx = a.index(min(a))
        return [a.pop(min_idx)] + SelectionSort2(a)

# 3
# def SelectionSort3(n):
#     if n == 0: return
#     min = SelectionSort3(n-1)
#     if a[n] < a[min]:
#         a[min], a[n] = a[n], a[min]
#     else :
#         min = n
#     return min

a = [10, 7, 3, 2, 1, 6, 5, 4, 9, 8]
# SelectionSort(0)
print(SelectionSort2(a))


