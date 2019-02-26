import sys
sys.stdin = open("4_피자굽기", "r")

def bfs(c):
      result, idx, num = 0, 0, 1
      q = []
      q.append([c[idx],num])
      while q:
            result = q[0][1]
            if idx < M-1:
                  if len(q) < N:
                        idx += 1
                        num += 1
                        q.append([c[idx],num])
                  else:
                        q[0][0] = q[0][0]//2
                        if q[0][0] == 0:
                              q.pop(0)
                        else:
                              q.append(q.pop(0))
            else:
                  q[0][0] = q[0][0]//2
                  if q[0][0] == 0:
                        q.pop(0)
                  else:
                        q.append(q.pop(0))
      return result

T = int(input())
for test_case in range(1, T + 1):
      N, M = map(int,input().split())
      c = list(map(int,input().split()))

      print(f'#{test_case} {bfs(c)}')