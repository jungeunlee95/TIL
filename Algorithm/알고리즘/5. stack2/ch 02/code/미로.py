import sys
sys.stdin = open('미로.txt','r')

T = int(input())

for t in range(T):
    N = int(input())
    maze = [[1 for x in range(N + 2)]]
    for n in range(N):
        msg = input()
        temp_li = [ int(x) for x in msg] # what is it?
        temp_li.insert(0,1)
        temp_li.append(1)
        maze.append(temp_li)
    maze.append([1 for x in range(N + 2)])
    visited = [[False for x in range(N + 2)] for y in range(N + 2)]

    # point = (i, j)
    start = (0, 0)
    end = (0, 0)

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                visited[i][j] = True
            elif maze[i][j] == 2:
                start = (i, j)
            elif maze[i][j] == 3:
                end = (i, j)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    stack = []
    stack.append(start)
    result = 0

    while stack:
        a, b = stack.pop()
        if a == end[0] and b == end[1]:
            result = 1
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if visited[x][y] == False:
                visited[x][y] = True
                stack.append((x, y))

    print(f"#{t + 1} {result}")