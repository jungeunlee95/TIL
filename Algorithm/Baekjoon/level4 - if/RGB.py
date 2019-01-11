"""
문제1


색이 칠해진 삼각형은 각각 빨강, 녹색 또는 파랑 색의 행에서 만들어집니다. 
마지막 행보다 하나 적은 색을 각각 포함하는 연속 행은 이전 행에서 두 개의 색을 
고려하여 생성됩니다. 이 색상이 동일하면 동일한 색상이 새 행에 사용됩니다. 
색상이 다른 경우 누락 된 색상이 새 행에 사용됩니다. 
단 하나의 색상으로 최종 행이 생성 될 때까지 계속됩니다

''''
Colour here:        G G        B G        R G        B R
Becomes colour:    G           R           B            G
   
처리 과정 
R R G B R G B B
 R B R G B R B 
  G G B R G G
   G R G B G
    B B R R
     B G R
      R B
       G
'''

입출력 결과:
•print(triangle('RRR')) => R
•print(triangle('RG')) => B 
•print(triangle('RRRGGGBBBBBB')) => G
•print(triangle('RRGBRGBB')) => G


"""
# 1
# def triangle(r):
#     dict = {
#         'GG':'G','BB':'B','RR':'R','GB':'R','GR':'B',
#         'BR':'G','BG':'R','RB':'G','RB':'G','RG':'B'
#     }
#     if len(r) > 2 :
#         s = ''
#         for i in range(len(r)-1):
#             s = s + dict[r[i:i+2]]
#         r = s
#         return triangle(r)
#     elif len(r) > 1:
#         return dict[r]
#     else :
#         return r

# 2
color_set = set("RGB")
def triangle(r):
    while len(r)>1:                                     # 만약 RRG 이면,    RRG, RG 비교
        r = ''.join(a if a==b else(color_set - {a, b}).pop() for a, b in zip(r,r[1:]))
    return r




print(triangle('RRR')) 
print(triangle('RG')) 
print(triangle('RRRGGGBBBBBB')) 
print(triangle('RRGBRGBB')) 