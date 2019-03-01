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






