'''
알고리즘 교수님은 학생들에게 병합 정렬을 이용해 오름차순으로 정렬하는 과제를 내려고 한다.
정렬 된 결과만으로는 실제로 병합 정렬을 적용했는지 알 수 없기 때문에 다음과 같은 제약을 주었다.
N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할 한다.
병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.
정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력한다.
알고리즘 교수님의 조건에 따라 병합 정렬을 수행하는 프로그램을 만드시오.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 정수의 개수 N이 주어지고, 다음 줄에 N개의 정수 ai가 주어진다.
5<=N<=1,000,000, 0 <= ai <= 1,000,000

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 오른쪽 원소가 먼저 복사되는 경우의 수, N//2번 원소를 출력한다.
'''
import sys
sys.stdin = open("5204_input", "r")


def merge_sort(m):
    # 사이즈가 0, 1이면 바로 리턴
    if len(m) <= 1:
        return m

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
    global cnt
    # 병합할 리스트
    result = []

    # 둘 중 하나가 빈 리스트가 될 때까지 계속 채우기
    if left[len(left)-1] > right[len(right)-1]:
        cnt += 1

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # 만약 하나만 비고 나머지가 남아있으면 그대로 뒤에 붙이기
    if len(left) > 0:
        result += left
    elif len(right) > 0:
        result += right

    return result

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)
    print("#{} {} {}".format(t, arr[n//2], cnt))
