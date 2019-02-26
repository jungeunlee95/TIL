import sys
sys.stdin = open("4_피자굽기", "r")

def BFS(p):
      id, num = 0, 1

      # 화로에 첫 번째 피자 넣기
      q.append( [num, p[id]] )

      # 화로가 빌 때까지,
      while q:
            # 지금 들어있는 피자의 num을 결과로
            result = q[0][0]

            if id < m-1: # 화로에 넣지 않은 피자가 있으면
                  if len(q) < n: # 화로가 널널하면 피자 더 넣기
                        id += 1
                        num += 1
                        q.append([num, p[id]])
                  else:         # 화로가 꽉 찼으면 치즈 녹여
                        q[0][1] = q[0][1]//2
                        if q[0][1] == 0: # 치즈 다 녹은 피자 빼기
                              q.pop(0)
                        else:            # 아직 안녹았으면 피자 돌리기
                              q.append(q.pop(0))
            else: # 화로에 피자를 다 넣었으면, 남은 피자들로
                  q[0][1] = q[0][1]//2
                  if q[0][1] == 0:
                        q.pop(0)
                  else:
                        q.append(q.pop(0))
      return result

T = int(input())
for tc in range(1, T + 1):
      n, m = map(int,input().split())
      p = list(map(int,input().split()))

      q = []
      result = 0

      print(f'#{tc} {BFS(p)}')