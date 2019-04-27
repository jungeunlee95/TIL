# 중간 값 pivot
def sort(left, right):
    if right <= left:
        return

    mid = partition(left, right)
    sort(left, mid - 1)
    sort(mid, right)

def partition(left, right):
    pivot = arr[(left + right) // 2]
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left, right = left + 1, right - 1
    return left


arr = [11, 45, 23, 81, 28, 34, 99, 22, 17, 8]
# arr = [11, 45, 23, 81, 28, 34]
# arr = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
sort(0, len(arr) - 1)
print(arr)