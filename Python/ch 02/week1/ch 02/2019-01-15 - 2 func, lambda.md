# 2019-01-15 - 2 func, lambda

```python
# 1
def hello():
    print("hello() 실행")

def greeting(func):
    func()

greeting(hello)  # hello() 실행


# 2
def hello():
    return "hello"

hi = lambda : "hi"

def greeter(func):
    return func()

print(greeter(hi))  # hi
```



**map만들어보기**

```python

# print(list(map(int, ["1","2"]))) 만들기! 
# 1. 빈 리스트 만들기
# 2. 인자로 받은 리스트를 돌며
# 3. 인자로 받은 함수를 각각의 요소에 적용한 값을 빈 리스트에 넣어
# 4. 빈 리스트를 리턴한다.
def my_map(func, input_list):
    list_a = []
    for i in input_list:
        list_a.append(func(i))
    return list_a
print(my_map(int, ["1","2"]))

# 2 list comprehension
def my_map(func, input_list):
    return [func(i) for i in input_list]
print(my_map(int, ["1","2"]))
```



**filter만들기**

```python
def is_even(num):
    return num % 2 == 0
# 1 
def my_filter(func, input_list):
    new_list = []
    for i in input_list:
        if func(i):
            new_list.append(func(i))
    return new_list
print(my_filter(is_even, [1,2,3,4,5]))

# 2
def my_filter(func, input_list):
    return [i for i in input_list if func(i)]
print(my_filter(is_even, [1,2,3,4,5]))

print(my_filter(lambda num: num % 2 == 0, [1,2,3,4,5])) 
```



**hof.py**

```python
def my_map(func, input_list):
    return [func(i) for i in input_list]
```



**lamda**

```python
import hof
import math

# 1
def add_two(num):
    return num + 2
# 람다로 가능-->  add_two = lambda num : num + 2
print(hof.my_map(add_two, [1,2,3,4]))

# 2 람다 사용
print(hof.my_map(lambda num:num+2, [1,2,3,4]))

# square라는 변수에 lambda를 통해 제곱하는 함수
square = lambda x : x **2
print(square(3))
# cube라는 변수에 세제곱
cube = lambda x : x **3
print(cube(5))
# sqrt 변수에 제곱근 (math활용)
sqrt = lambda x : math.sqrt(x)
print(hof.my_map(sqrt, [1,2,3,4]))
```

















