# 2019-01-09 - function_pratice 2

### 문제1

> 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.  예를들어, N=123이면 1+2+3=6을 return 하면 됩니다.

```python
# 1
def solution(n):
    n = str(n)
    sum1 = 0
    for i in range(0, len(n)):
        sum1 += int(n[i])
    return sum1
print(solution(123))

# 2
def solution2(n):
    return sum([int(i) for i in str(n)])
print(solution(123))

```



------

### 문제2

> 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.  예를 들어, n이 12345이면 [5, 4, 3, 2, 1]을 리턴합니다.

```python
# 1
def solution(n):
    nums = []
    for i in range(0, len(str(n))):
        nums.append(int(str(n)[i]))
    return nums[::-1]
    
print(solution(12345))

# 2
def solution2(n):
    list_a = [int(i) for i in str(n)]
    list_a.reverse()
    return list_a

print(solution2(12345))

# 3
def solution3(n):
    return [int(i) for i in str(n)][::-1]

print(solution3(12345))

# 4
def solution4(n):
    return list(map(int, reversed(str(n))))

print(solution4(12345))
```



------

### 문제3

> 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요.

```python
# 1
def solution(nums):
    nums = list(set(nums))
    nums.remove(min(nums))
    nums.sort()
    return nums
print(solution([4,3,2,1,1]))

# 3
def solution2(nums):
    return list(filter(lambda x: x > min(nums), nums))
print(solution2([5,6,2,4,1]))
```



### filter, lambda

> ## filter
>
> filter란 무엇인가를 걸러낸다는 뜻으로, filter 함수도 동일한 의미를 가진다. filter 함수는 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다. 그리고 두 번째 인수인 반복 가능한 자료형 요소들이 첫 번째 인수인 함수에 입력되었을 때 리턴값이 참인 것만 묶어서(걸러내서) 돌려준다.
>
> ```
> #filter1.py
> def positive(x):
>     return x > 0
> 
> print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
> ```
>
> > 결과값: [1, 2, 6]
>
> 여기서는 두 번째 인수인 리스트의 요소들이 첫 번째 인수인 positive 함수에 입력되었을 때 리턴값이 참인 것만 묶어서 돌려준다. 앞의 예에서는 1, 2, 6만 양수여서 x > 0 이라는 문장이 참이 되므로 [1, 2, 6]이라는 결과값을 리턴하게 된 것이다.
>
> 앞의 함수는 lambda를 이용하면 더욱 간편하게 코드를 작성할 수 있다.
>
> ```
> >>> list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))
> [1, 2, 6]
> ```

> ### lambda 함수
>
> - 익명함수 : 메모리를 아끼고 가독성을 향상시킨다. pythonic
> - 일반적인 함수는 객체를 만들고, 재사용을 위해 함수 이름(메모리)를 할당한다.
>
> ```
> # lambda 인수1, 인수2, ... : 인수를 이용한 표현식
> >>> sum = lambda a, b: a+b
> >>> sum(3,4)
> 7
> ```
>
> ### 왜 쓰는가?
>
> - 익명함수이기 때문에 한번 쓰이고 다음줄로 넘어가면 힙(heap) 메모리 영역에서 증발
> - (참고) 가비지 컬렉터 (참조하는 객체가 없으면 지워버린다)
>   - 파이썬에서는 모든것이 객체로 관리 되고 각 객체들은 레퍼런스 카운터를 갖게 된다. 이 카운터가 0 즉, 그 누구도 참조하지 않게 된다면 메모리를 환원 하게 된다.





------

### 문제4

> 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요

```python
# 1
def solution(num):
    if num % 2 == 0:
        return "Even"
    else :
        return "Odd"
print(solution(2))

# 2
def solution2(num):
    return "Even" if num%2==0 else "Odd"
print(solution2(1))

```



------

### 문제5

> 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 자연수 n을 입력받아 n이 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

> 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.

```python
# 1
def solution(n):
    a = str(n)[0]
    b = str(n)[1]
    if(n % (int(a)+int(b)) == 0):
        return True
    else :
        return False
print(solution(32))

# 2 
def solution2(n):
    return True if (n % (int(str(n)[0]) + int(str(n)[1]))) == 0 else False 
print(solution2(18))

# 3
def solution3(x):
    sum1 = 0
    for i in str(x):
        sum1 += int(i)
    return False if x % sum1 else True
print(solution3(19))

# 4
def solution4(x):
    return x % sum(int(x) for x in str(x) ) == 0
print(solution4(30))


```



---

### 문제6

> OOO 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다. 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

```python
# 1
def solution(p_num):
    return "*** - **** - "+ p_num.split('-')[2]
print(solution("010-1111-2222"))

# 1
def solution2(p_num):
    return "*" * 8 +p_num[-4:]
print(solution2("01011112222"))
```



---

### 문제7

> 문자열이 주어지면, 각 문자(대소문자 구분)를 한번씩 반복하여 문자열을 반환하는 함수를 작성하세요.

> 예시
>
> - double_char("String") ==> "SSttrriinngg"
> - double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"
> - double_char("1234!_ ") ==> "11223344!!__  "

```python
# 1
def double_char(word):
    result = ""
    for i in range(0, len(word)):
        result += word[i]*2
    return result
    
print(double_char("1234!_ "))

# 2
def double_char2(word):
    res = ""
    for s in word:
        res += s * 2
    return res
print(double_char2("Hello World"))

# 3

def double_char3(word):
    return ''.join(s * 2 for s in word)
print(double_char3("string"))
```



---

### 문제8

> 크기를 가지고 1과 0을 번갈아 나타내는 stringy 함수를 작성하고자 합니다. 

> 조건 및 출력예시
>
> - 문자열은 반드시 1부터 시작해야 합니다. 
> - 스트링의 크기는 항상 양수이며 정수만 사용합니다.
> - 스트링의 크기(size)가 6이면 '101010'을 반환합니다.
> - 스트링의 크기(size)가 4이면 '1010'을 반환합니다. 
> - 스트링의 크기(size)가 12이면 '101010101010'을 반환합니다.

```python
# 1  
def stringy(num):
    result = "10" * num
    return result[:num]

print(stringy(12))

# 2
def stringy2(num):
    return '10' * int((num/2)) + '1' * (num%2)
print(stringy2(3))

# 3
def stringy3(num):
    return ''.join([str(i%2) for i in range(1,num +1)])
print(stringy3(6))

```



---

### 문제9

> 당신이 일하는 회사는 지불 시스템을 개발하는 계약을 맺었습니다. 당신의 임무는 금액(실수)을 달러와 센트의 문자열 서식으로 반환하는 함수를 개발하는 일입니다. 0이 누락 경우에 뒤에 0을 추가해야 합니다.

> 예시
>
> - 3 -> $3.00 

```python
# 1
def solution(num):
    return f'${num:0.2f}'
print(solution(3))

# 2
def solution2(num):
    return '${:.2f}'.format(num)
print(solution2(4))
```



---

### 문제10

> 1세기는 1년~100년까지, 2세기는 101년에서 200년까지를 포함합니다. 주어진 연도 값에서, 세기를 반환하는 함수를 작성하세요. 

```python
# 1
def solution(year):
    return str((year-1)//100 +1)+"세기"
print(solution(101))

# 2
def solution2(year):
    return(year + 99) // 100
print(solution2(101),"세기")
```

