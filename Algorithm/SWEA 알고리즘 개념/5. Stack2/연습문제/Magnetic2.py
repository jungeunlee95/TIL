import sys
sys.stdin = open("Magnetic", "r")

for t in range(1,11):
    a = int(input())
    b = []
    for i in range(a):
        c = list(map(int, input().split()))
        b.append(c)

    result = 0
    for i in range(a):
        check = 0
        for j in range(a):
            if(b[j][i] != 0):
                if(b[j][i] == 1):
                    check =1
                elif(b[j][i] == 2):
                    if(check == 1):
                        result+=1
                        check = 0
    print(f"#{t} {result}")

