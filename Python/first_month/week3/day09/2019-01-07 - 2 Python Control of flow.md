# 2019-01-07 - 2 Python Control of flow

---

# 조건문

지금까지의 코드는 위에서부터 아래로 순차적으로 명령을 수행하는 프로그램을 작성하였다. 

제어문(Control of Flow)은 크게 반복문과 조건문으로 나눌 수 있고, 이는 순서도(Flow chart로 표현이 가능하다.)

![1546837594800](..\typora-user-images\1546837594800.png)



## 조건문 문법

1. `if` 문은 반드시 일정한 참/거짓을 판단할 수 있는 `조건식`과 함께 사용이 되어야한다. `if <조건식>:`

2-1. `<조건식>`이 참인 경우 `:` 이후의 문장을 수행한다.

2-2. `<조건식>`이 거짓인 경우 `else:` 이후의 문장을 수행한다.

- 이때 반드시 **들여쓰기를** 유의해야한다.  파이썬에서는 코드 블록을 자바나 C언어의 `{}`와 달리 `들여쓰기`로 판단하기 때문이다.
- 앞으로 우리는 `PEP-8`에서 권장하는 `4spaces`를 사용할 것이다.



---

### 실습문제1 - 조건문 기초 활용

> **조건문을 통해 변수 num의 값과 홀수/짝수 여부를 출력하세요.**

------

```python
# 예시 출력)
# 3
# 홀수입니다.
num = int(input("숫자를 입력해주세요 :"))
if(num % 2 == 0 ):
    print("{}\n짝수입니다.".format(num))
else:
    print("{}\n홀수입니다.".format(num))
```



---

---

### 복수 조건문

> **2개이상의 조건문을 활용할 경우 `elif <조건식>:`을 활용한다.**



---

### 실습문제2 - 조건식 2개 이상 활용하기

> 조건문을 통해 변수 score에 따른 평점을 출력하세요

| 점수      | 등급 |
| --------- | ---- |
| 90점 이상 | A    |
| 80점 이상 | B    |
| 70점 이상 | C    |
| 60점 이상 | D    |
| 60점 미만 | F    |

```python
# 예시 출력)
# B

score = int(input("점수를 입력하세요 : "))
if(score<60):
    print("F")
elif(60<=score<70):
    print("D")
elif(70<=score<80):
    print("C")
elif(80<=score<90):
    print("B")
else:
    print("A")
```



---

### 실습문제3 - 중첩 조건문 활용

> **위의 실습문제 2코드를 활용하여  95점 이상이면, "참잘했어요"를 함께 출력해주세요**

```python
# 예시 출력)
# A
# 참잘했어요

score = int(input("점수를 입력하세요 : "))
if(score<60):
    print("F")
elif(60<=score<70):
    print("D")
elif(70<=score<80):
    print("C")
elif(80<=score<90):
    print("B")
else:
    print("A")
    if(95<=score):
        print("참잘했어요")
```



---

## 조건 표현식(Conditional Expression)

**활용법**

```
true_value if <조건식> else false_value
```

와 같이 표현식을 작성할 수 있다. 이는 보통 다른 언어에서 활용되는 삼항연산자와 동일하다.

- 표현식은 보통 조건에 따라 값을 정할 때 많이 활용된다

```python
a = int(input("숫자를 입력하세요 : "))
print('3맞음') if a == 3 else print('3아님')
---
# 숫자를 입력하세요 : 4
# 3아님
```

```python
num = int(input("숫자를 입력하세요 : "))
value = num if num >= 0 else 0
print(value)
```



---

### 실습문제 4 - 조건표현식과 동일한 `if`문 작성하기

> 다음의 코드와 동일한 `if`문을 작성해보세요.

```python
num = -5
value = num if num >= 0 else 0
print(value)
```

```python
# 예시 출력)
# 0
num = -5
if(num >= 0 ):
    print(num)
else:
    print(0)
```

---

### 실습문제 5 - 조건표현식 만들어보기

> 다음의 코드와 동일한 조건 표현식을 작성해보세요.

```python
num = 2
if num % 2 == 1:
    result = '홀수입니다.'
else:
    result = '짝수입니다.'
print(result)
```

```python
# 예시 출력)
# 짝수입니다.
num = 2
print("홀수입니다") if num % 2 == 1 else print("짝수입니다")
```







---

---

---

# 반복문

## `while` 문

`while`문은 조건식이 참(True)인 경우 반복적으로 코드를 실행합니다.  

**while 문은 종료조건을 반드시 설정해주어야 합니다.**

   						**while True:**

​					      		**print("계속계속")**

`while`문 역시 `<조건식>`이후에 `:`이 반드시 필요하며, 

이후 오는 코드 블록은 `4spaces`로 **들여쓰기**를 해주셔야 합니다.

```python
a = 0
while a < 5:
    print(a)
    a += 1
    
# 0
# 1
# 2
# 3
# 4
```



---

## `for` 문

`for`문은 정해진 범위 내(시퀀스)에서 순차적으로 코드를 실행합니다.

```python
for i in sequence:
    print("정해진 범위안에서 계속 반복")
    
for variable in sequence:
    code line1
    code line2   
    
for i in range(5):
    print(i)
print('끝')

# 0

# 1
# 2
# 3
# 4
# 끝
```

`for`문은 `sequence`를 순차적으로 **variable**에 값을 바인딩하며, 코드 블록을 시행합니다.

---

---

### 실습문제

> 반복문과 조건문만 활용하여 1~30까지 숫자 중에 홀수만 담긴 리스트를 만드세요.

list에서 값 추가는 `.append(value)`로 합니다.

------

```python
# 예시 출력)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

result = []
for i in range(31):
    if(i%2==1):
        result.append(i)
print(result)
```



---

### index와 함께 `for`문 활용하기

`enumerate()`를 활용하면, 추가적인 변수를 활용할 수 있습니다.

- `enumerate()`는 [파이썬 표준 라이브러리의 내장함수](https://docs.python.org/ko/3.6/library/functions.html) 중 하나이며, 다음과 같이 구성되어 있다.

```python
# enumerate()를 활용해서 출력해봅시다.
fruit = ['apple', 'orange', 'banana']
for idx, menu in enumerate(fruit):
    print(idx, ":", menu)

# 출력 ↓
# 0 : apple
# 1 : orange
# 2 : banana
```

```python
# enumerate() 함수를 사용하였을 때 어떻게 표현이 되는지 확인해봅시다.
list(enumerate(fruit, start = 4))

# 출력 ↓
# [(4, 'apple'), (5, 'orange'), (6, 'banana')]
```



---

### dictionary 반복문 활용하기

기본적으로 dictionary를 `for`문을 시행시키면 다음과 같이 시행됩니다.

dictionary의 `key`를 출력함으로써 `value`에도 접근할 수 있기 때문입니다.

따라서 dictionary의 value를 출력하기 위해서는 아래와 같이 작성합니다.

```python
# 옆자리 친구의 이름을 활용하여 dictionary를 만들어봅시다.
classroom = {'teacher':'lim','student1':'hong','student2':'kim'}

classroom.keys()
# dict_keys(['teacher', 'student1', 'student2'])

------------------------------------------------------
# key를 출력해봅시다.
for member in classroom:
    print(member)
# >> 출력 ↓
# teacher
# student1
# student2
------------------------------------------------------
# value를 출력해봅시다.
for member in classroom:
    print(classroom[member])
# >> 출력 ↓
# lim
# hong
# kim
```



- dictionary에서 `for` 활용하는 4가지 방법

```python
# 0. dictionary (key 반복)
for key in dict:
    print(key)

# 1. key 반복
for key in dict.keys():
    print(key)

# 2. value 반복    
for val in dict.values():
    print(val)

# 3. key와 value 반복
for key, val in dict.items():
    print(key, val)
```

---

### 실습문제

> 한번 직접 4가지 반복문을 활용해보고 출력되는 결과를 확인해보세요.

```python
classroom = {"teacher": "Kim", "student1": "Hong", "student2": "Kang"}

for key in classroom:
    print(key)
# teacher
# student1
# student2

for key in classroom.keys():
    print(key)
# teacher
# student1
# student2    

for val in classroom.values():
    print(val)
# lim
# hong
# kim

for key, val in classroom.items():
    print(key, val)
# teacher lim
# student1 hong
# student2 kim

```

---

## `break`, `continue`, `else`



### `break`

`break`문은 반복문을 종료하는 표현입니다. 

```python
for i in range(10):
    if(i != 0):
        break
    print(i)
# > 출력
# 0
```



---

#### 실습문제

> 조건문과 반복문, break, continue 를 통해서 아래의 코드와 동일한 코드를 작성하세요.
>
> (3이 있을 경우 True를 print하고, 아닐 경우 False를 print 합니다.)

```python
numbers = [1, 5, 10]
print(3 in numbers)
# 예시 출력)
# False
```

------

```python
numbers = [1, 5, 10]
# 1
if 3 in numbers:
     print(True)
else:
     print(False)
        
# > 출력
# False   

# 2
for idx, num in enumerate(numbers):  # [ [0, 1], [1, 5], [2, 10] ]
    if num == 3:
        print("True")
        break
    if idx + 1 == len(numbers):
        print("False")
# > 출력
# False   
```



### `continue`

`continue`문은 continue 이후의 코드를 수행하지 않고 다음 요소를 선택해 반복을 계속 수행합니다.

```python
# continue를 통해 
for i in range(6):
    if i % 2 == 0 : 
        continue   # 뒤의 코드를 보지않고, 다음 sequence -> 다음 for문을 돔
    print(f'{i}는 홀수입니다.')

# > 출력
# 1는 홀수입니다.
# 3는 홀수입니다.
# 5는 홀수입니다.
```



### `else`

`else`문은 끝까지 반복문을 시행한 이후에 실행됩니다.

(`break`를 통해 중간에 종료되지 않은 경우만 실행)

```python
# break가 안되는 상황을 만들어봅시다.
for i in range(3):
    if i == 3:          	   	   # 시퀀스에 3이 없음
        print(f'{i}에서 break.')
        break
else:
    print("break 안됨")

# > 출력
# break 안됨

```

```python
# 앞선 실습문제를 else를 통해 개선해봅시다.
numbers = [1, 5, 10]

for num in numbers:
    if num == 3:
        print("TRUE")
        break
else :
    print("FALSE")

```





---

### 대부분의 컨테이너 객체들은 for문으로 루핑이 가능

```python
for element in [1, 2, 3]: 
    print(element)
for element in (1, 2, 3): 
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123": 
    print(char)
for char in "abcdefg":
    print(char)
```









