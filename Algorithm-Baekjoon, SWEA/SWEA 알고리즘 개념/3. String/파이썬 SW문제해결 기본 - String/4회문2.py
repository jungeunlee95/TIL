'''
"기러기" 또는 "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
주어진 100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제이다.

위와 같은 글자 판이 주어졌을 때, 길이가 가장 긴 회문은 붉은색 테두리로 표시된 7칸짜리 회문이다.
예시의 경우 설명을 위해 글자판의 크기가 100 x 100이 아닌 8 x 8으로 주어졌음에 주의한다.


[제약사항]
각 칸의 들어가는 글자는 c언어 char type으로 주어지며 'A', 'B', 'C' 중 하나이다.
글자 판은 무조건 정사각형으로 주어진다.
ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.
가로, 세로 각각에 대해서 직선으로만 판단한다.
즉, 아래 예에서 노란색 경로를 따라가면 길이 7짜리 회문이 되지만 직선이 아니기 때문에 인정되지 않는다.

[입력]
각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.
총 10개의 테스트케이스가 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 길이를 출력한다.
'''
# 10 X 10
import sys
sys.stdin = open("4회문2","r")
# 1
# def longest_palindrom(s):
#     # 비교할 문자열의 길이를 지정 : 문자열의 제일 긴 길이부터 0까지 -1씩 줄여나감
#     for i in range(len(s), 0, -1):
#         # 짧아진 길이 만큼 앞뒤로 이동시키며 비교 : 줄인 길이 만큼 문자열의 시작점을 이동시키며 비교해야 한다.
#         # 때문에 +1을 해준다.
#         for j in range(len(s) - i + 1):
#             # j는 부분 문자열의 시작 index, i는 부분 문자열의 길이
#             if(s[j:j+i] == my_reverse(s[j:j+i])):
#                 return i
# def my_max(arr):
#     max1 = 0
#     for i in range(len(arr)):
#         if arr[i] > max1:
#             max1=arr[i]
#     return max1
#
# def my_reverse(s):
#     result = ""
#     for i in range(len(s)-1, -1, -1):
#         result += s[i]
#     return result
#
# for tc in range(10):
#     tc = input()
#     result = []
#     answer = []
#     for num in range(100):
#         result += [input()]
#
#     # 가로 회문찾기
#     for i in range(100):
#         a = longest_palindrom(result[i])
#         answer.append(a)
#
#     # 세로 회문 찾기
#     c = []
#     for i in range(100):
#         b = ''
#         for j in range(100):
#             b += result[j][i]
#         c.append(b)
#     for i in range(100):
#         a = longest_palindrom(c[i])
#         answer.append(a)
#
#     print(f"#{tc} {my_max(answer)}")



# 2
def longest_palindrom(s):
    for i in range(len(s), 0, -1):
        for j in range(len(s) - i + 1):
            if(s[j:j+i] == s[j:j+i][::-1]):
                return i

for tc in range(10):
    tc = input()
    result = []
    answer = 0

    for _ in range(100):
        result.append(input())

    # 가로 회문찾기
    for i in range(100):
        a = longest_palindrom(result[i])
        if a > answer: answer = a

    # 세로 회문 찾기
    for i in range(100):
        b = ''
        for j in range(100):
            b += result[j][i]
        a = longest_palindrom(b)
        if a > answer: answer = a

    print(f"#{tc} {answer}")


# 3
# for tc in range(1, 11):
#     tn = input()
#     pan = []
#     for num in range(100):
#         pan += [input()]
#
#     # 전치해서 붙여서 가로만 찾자.
#     pan2 = ['' for _ in range(100)]
#     for row in range(100):
#         for col in range(100):
#             pan2[row] += pan[col][row]
#     pan += pan2
#
#     # 제일 긴 거부터 찾아서 break로 나오자.
#     maxv = 0
#     for length in range(100, 0, -1):
#         for row in range(len(pan)):
#             for startpoint in range(0, 100 - length + 1):
#                 for check in range(length):
#                     if pan[row][startpoint + check] != pan[row][-100 + length - 1 + startpoint - check]:
#                         break
#                 #  for문을 다 돌았으면
#                 if check == length - 1:
#                     maxv = length
#             if maxv > 0: break
#         if maxv > 0: break
#
#     print("#%d %d" % (tc, maxv))

# 4
# def isPalinH(x, y, N):
#     for i in range(N // 2):
#         if mat[x][y + i] != mat[x][y + (N - 1) - i]:
#             return False
#     return True
#
#
# def isPalinV(x, y, N):
#     for i in range(N // 2):
#         if mat[x + i][y] != mat[x + (N - 1) - i][y]:
#             return False
#     return True
#
#
# def manachers(S):
#     A = [0] * 202
#     r = p = 0
#     for i in range(len(S)):
#         if i <= r:
#             A[i] = min(A[2 * p - i], r - i)
#         else:
#             A[i] = 0
#
#         while i - A[i] - 1 >= 0 and i + A[i] + 1 < 201 and S[i - A[i] - 1] == S[i + A[i] + 1]:
#             A[i] += 1
#
#         if r < i + A[i]:
#             r = i + A[i]
#             p = i
#     return max(A)
#
#
# for _ in range(10):
#     tc = input()
#     mat = [0] * 100
#     for i in range(100):
#         mat[i] = list(input())
#
#     ans = 1
#     for i in range(100):
#         temp = '#' + '#'.join(mat[i]) + '#'
#         t = manachers(temp)
#         if ans < t: ans = t
#
#     for i in range(100):
#         for j in range(100):
#             if i > j:
#                 mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
#
#     for i in range(100):
#         temp = '#' + '#'.join(mat[i]) + '#'
#         t = manachers(temp)
#         if ans < t: ans = t
#
#     print("#" + tc, ans)