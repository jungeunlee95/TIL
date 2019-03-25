미로의 거리

```python
import sys
sys.stdin = open("미로의거리.txt", "r")

def check(x,y):
    if x < 0 or x > N - 1: return False
    if y < 0 or y > N - 1: return False
    if matrix[x][y] == 1: return False
    return True

def bfs(matrix, start, finish):
    tq = []
    result = 0
    tq.append(start)
    visited[start[0]][start[1]] = 1
    
    while tq:
        q = tq[:]
        tq = []
        while q:
            t = q.pop(0)
            for i in range(4):
                x = t[0] + dx[i]
                y = t[1] + dy[i]
                if check(x,y) and not visited[x][y]:
                    if matrix[x][y] == 3:
                        q = []
                        tq = []
                        return result
                    else:
                        tq.append((x,y))
                        visited[x][y] = 1
        result += 1

    return 0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int,input())) for _ in range(N)]
    start, finish = 0,0
    visited = [[0]*N for _ in range(N)]
    dx, dy = [1,-1,0,0],[0,0,1,-1]

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                start = (i,j)
            elif matrix[i][j] == 3:
                finish = (i,j)
    
    print(f'#{test_case} {bfs(matrix,start,finish)}')
```



Contact

```python
import sys
sys.stdin = open("Contact.txt", "r")

def bfs(start):
    result = 0
    tq = []
    visited = [0]*(max(node)+1)
    tq.append(start)
    visited[start] = 1
    while tq:
        q = tq[:]
        tq = []
        result = max(q)
        while q:
            t = q.pop(0)
            for i in range(len(matrix[t])):
                if matrix[t][i] == 1 and not visited[i]:
                    tq.append(i)
                    visited[i] = 1
    
    return result
 
for test_case in range(1, 2):
    len_, start = map(int,input().split())
    node = list(map(int,input().split()))
    matrix = [[0]*(max(node)+1) for _ in range(max(node)+1)]
 
    for i in range(0,len_,2):
        matrix[node[i]][node[i+1]] = 1
 

    for i in matrix:
        print(i)
    print(f'#{test_case} {bfs(start)}')
```



회전

```python
import sys
sys.stdin = open("회전.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    number = list(map(int,input().split()))
    [number.append(number.pop(0)) for _ in range(M)]
    print(f'#{test_case} {number[0]}')
```



노드의 거리	

```python
import sys
sys.stdin = open("노드의거리.txt", "r")

def bfs(matrix,S,G):
    global V
    visited = [0]*(V+1)
    q = []
    result = 0
    q.append(S)
    visited[S] = 1
    
    while q:
        sq = q[:]
        q = []
        print(sq)
        result += 1
        while sq:
            t = sq.pop(0)
            for i in range(len(matrix[t])):
                if matrix[t][i] == 1 and not visited[i]:
                    if i == G:
                        visited[i] = 1
                        return result
                    else:
                        q.append(i)
                        visited[i] = 1
    return 0


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int,input().split())
    node = [list(map(int,input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    matrix = [[0]*(V+1) for _ in range(V+1)]

    for i in range(len(node)):
        matrix[node[i][0]][node[i][1]] = 1
        matrix[node[i][1]][node[i][0]] = 1
    
    print(f'#{test_case} {bfs(matrix,S,G)}')
```

