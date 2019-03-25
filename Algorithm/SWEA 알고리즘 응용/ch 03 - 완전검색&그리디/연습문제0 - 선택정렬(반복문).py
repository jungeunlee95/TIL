'''
선택 정렬 함수를 반복문으로 작성
'''
# 1
a = [10, 7, 3, 2, 1, 6, 5, 4, 9, 8]

n = len(a)
for i in range(0, n-1):
    min = i
    for j in range(i+1, n):
        if a[j] < a[min]:
            min = j
    temp = a[min]
    a[min] = a[i]
    a[i] = temp

print(a)

