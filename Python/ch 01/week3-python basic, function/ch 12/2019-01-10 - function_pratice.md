# 2019-01-10

# 문자열 덧셈 하기 - 문자열 조작 및 반복/조건문 활용

**문제 풀기 전에 어떻게 풀어야할지 생각부터 해봅시다!**

> 사람은 덧셈을 할때 뒤에서부터 계산하고, 받아올림을 합니다.
>
> 문자열 2개를 받아 덧셈을 하여 숫자를 반환하는 함수 `my_sum(num1, num2)`을 만들어보세요.

**절대로 return int(num1)+int(num2) 이렇게 풀지 맙시다!!**

**재귀함수도 사용할 필요 없습니다.**

```python
def my_sum(num1, num2):
    len_num1 = len(num1)
    len_num2 = len(num2)
    
    # 자릿수 먼저 고려
    if len_num1 > len_num2: # 12345, 00078
        num2 = (len_num1 - len_num2) * '0' + num2
    else:
        num1 = (len_num2 - len_num1) * '0' + num1
    
    # 숫자 뒤집기 54321, 87000
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    result = 0
    carry = 0
    
    for i in range(len(num1)): 
        carry, r = divmod((int(num1[i])+ int(num2[i]) + carry), 10)  
        # divmod(a,b) -> a를 b로 나눈 carry = 몫, r=나머지
        result += r * (10 ** i)
    else:
        result += carry * 10 ** (i+1)
    return result
    
    
print(my_sum('3', '5')) # --> 8
print(my_sum('123', '77')) # --> 200
print(my_sum('1', '9999')) # --> 10000
    
    
    
```



---

---

---

### 문제1

> 모든 인수의 합계를 반환하는 함수를 만드세요. 입력 값은 함수에 대한 매개 변수로 인덱스와 함께 점차 증가합니다. (첫번째 인덱스는 1부터 시작합니다)

```python
# 1
def add(*args):
    sum1 = 0
    for i in range(1, len(args)+1):
        sum1 += args[i-1]*i
    return sum1

# 2
def add2(*args):
    result = 0
    for idx, num in enumerate(args, 1):
        result += idx * num 
    return result

```



---

### 문제2

> 양을 세는 함수를 만들어 보세요. 예를 들어, 3이라는 숫자가 주어지면 "1 sheep...2 sheep...3 sheep..."이라는 문자열을 리턴하면 됩니다.

> 항상 '양의 정수' 만을 인수로 받습니다.

```python
# 1
def count_sheep(n):
    result = ""
    for i in range(1, n+1):
        result += "{}sheep...".format(i)
        # result += str(i) + "sheep..."
    return result
print(count_sheep(5))

```



---

### 문제3

> 문자열 목록을 필터링하고 친구 이름만 있는 목록을 반환하는 프로그램을 만드세요. 당신의 친구들의 이름은 모두 4개의 글자로 되어 있습니다.

> 예시
>
> - Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

```python
# 1
def friends(name):
    result = []
    for i in name:
        if len(i) == 4:
            result.append(i)
    return result

# 2
def friends2(name):
    for i in range(len(name)-1, 0, -1):
        if len(name[i]) != 4:
            name.remove(name[i])
    return name

```



---

### 문제4

> 자릿수가 주어지면 5미만의 숫자를 '0'으로 바꾸고, 5 이상의 숫자는 '1로'바꿔서 문자열로 반환하는 함수를 작성하세요. (단, 함수를 호출할 때 인자는 str 자료형이어야 합니다)

```python
# 1
def solution(num):
    str1 = ""
    for i in num:
        if(int(i)<5):
            str1 += "0"
        else:
            str1+="1"
    return str1
print(solution("12378"))

# 2
def solution2(num):
    str1 = ""
    for i in num:
        str1 += "0" if int(i) < 5 else "1"
    return str1    
print(solution2("12378"))
```



---

### 문제5

> 휴식을 위해 휴가를 가기로 결정했습니다. 휴가지에서 편히 돌아다니기 위해 렌터카를 빌려야 합니다. 렌터카 회사의 직원이 당신에게 보내준 가격 책정 방법은 다음과 같습니다.

> 매일 40달러의 비용이 청구됩니다. 7일 이상 차를 빌리면, 50달러가 할인됩니다. 또한, 3일 이상 차를 렌트하면 20달러가 할인됩니다. 총 금액을 '당신의 렌터카 비용은 00$입니다' 라는 메세지를 반환하는 함수를 만드세요.

```python
# 1
def solution(d):
    cost = 0
    if d < 3 :
        cost = d * 40
    elif d < 7 :
        cost = (d*40)-20
    else :
        cost = (d*40)-50
    return f'당신의 렌터카 비용은 {cost}$입니다.'
# 2
def solution2(day):
    result = day * 40
    if day >= 7 :
        result -= 50
    elif day >= 3:
        result -= 20
    return f'당신의 렌터카 비용은 {result}$입니다.'
```



---

### 문제6

> 같은 숫자가 한개 있거나 두개가 들어있는 리스트가 주어집니다. 이러한 리스트에서 숫자가 한개만있는 요소들의 합을 구하는 함수를 작성하세요.

> 예를 들어, repeats([4, 5, 7, 5, 4, 8]) = 15 는 7과 8이 한번만 나오기 때문에 두개를 더한 15가 결과값으로 도출됩니다. 

```python
# 1
def solution(nums):
    sum1 = 0
    for i in nums:
        if(nums.count(i) == 1):
            sum1 += i
    return sum1    

# 2 
def solution2(s):
    numbers = set()
    
    for n in s:
        if n in numbers:
            numbers.remove(n)
        else:
            numbers.add(n)
    return sum(numbers)
```



---

### 문제7

> 과수원에 농부 한명이 썩은 과일이 몇개 들어있는 과일 봉지를 가지고 있습니다. (이 과일 봉지는리스트를 의미합니다) 농부는 썩은 과일 조각들을 모두 신선한 것으로 교체하고 싶어합니다. (rotten과일을 신선한 과일로 바꿔야 합니다)

> 예를 들어,
>
> - ["apple","rottenBanana","apple"] 이라는 리스트가 주어진 경우, 대체된 리스트는["apple","banana","apple"]이어야 합니다. 당신은 썩은 과일들이 신선한 과일로 대체되어 리스트로 만드는 함수를 작성하면 됩니다.

> 유의
>
> - 만약 리스트가 null/nil/None이거나 비어 있는 경우 빈 리스트를 반환합니다.
> - 반환된 리스트는 소문자여야 합니다,

```python
def solution(fruits):
    if not fruits:
        return []
    
    result = []
    for i in fruits:
        if "rotten" in i:
            r = i.replace("rotten","")
            result.append(r.lower())
        else :
            result.append(i)
    return result
                    
print(solution(["apple","rottenBanana","apple"]))    
```



---

### 문제8

> 마을의 신호등을 제어하는 코드를 작성하려고 합니다. 녹색 -> 노란색 -> 빨간색  -> 녹색으로 변환하는 함수가 필요합니다. 

> 현재의 불빛 상태를 나타내는 인수하고 함수를 실행 시켰을 때 변경 되어야 하는 빛의 색을  나타내는 함수를 완성하세요.

> 예시:update_light('green') should return 'yellow'.

```python
#1 
def solution(color):
    result = ""
    if color == "green":
        result += "yellow"
    elif color == "yellow":
        result += "red"
    else:
        result += "green"
    return f'{color}는 {result}로 변경 되어야 합니다.'
print(solution("green"))

# 2
def solution2(color):
    result = {"green" : "yellow", "yellow":"red", "red":"green"}[color]
    return f'{color}는 {result}로 변경 되어야 합니다.'
print(solution2("green"))




```



---

### 문제9

> 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 

> 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다. 

```python
# 1 
def solution(a, b):
    min1 = []
    if b > a :
        a, b = b, a
        
    for i in range(1, a+1):
        if(a%i==0 and b%i==0):
            min1.append(i)
            
    max1 = a*b//max(min1) 
    
    return [max(min1), max1]
    
print(solution(12, 3))

# 2
def solution2(n, m):
    c = max(n,m)
    d = max(n,m)
    t = 1
    while t > 0 :
        t = c % d
        c = d
        d = t
    answer = [c,int(n*m/c)]
    return answer
print(solution2(12, 3))
```

