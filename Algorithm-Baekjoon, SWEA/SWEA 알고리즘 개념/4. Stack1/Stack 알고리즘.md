# Stack

**LIFO (Last-In-First-Out) 구조**

![1550018717183](../typora-user-images/1550018717183.png)

![1550018748234](../typora-user-images/1550018748234.png)



![1550018961713](../typora-user-images/1550018961713.png)

---

![1550020416396](../typora-user-images/1550020416396.png)

![1550020599117](../typora-user-images/1550020599117.png)

---

![1550020422237](../typora-user-images/1550020422237.png)

![1550020611970](../typora-user-images/1550020611970.png)

---

### 기본 구현

```python
stack = [0] * 10
top = -1
for i in range(3):
    stack[top+1] = i
    top += 1
    
for i in range(3):
    t = stack[top]
    top-=1
      print(t)
```

---

![1550020914627](../typora-user-images/1550020914627.png)



![1550021198663](../typora-user-images/1550021198663.png)

![1550021206017](../typora-user-images/1550021206017.png)

![1550021214994](../typora-user-images/1550021214994.png)

```python

def checkStack(s):
    stack = [0] * len(s)
    top = -1
    wrong = 0
    for i in range(len(s)):
        if (s[i] == "("):
            top += 1
            stack[top] = s[i]
        elif s[i] == ")":
            if top == -1:
                wrong = 1
                break
            if stack[top] == "(":
                top -=1
    if top == -1 and not wrong : return "Yes"
    else: return "No"

a = "()()((()))"
b = "((()((((()()((()())((())))))"

print("괄호 짝이 맞니?",checkStack(a))
print("괄호 짝이 맞니?",checkStack(b))

```



---

![1550024363563](../typora-user-images/1550024363563.png)

![1550024369350](../typora-user-images/1550024369350.png)

---

![1550024394060](../typora-user-images/1550024394060.png)

![1550024412626](../typora-user-images/1550024412626.png)

![1550024427751](../typora-user-images/1550024427751.png)

## 피보나치 수를 구하는 재귀함수

![1550024932858](../typora-user-images/1550024932858.png)

![1550024936989](../typora-user-images/1550024936989.png)

> ## ---> 엄청난 중복 호출이 존재함!!!!!
>
> ![1550024968897](../typora-user-images/1550024968897.png)



## Memoization 

### - 중복 제거(이전에 계산한 값을 메모리에 저장 -> 다시 계산하지 X)

```python
memo = [0] * 100
memo[0] = 0
memo[1] = 1

def f(n):
    if n <2 or memo[n] != 0 :
        return memo[n]
    memo[n] = f(n-1) + f(n-2)
    return memo[n]
```

![1550029770603](../typora-user-images/1550029770603.png)





---

# DP(Dynamic Programming)

![1550030833235](../typora-user-images/1550030833235.png)

![1550030841140](../typora-user-images/1550030841140.png)

![1550030847800](../typora-user-images/1550030847800.png)

![1550030853964](../typora-user-images/1550030853964.png)

```python
def fibo2(n):
    f = [0,1]
    
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
```

---





---

# DP의 구현 방식

### fiboMemo() -> 재귀적 DP -> 다이나믹 백트레킹

### fiboIterative() -> 반복적 DP -> DP

![1550031477954](../typora-user-images/1550031477954.png)

![1550031492256](../typora-user-images/1550031492256.png)



![1550031500095](../typora-user-images/1550031500095.png)

![1550031506935](../typora-user-images/1550031506935.png)

![1550031516928](../typora-user-images/1550031516928.png)



![1550036237931](../typora-user-images/1550036237931.png)

![1550036248375](../typora-user-images/1550036248375.png)

![1550036253696](../typora-user-images/1550036253696.png)



![1550036260131](../typora-user-images/1550036260131.png)

![1550036266166](../typora-user-images/1550036266166.png)

![1550036273105](../typora-user-images/1550036273105.png)

![1550036278108](../typora-user-images/1550036278108.png)

![1550036282804](../typora-user-images/1550036282804.png)

![1550036287382](../typora-user-images/1550036287382.png)

![1550036291756](../typora-user-images/1550036291756.png)

![1550036296268](../typora-user-images/1550036296268.png)

![1550036300968](../typora-user-images/1550036300968.png)

![1550036306947](../typora-user-images/1550036306947.png)

![1550036312050](../typora-user-images/1550036312050.png)

![1550036317711](../typora-user-images/1550036317711.png)