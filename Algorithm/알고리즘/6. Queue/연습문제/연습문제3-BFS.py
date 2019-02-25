class Node :
    def __init__(self, item, n=None):
        self.item = item
        self.next = n

def enQueue(item):
    global front, rear
    newNode = Node(item)
    if front == None:
        front = newNode
    else:
        rear.next = newNode
    rear = newNode

def isEmpty():
    return front == None

def deQueue():
    global front, rear
    if isEmpty():
        print("EMPTY!!")
        return None

    item = front.item
    front = front.next
    if front == None:
        rear = None
    return item

def Qpeek():
    return front.item

def printQ():
    f = front
    s = ""
    while f:
        s += str(f.item) + " "
        f = f.next
    return s


def BFS(G, v): # G:그래프, v: 탐색 시작점
    enQueue(v)
    while not isEmpty():
        a = deQueue()  # 첫번째 원소 꺼내
        if visited[a-1] == 0:
            visited[a-1] = 1 # visited 체크
            result.append(a)
        for i in range(8):
            if G[a][i] == 1:
                enQueue(i)  # 노드 q에 넣기
        if(0 not in visited): break

a = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
G = [[0]*8 for _ in range(8)]

for i in range(0, len(a)-1, 2):
    G[a[i]][a[i + 1]] += 1
    G[a[i + 1]][a[i]] += 1
# G = [[0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 1, 1, 0, 0, 0, 0],
#      [0, 1, 0, 0, 1, 1, 0, 0],
#      [0, 1, 0, 0, 0, 0, 0, 1],
#      [0, 0, 1, 0, 0, 0, 1, 0],
#      [0, 0, 1, 0, 0, 0, 1, 0],
#      [0, 0, 0, 0, 1, 1, 0, 1],
#      [0, 0, 0, 1, 0, 0, 1, 0]]

visited = [0] * 7   # [0, 0, 0, 0, 0, 0, 0, 0]
front = rear = None
result = []
BFS(G, 1)
print(result)
