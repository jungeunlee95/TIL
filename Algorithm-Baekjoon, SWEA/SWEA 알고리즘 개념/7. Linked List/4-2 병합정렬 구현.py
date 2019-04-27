'''
오름 차순 병합 정렬 구현
69, 10, 30, 2, 16, 8, 31, 22
'''
a = [69, 10, 30, 2, 16, 8, 31, 22]

def merge_sort(m):
    # 사이즈가 0, 1이면 바로 리턴
    if len(m) <= 1 : return m

    # 들어온 리스트 계속 반으로 자르기
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]
    
    # 리스트의 크기가 1이 될 때까지 merge_sort 로 반씩 잘라!
    left = merge_sort(left)
    right = merge_sort(right)
    
    # 분할된 리스트들을 하나로 병합해서  return 
    return merge(left, right)

def merge(left, right):
    # 병합할 리스트
    result = []

    # 둘 중 하나가 빈 리스트가 될 때까지 계속 채우기
    while len(left) > 0 and len(right) > 0 :
        if left[0] <= right[0] :
            result.append(left.pop(0))
        else :
            result.append(right.pop(0))

    # 만약 하나만 비고 나머지가 남아있으면 그대로 뒤에 붙이기
    if len(left) > 0 :
        result += left
    elif len(right) > 0 :
        result += right

    return result

print(merge_sort(a))