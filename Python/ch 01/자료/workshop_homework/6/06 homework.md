# 05 homework

## 학습해야 할 내용

 • 함수

1. **. 우리가 이제까지 활용했던 print는 내장 함수(built-in function)입니다. 배웠던 내장 함수 중 5개만 나열해보세요**


```python
print()
sum()
max()
filter()
all()
any()

```



2. 다음 중 틀린 것은?
   (1) 함수는 오직 하나의 객체만 반환할 수 있어서, return a, b 처럼 쓸 수 없다. 

   (2) 함수에서 return을 작성하지 않으면 None 값을 반환한다. 

   (3) 함수의 인자(parameter)는 함수 선언시 설정한 값이며, 인수(argument)는 함수 호출시 넘겨주는 값이다. 

   (4) 가변 인자를 설정할 때는 인자 앞에서 *을 붙이고, 이때는 함수 내에서 tuple로 처리된다. 

   (5) 파이썬 활용되는 ‘스코프(scope)’ 룰에 따르면 변수에서 값을 Local scope -> Global scope -> Built-in scope 순으로 찾는다.



3. **함수의 인자 기본 값을 설정을 활용하여 곱셈의 결과를 반환하는 my_mul을 만들어주세요**

```python
예시 호출1) my_mul(6) 
예시 결과1) 6 
예시 호출2) my_mul(3, 5) 
예시 결과2) 1

def my_mul(*args):
    result = 1
    for i in args:
        result *= i
    return result
```





### workshop

>  **양의 정수 x를 입력 받아 제곱근의 근사값의 결과를 반환하는 함수를 작성하세요.** 

> **sqrt() 사용 금지**

```python
# 1
def my_sqrt(n):
    x, y = 0, n
    answer = 0
    
    while abs(answer ** 2 -n) > 0.0001:
        answer = (x + y) / 2
        if answer ** 2 < n :
            x = answer
        else:
            y = answer
    return answer
print(my_sqrt(2))

# 2
# 2
def my_sqrt2(n):
    min1, max1 = 0, 1
    while 1:
        if n == max1 ** 2:
            return max1
        elif min1 ** 2 < n < max1 ** 2:
            guess = (min1 + max1) / 2
            
            if round(min1, 5) == round(max1,5):
                return round(guess, 5)
            elif guess**2 > n:
                max1 = guess
            else:
                min1 = guess
        else:
            min1 += 1
            max1 += 1
print(my_sqrt2(5))
```

