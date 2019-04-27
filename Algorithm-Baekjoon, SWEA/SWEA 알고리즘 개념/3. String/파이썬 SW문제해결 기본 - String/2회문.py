'''
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. 
NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다. 

예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.
 
[입력] 
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
import sys
sys.stdin= open("2회문","r")

# 1
# def isPalindrome(a):
#     # if(a == a[::-1]):
#     #     return True
#     # else:
#     #     return False
#     len_a = len(a)
#     for i in range(len_a // 2):
#         if a[i] != a[len_a - (i + 1)]:
#             return False
#     return True
#
# T = int(input())
# for t in range(1, T+1):
#     a, b = map(int, input().split()) # 20 13
#     c = a-b+1
#     result = [[] for _ in range(a)]  # [[], [], [], [], [], [], [], [], []]
#     answer=''
#     # 2차원 배열 만들기
#     for i in range(a):
#         word = input()
#         for j in range(a):
#             result[i].append(word[j])
#
#     # 가로, 세로 회전문 조회
#     for i in range(a):
#         for j in range(c):
#             wid = ''
#             hei = ''
#             for k in range(j, j+b):
#                 wid += result[i][k]
#                 hei += result[k][i]
#             if(isPalindrome(wid) == True):
#                 print(f"#{t} {wid}")
#             if(isPalindrome(hei) == True):
#                 print(f"#{t} {hei}")


# 2
def isPalindrome(a):
    len_a = len(a)
    for i in range(len_a // 2):
        if a[i] != a[len_a - (i + 1)]:
            return False
    return True

def getSentence(a, b, result):
    c = a - b + 1 # ex) a=20, b=13이면 20까지 13글자를 조회해야함. 마지막 index 는 [i][7]~[i][19]까지니까 c= 20-13+1=8

    # 가로, 세로 회전문 조회
    for i in range(a):      # 세로 길f이
        for j in range(c):  # 최대 j(13글자 조회니까 7까지만 가야함)
            wid = ''
            hei = ''
            for k in range(j, j+b):
                wid += result[i][k]   # 0: i,0 ~ i,12,  1: 0,1 ~ 0, 13,  2: 0,2 ~ 0, 14 ..., 7: 0,7 ~ 0,19
                hei += result[k][i]   # 0: 0,0 ~ 12,0,  1: 1,0 ~ 13,0 , .... ,  7 : 7,0 ~ 19,0
            if(isPalindrome(wid) == True):
                return wid
            if(isPalindrome(hei) == True):
                return hei

T = int(input())
for t in range(1, T+1):
    a, b = map(int, input().split())
    result = [[] for _ in range(a)]

    # 글자를 2차원 배열로 만들기
    for i in range(a):
        word = input()
        for j in range(a):
            result[i].append(word[j])
    print(result)
    answer = getSentence(a, b, result)

    print(f"#{t} {answer}")



