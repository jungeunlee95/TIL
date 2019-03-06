# 2019-01-09 - function_pratice 1

**얕은 복사, 깊은 복사**

https://wikidocs.net/16038



---

### 문제1

> 다음 리스트의 합계, 평균, 분산을 구하는 함수를 만드세요

> grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5, 62.5]

```python
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5, 62.5]

#합계
def grades_sum(scores):
    sum1 = 0
    for i in scores:
        sum1 += i
    return sum1
print(grades_sum(grades))    

#평균
def grades_avg(grades):
    sum_of_grades = grades_sum(grades)
    return round(sum_of_grades / len(grades),2)
    
print(grades_avg(grades))

#분산
# 1
def grades_var(scores):
    avg = grades_avg(scores)
    var = 0
    for i in scores:
        var += (avg - i) ** 2
    return round(var/len(scores),2)
print(grades_var(grades))

# 2
# def grades_var(scores):
#     avg = grades_avg(scores)
#     var = []
    
#     for i in scores:
#         var.append((avg - i) ** 2)
#     return grades_avg(var)
# print(grades_var(grades))
```



---

### 문제2

> 함수는 다음과 같은 4가지의 경우로 나눠서 생각할 수 있습니다.
>
> - 입력/리턴값이 모두 있는 경우
> - 입력값만 있는 경우
> - 리턴값만 있는 경우
> - 입력/리턴값이 모두 없는 경우

> 위의 4가지 경우의 예시를 각각 작성해보세요.

```python
# 1: •입력/리턴값이 모두 있는 경우
def apple(a):
    return(f'{a}는 사과를 먹습니다.')
print(apple("정은이"))

# 2: •입력값만 있는 경우
def banana(a):
    fruit = a
print("banana호출 : ", banana("바나나"))

# 3: •리턴값만 있는 경우
def cake():
    return "티라미수"
print("cake함수호출 : ",cake())

# 4:•입력/리턴값이 모두 없는 경우
def candy():
    print("candy함수실행")
print("candy함수호출 : " , candy())

# > 출력
# 정은이는 사과를 먹습니다.
# banana호출 :  None
# cake함수호출 :  티라미수
# candy함수실행
# candy함수호출 :  None
```



---

### 문제3

> A 씨는 게시판 프로그램을 작성하고 있습니다. 게시물의 총 건수와 페이지에 보여줄 게시물 수를 입력으로 주었을 때  총 페이지수를 출력하는 프로그램이 필요합니다. A씨를 위한 게시판 페이징을 해주세요.

> 페이징: 게시판 페이지수를 보여주는 것 
>
> - 총 페이지수 = 총 건수 / 한 페이지당 보여줄 건수 + 1

```python
a, b = map(int,input("총 건수, 페이지당 게시글 입력 : ").split())

# 1
def getTotalPages(m, n):
    if m % n == 0:
        return m // n
    else:
        return round(m // n) + 1
    
print(getTotalPages(a,b))
```



---

### 문제4

> 다음 중 가장 높은 점수가 출력되도록 만들어주세요.

> korean, english, mathematics, science = 100, 86, 81, 91

```python
korean, english, mathematics, science = 100, 86, 81, 91

def max_scores(*args):
    return max(args)

print(max_scores(korean, english, mathematics, science))
print(max_scores(english, mathematics, science))
```



---

### 문제5

> 길이가 n이고, "수박수박수박수..."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 

> 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다

```python
def solution(n):
    answer = '수박' * n
    return answer[:n]
print(solution(3))
```



---

### 문제6

> 단어의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

```python
# 1
def middle_word(a):
    if len(a) % 2 == 0:
        i = len(a) // 2
        return a[i-1:i+1]
    else:
        return a[len(a)//2]
    

# 2
def solution(str):
    if len(str) % 2 :
        return str[len(str) // 2]
    else :
        return str[(len(str) // 2) -1 : (len(str) // 2) + 1]
     

# 3
def solution2(str):
    return str[(len(str) -1) // 2 : (len(str) // 2 + 1)]

```



---

### 문제7

> 리스트의 각 요소중 특정 정수로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수 solution을 작성해주세요. 특정 정수로 나누어 떨어지는 요소가 하나도 없다면 리스트에 -1을 담아 반환하면 됩니다.

> Example
>
> - solution([1, 2, 3, 4, 5, 6, 7], 2) ==> [2, 4, 6]
> - [[리스트], 특정 정수]

```python
#여기에 코드를 작성하세요
# 1
def solution(a, b):
    result = []
    for i in a:
        if i % b == 0 :
            result.append(i)
            result.sort()
    if result == [] :
        result.append(-1)
    return result

print(solution([8,1,2,3,4,5,6,7],2))


```



---

### 문제8

> 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요. 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.  (a와 b를 모두 포함해야 합니다)

```python
# 1
def solution(a, b):
    result = 0
    if a > b :
        for i in range(b, a+1):
            result += i
    else :
        for i in range(a, b+1):
            result += i
    return result
print(solution(3, 4))

# 2
def solution2(a, b):
    if a == b :
        return a
    elif a < b :
        return sum(list(range(a, b+1)))
    else:
        return sum(list(range(b, a+1)))
print(solution2(3, 4))


```



---

### 문제9

> 문자열 s의 길이가 4혹은 6이고, 숫자로만 구성되어있는지 확인해주는 함수, solution을 완성하세요.예를들어, s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

> Hint : isdigit() 내장 메서드를 통해 숫자가 들어있는지 여부를 확인할 수 있습니다.

```python
# 1
def solution(s):
    if(len(s)==4 or len(s)==6):
        if(s.isdigit()):
            return "True"
        else:
            return "False"
    else:
        return "False"

# 2
def solution2(s):
    return s.isdigit() and (len(s) == 4 or len(s) == 6) 
```



---

### 문제10

> 자연수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요. 

> 제한 조건: n은 0이상 3000이하인 자연수입니다.

```python
num = int(input("0<= x <= 3000의 자연수를 입력하세요"))

if(num <0 or num > 3000):
    while(num<=0 or num >= 3000):
        num = int(input("0<= x <= 3000사이의 자연수를 입력!!!!"))
    
def solution(num):
    sum1 = 0 
    for i in range(1, num+1):
        if num % i == 0 :
            sum1 += i
        else : 
            continue
    return sum1
print(solution(num))
```


