# 2019-01-09 - function_pratice 3



# 종합소득세 계산하기

> A라는 나라에서는 종합소득세는 과세표준 금액 구간에 따라 다른 세율이 적용됩니다.

| 과세표준액    | 세율 |
| ------------- | ---- |
| 1,200이하     | 6%   |
| 1,200 ~ 4,600 | 15%  |
| 4,600 ~       | 35%  |

즉, 1,300원을 벌었을 경우 `1,200\*0.06 + 100\*0.15`를 계산한 결과가 납부해야 하는 세액입니다.

함수 `tax(won)`을 만들고 납부해야하는 세금의 결과를 반환하는 함수를 만들어보세요.

```
예시)
tax(1200) #=> 72.0
tax(4600) #=> 582.0
tax(5000) #=> 722.0
```

```python
def tax(won):
    if won >= 4600:
        return 1200 * 0.06 + 3400 * 0.15 + (won-4600) * 0.35
    elif won >= 1200 :
        return (1200 * 0.06) + ((won-1200)*0.15) 
    else:
        return won * 0.06
    
    
print(tax(1200))
print(tax(4600))
print(tax(5000))
```



---

---

# 카쉐어링 요금 계산하기

> 카쉐어링 서비스는 요금을 다음과 같이 계산합니다.
>
> 대여는 10분 단위로 가능합니다.
>
> 1. 대여 요금 : 10분당 1,200원
> 2. 보험료 : 30분당 525원 (50분을 빌리면, 1시간으로 계산됩니다.)
> 3. 주행 요금 : km당 170원 (주행 요금은 100km가 넘어가면, 넘어간 부분에 대하여 할인이 50% 적용됩니다.)
>
> 예) 160km를 달렸으면, 170*100 + 85 *60
>
> 양의 정수인 대여시간(분)과 주행거리를 받아 계산 결과를 반환하는 함수 `fee(minute, distance)`를 만들어보세요.

------

```
예시) 
    fee(600, 50) #=> 91000
    fee(600, 110) #=> 100350
```

```python
# 1
def fee(minute, distance):
    cost = 0 
    
    #대여요금 
    cost += minute * 120
    
    # 보험료
    if(minute %30 > 0.6):
        cost += 525
    cost += minute//30 * 525

    # 주행요금
    if distance > 100 :
        cost += (distance - (distance-100))*170 + (distance-100)*85
    else :
        cost += distance * 170
    return cost

print(fee(600, 50))
print(fee(600, 110)) 
    
# 2
def fee2(minute, distance):
    
    result = minute * 120 + ((minute - 1) // 30 + 1) * 525
    if distance > 100 :
        result += 17000 + 85 * (distance - 100)
    else:
        result += 170 * distance
    return result

print(fee2(600, 50))
print(fee2(600, 110)) 

```



---

---

# 이상한 덧셈

> 숫자 구성된 리스트에서 양의 정수의 합을 구하는 함수 `positive_sum`을 작성하세요.

예시)

```python
positive_sum([1,-4,7,12]) #=> 20
positive_sum([-1, -2, -3, -4]) #=> 0
```

```python
# 1
def positive_sum(a):
    sum1 = 0
    for i in a :
        if i > 0:
            sum1 += i
    if sum1 == 0 :
        return 0
    else:
        return sum1
    
print(positive_sum([1,-4,7,12]))
print(positive_sum([-1, -2, -3, -4]))

# 2
def positive_sum2(a):
    return sum(filter(lambda x: x>0, a))
    
print(positive_sum2([1,-4,7,12]))
print(positive_sum2([-1, -2, -3, -4]))
```



---

---

# Collatz

> 1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측입니다. 작업은 다음과 같습니다.
>
> 1. 입력된 수가 짝수라면 2로 나눕니다. 
> 2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
> 3. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
>
> 예를 들어, 입력된 수가 6이라면 6→3→10→5→16→8→4→2→1 이 되어 총 8번 만에 1이 됩니다.
>
> 위 작업을 몇 번이나 반복해야하는지 반환하는 함수, collatz를 완성해 주세요.
>
> 단, 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환해 주세요.

예시)

```python
collatz(6) #=> 8
collatz(16) #=> 4
collatz(27) #=> 111
collatz(626331) #=> -1
```

```python
def collatz(num):
    cnt = 0
    while(num != 1):
        if num % 2 == 0 :
            num = num // 2
            cnt+=1
        else: 
            num = num * 3 + 1
            cnt+=1
    if cnt > 500 :
        cnt = -1
    return cnt

print(collatz(6))
print(collatz(16))
print(collatz(27))
print(collatz(626331))
```



---

---

# 솔로 천국 만들기

> 리스트가 주어집니다. 리스트의 각 요소는 숫자 0부터 9까지로 이루어져 있습니다. 
>
> 이때, 리스트에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 
>
> 리스트에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 반환하는 lonely 함수를 작성해 주세요.
>
> 단, 제거된 후 남은 수들을 반환할 때는 리스트의 요소들의 순서를 유지해야 합니다.  

예시)

```python
lonely([1, 1, 3, 3, 0, 1, 1]) #=> [1, 3, 0, 1]
lonely([4,4,4,3,3]) #=> [4,3]
```

```python

```

