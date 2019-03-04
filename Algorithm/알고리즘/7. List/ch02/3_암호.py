"""
A사는 창립기념일 이벤트로 비밀번호 맞추기 대회를 열어, 최대 10개인 비밀번호를 맞추는 사람에게 기념품을 제공하기로 했다.
기념품을 받을 수 있도록 다음 조건에 맞는 비밀번호 찾기 프로그램을 작성하시오.
- 1000이하의 숫자 N개가 주어진다. 이때 시작 숫자가 정해지고, 첫 번째 지정 위치가 된다.
- 지정 위치부터 M번째 칸을 추가한다. 여기에 앞칸의 숫자와 뒤로 밀려난 칸의 숫자를 더해 넣는다. 추가된 칸이 새로운 지정 위치가 된다. 밀려난 칸이 없으면 시작 숫자와 더한다.
- 이 작업을 K회 반복하는데, M칸 전에 마지막 숫자에 이르면 남은 칸수는 시작 숫자부터 이어간다.
- 마지막 숫자부터 역순으로 숫자를 출력하면 비밀번호가 된다. 숫자가 10개 이상인 경우 10개까지만 출력한다.
다음은 N, M, K가 6, 3, 3이고, 주어진 숫자가 6, 2, 4, 9, 1, 5인 경우의 예이다. 6이 시작 숫자이자 첫번째 지정 위치가 된다.
(1) 3번째에 새로운 칸을 추가하고, 앞의 숫자 4와 뒤로 밀려난 9를 더해 칸을 채운다.
(2) 다시 3칸 뒤에 새로운 칸을 추가하고, 앞 뒤 숫자를 더해 넣는다.
(3) 다시 3칸 뒤에 칸을 추가하고 앞 뒤 숫자를 더해 넣는다.
암호는 역순인 5 6 1 9 13 4 2 8 6이 된다.
[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 첫 줄에 N, M, K가, 다음 줄에 1000이하의 자연수 N개가 주어진다. 3<=N, M, K<=1000
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
최초 작성 2019.02.27 PBY
"""

import sys
sys.stdin = open("input","r")

T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    nums = list(map(int, input().split()))

    a = 0
    for i in range(K):
        a += M
        if a > len(nums): a -= len(nums)
        if a == 0 : nums.insert(0, nums[1] + nums[len(nums)-1])
        elif a == len(nums): nums.insert(len(nums), nums[0]+ nums[len(nums)-1])
        else: nums.insert(a, nums[a-1]+nums[a])

    nums = nums[::-1]
    print("#{} {}".format(t, ' '.join(list(map(str, nums[:10])))))



# class Node:
#     def __init__(self, data, link):
#         self.data=data
#         self.link=link
# # 첫 노드 생성
# def addtoFirst(data):
#     global Head
#     Head = Node(data,None)
#     return Head
# # 추가
# def add(pre,data):
#     if pre== None:
#         print('error')
#     else:
#         pre.link=Node(data,pre.link)
#     return pre.link
# # 삽입
# def insert(head,m,n):
#     global Head
#     node=head
#     i=0
#     # 첫 번째 노드 뒤에 추가하게 될 때
#     if m==0:
#         nextNode=Head.link
#         Head.link=Node(nextNode.data+Head.data,Head.link)
#         return m
#     # 해당 위치까지 탐색 후 추가
#     while node:
#         if i==m:
#             nextNode=node.link
#             # 중간에 삽입할 때
#             if nextNode:
#                 node.link=Node(node.data+nextNode.data,node.link)
#             # 맨 끝에 삽입할 때
#             else:
#                 node.link=Node(node.data+Head.data,node.link)
#         i+=1
#         node=node.link
#     return m
#
# def printAll(head,num):
#     node=head
#     i=0
#     result=[]
#     while node:
#         result.append(str(node.data))
#         i+=1
#         node=node.link
#     print(f'#{num} {" ".join(result[::-1][:10])}')
#
# TC=int(input())
# for num in range(1,TC+1):
#     n,m,k = map(int,input().split())
#     line = list(map(int,input().split()))
#     addtoFirst(line[0])
#     preNode=Head
#     # linkedlist 생성
#     for i in line[1:]:
#         preNode=add(preNode,i)
#     target=m-1 # 삽입하려는 인덱스의 이전 인덱스를 가리킴
#     for i in range(1,k+1):
#         target=insert(Head,target,n)
#         target+=m # m칸 만큼 이동
#         n+=1 # 숫자 추가로 길이 +1
#         # 만약 가리키는 인덱스가 길이를 넘어서면 mod 연산
#         if target>=n:
#             target%=n
#     printAll(Head,num)
