import sys
sys.stdin = open("금속막대", "r")

# 막대의 왼쪽부분이 오른쪽 부분에 없다면, 걔를 1번째 인덱스에 놀거임 

# 1
T = int(input())
for t in range(1,T+1):
    m = int(input())
    a = list(map(int,input().split()))
    b = []
    
    # 정수로 들어온 a를 2차원 배열로 2개씩 묶어서 b로 만듦
    for i in range(0, len(a)-1, 2):
        c = [a[i], a[i + 1]]
        b.append(c)

    c = [[0, 0]] * m  # 막대를 체워나갈 배열
    second_num = []   # 막대의 오른쪽 부분만 따로 배열로 만듦
    for i in range(m):
        second_num.append(b[i][1])

    for i in range(m): # b 배열을 돌면서, 배열의 [i][0]부분들이 second_num에 없다면, 걔가 c에 첫번째로 들어감
        if b[i][0] not in second_num:
            c[0] = b[i]
            del b[i]
            break;
    # print(b)  # [[1, 2], [2, 3], [8, 1], [3, 7], [5, 8]]
    # print(c)  # [[9, 5], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    # 이제 c의 첫번째 인덱스가 정해졌으니까, b배열을 돌면서 [i][0] 값이 c의[i][1]값과 같다면 뒤에 계속 붙여줌 
    for i in range(len(c)):  # 0 1 2 3 4
        for j in range(len(b)):
            if b[j][0] == c[i][1]:
                c[i + 1] = b[j]

    # 출력
    print(f'#{t}', end=" ")
    for i in range(len(c)):
        for j in range(2):
            print(c[i][j], end=" ")
    print()


# 2
TC = int(input())
for tc in range (1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        found = False
        for j in range(N):
            if arr[i * 2] == arr[j * 2 + 1] :
                found = True
                break
        if found == False:
            start_position = i
            break

    arr[0], arr[start_position * 2] = arr[start_position * 2], arr[0]
    arr[1], arr[start_position * 2 + 1] = arr[start_position * 2 + 1], arr[1]

    for i in range(1, N - 1):
        for j in range(i, N):
            if arr[i * 2 - 1] == arr[j * 2]:
                arr[i * 2], arr[j * 2] = arr[j * 2], arr[i * 2]
                arr[i * 2 + 1], arr[j * 2 + 1] = arr[j * 2 + 1], arr[i * 2 + 1]
                break

    print("#%d "%tc, end=' ')
    for i in range(N*2):
        print("%d "%arr[i], end=' ')
    print()




