<<<<<<< HEAD
import sys
sys.stdin = open("1_숫자추가", "r")

# Linked List 큐
class Node :
    def __init__(self, item, n=None):
        self.item = item
        self.next = n


def enPQueue(item, cnt=0) :
    global front, rear
    newNode = Node(item)

    if front == None :
        front = newNode
    else :
        f = front
        pre = None
        if cnt != 0 :
            for i in range(cnt):
                pre = f
                f = f.next
            newNode.next = f
            pre.next = newNode
        else:
            while f :
                pre = f
                f = f.next
            if pre == None :
                front = newNode
                newNode.next = f
            elif f == None:
                pre.next = newNode
                rear= newNode
            else:
                pre.next = newNode
                newNode.next = f

def addFront(item, cnt=0) :
    global front, rear
    newNode = Node(item)

    if front == None :
        front = newNode
    else :
        f = front
        pre = None
    newNode.next = f
    front = newNode

def enQueue(item):
    global front, rear
    newNode = Node(item)
    if front == None :
        front = newNode
    else :
        rear.next = newNode
    rear = newNode

def deQueue():
    global front, rear
    if front == None:
        print("Queue_Empty")
        return None

    item = front.item
    front = front.next
    if front == None:
        rear = None
    return item

def printQ10() :
    f = front
    result  = []
    while f:
        result.append(f.item)
        f = f.next
    return result


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    front = None
    rear = None

    for i in range(M):
        data = list(map(int, input().split()))
        for j in data:
            enPQueue(j)

    for i in range(N):
        enPQueue(data[i])

    for i in range(M):
        a, b  = map(int, input().split())
        if a == 0: addFront(b, a)
        else: enPQueue(b, a)

    result = printQ10()

    print(f"#{t} {result[L]}")






=======

"""
5110. [파이썬 S/W 문제해결 기본] 7일차 - 수열 합치기
문제 내용
여러 개의 수열을 정해진 규칙에 따라 합치려고 한다. 다음은 3개의 수열이 주어진 경우의 예이다.
수열 2의 첫 숫자 보다 큰 수자를 수열 1에서 찾아 그 앞에 수열 2를 끼워 넣는다.
합쳐진 수열에 대해, 수열 3의 첫 숫자보다 큰 숫자를 찾아 그 앞에 수열 3을 끼워 넣는다. 큰 숫자가 없는 경우 맨 뒤에 붙인다.
마지막 수열까지 합치고 나면, 맨 뒤의 숫자부터 역순으로 10개를 출력한다.
[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 첫 줄에 수열의 길이 N, 수열의 개수 M, 이후 M개의 줄에 걸쳐 1000이하의 자연수로 구성된 수열이 주어진다. 4<=N<=1000, 1<=M<=1000
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 완성된 수열의 맨 뒤부터 10개의 숫자를 역순으로 출력한다.
최초 작성 2019.02.27 PBY
"""
import sys
sys.stdin = open("input", "r")

class Node :
    def __init__(self, item, n=None):
        self.item = item
        self.next = n

def add(pre, item):
    if pre == None:
        print("ERROR")
    else:
        pre.next = Node(item, pre.next)

def addFront(item, cnt=0) :
    global front
    front = Node(data, front)


def addLast(item):
    global front
    if front == None:
        front = Node(item)
    else:
        pre = front
        while pre.next != None:
            pre = pre.next
        pre.next = Node(item)


def printQ10() :
    f = front
    result  = []
    while f:
        result.append(f.item)
        f = f.next
    return result


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    nums = []

    front = None

    # 첫번째 수열 연결하기
    nums = list(map(int, input().split()))
    for i in range(N):
        addLast(nums[i])

    # 두번째 수열부터는 M-1만큼 돌면서 연결해야함
    for i in range(M-1):
        data = list(map(int, input().split()))
        pre = front
        # 방금 받은 수열의 첫번째 indexq보다 큰 값이 이전 연결리스트에 있는지 찾기
        while pre.next != None:
            if data[0] < pre.next.item:
                break
            pre = pre.next

        if pre == front:
            addFront(data[0])
            pre = front
            for i in data[1:]:
                add(pre, i)
                pre = pre.next
        else:
            for i in data:
                add(pre, i)
                pre = pre.next

    result = printQ10()[::-1][:10]
    print(f"#{t}", end=" ")
    for i in result:
        print(i, end=" ")
    print()


# 2
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    
    for _ in range(M-1): 
        data = list(map(int, input().split()))
        for i in range(N):
            if nums[i] > data[0]:
                nums[i:i] = data
                break
        else: 
            nums += data
    print("#%d %s" %(t+1, ' '.join(list(map(str,nums[::-1][:10])))))











>>>>>>> 8edfc07f9cb4134bc3c0dcb3cd3162adf530a383
