# 2019-01-10 - function_pratice2

### 문제1

> Arara는 셈을 한쌍으로 하는 아마존에 살고 있는 부족입니다. 이들이 행하는 셈의 방식은 다음과 같습니다.

> 예를 들어, 1에서 8까지는 셈을 한다면,
>
> - 1 = anane 
> - 2 = adak 
> - 3 = adak anane 
> - 4 = adak adak 
> - 5 = adak adak anane 
> - 6 = adak adak adak
> - 7 = adak adak adak anane
> - 8 = adak adak adak adak 

> 주어진 숫자 인수를 통해 다음과 같은 함수를 작성하세요.

> 예시
>
> - count_arara(3) # -> 'adak anane'
> - count_arara(8) # -> 'adak adak adak adak'

```python
# 1
def count_arara(num):
    if(num % 2 == 0 ):
        return "adak " * (num//2)
    else:
        return "adak " * (num//2) + "anane " 

print(count_arara(1))
print(count_arara(8))

# 2
def count_arara2(num):
    return "adak " * (num//2) if (num % 2 == 0 ) else "adak " * (num//2) + "anane " 

print(count_arara2(3))
print(count_arara2(8))

```



---

### 문제 2

> 제 친구 Rora는 그녀가 하고있는 밴드의 이름을 바꾸고 싶어합니다.  그녀는 "The" + 대문자 명사 형태의 밴드 이름을 원합니다. 예를 들어,"dolphin" -> "The Dolphin"와 같습니다.

> 또는 첫글자와 마지막 글자가 같다면 같은 단어(명사)를 반복하여 결합하여 첫번째 문자를 대문자로 시작하는 밴드 이름을  만들고 싶어합니다. (이때는 앞쪽에 'The'가 없음) 예를 들어, "alaska" -> "Alaskaalaska"과 같습니다.

> 명사를 문자열로 하는 함수를 완성하고 선호하는 밴드 이름을 문자열로 표시하세요.

```python
# 1
def solution(name):
    result = ""
    if(name[0] == name[-1]):
        result = (name * 2)
        result= result[0].upper() + result[1:]
        return result
    else : 
        return "The " + name[0].upper() + name[1:]
    
print(solution("alaska"))
print(solution("dolphin"))

# 2
def solution2(name):
    if name[0] != name[-1]:
        return f'The {name[0].upper()}{name[1:]}'
    else:
        return "{}{}".format(name[0].upper, name[1:], name)
print(solution2("alaska"))
print(solution2("dolphin"))

```



---

### 문제3

> 다음 참고 자료를 활용하여 복합세를 계산하는 함수를 만드세요.
>
> - 10달러 이하일 경우, 세율은 10%가 되어야 합니다.
> - 20달러 이하의 경우, 처음 10달러의 세율은 10%이고, 나머지는 7%입니다.
> - 30달러 이하의 경우, 처음 10달러의 세율은 10%이고, 다음 10달러의 세율은 7%이고, 나머지 모든 것의 세율은 5%입니다.
> - 총 30달러를 초과하는 부분에 대해 3%의 세금을 추가하세요. 잘못된 숫자의 입력은 0을 반환하세요. 

> 예시
>
> - 10을 입력하면 1을 반환해야 합니다. (1은 10의 10%)
> - 21을 입력하면 1.75를 반환해야 합니다. (10의 10% + 10의 7% + 1의 5%)

```python
# 1
def solution(a):
    answer = 0
    if a > 30 : 
        answer = 10 * 0.1 + 10* 0.07 + 10*0.05 + (a-30) * 0.03
    elif a >20:
        answer = 10 * 0.1 + 10* 0.07 + (a-20) * 0.05
    elif a > 10:
        answer = 10 * 0.1 + (a-10)* 0.07
    else :
        answer = a*0.1
    return round(answer,2)
    
print(solution(10))
print(solution(21))

# 2
def solution2(total):
    if not isinstance(total, (int, float)) or total < 0: return 0
    
    tax = 0
    if total >30 :
        tax = 2.2 + (total - 30) * 0.03
    elif total > 20:
        tax = 1.7 + (total - 20) * 0.05
    elif total > 10:
        tax = 1 + (total - 10) * 0.07
    elif total > 0 :
        tax = total / 10
    return round(tax,2)

print(solution2(10))
print(solution2(21))
```



---

### 문제4

> 등차수열 만들기
>
> > 입력값 : 시작값(a),증가값(r), 횟수(n)

```python
# 예시
# arithmetic_sequence_sum(2, 3, 5) -> return 40
# 1     2        3          4            5
# a + (a+r) + (a+r+r) + (a+r+r+r) + (a+r+r+r+r) 
# 2 + (2+3) + (2+3+3) + (2+3+3+3) + (2+3+3+3+3) = 40

def solution(a, r, n):
    sum1 = a
    for i in range(1, n):
        sum1 += a+r*i
    return sum1
    
```



---

### 문제5

> 첫 번째 입력 리스트에는 ["a", "a", "b", "d"]처럼 '답'이 들어 있습니다.. 두 번째 입력 리스트는 '해답'이며 사용자의 답이 포함되어 있습니다.  두 개의 리스트는 모두 비어있지 않으며 길이가 같다. 이 답변 배열 리스트에 대한 점수를  반환합니다. 정답의 경우 +4, 오답의 경우 -1, 공백 응답(빈 문자열)의 경우 +0 을 한다. 점수가 0보다 작으면 0을 반환합니다.

> 위와 같은 점수 계산을 하는 함수를 작성하세요.

> 예시
>
> - checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) → 6
> - checkExam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) → 7
> - checkExam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) → 16
> - checkExam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) → 0

```python
# 1
def solution(a, b):
    point=0
    for i in range(len(a)):
        if a[i] == b[i]:
            point += 4
        else :
            if(b[i] != ""):
                point -=1
    if(point<0):
        return 0
    return point
        
# 2
def solution2(a, b):
    point=0
    for i in range(0,4):
        if a[i] == b[i]:
            point += 4
        elif a[i] == "" or b[i] == "":
            point += 0
        else:
            point -= 1
    return point if point >= 0 else 0
```

