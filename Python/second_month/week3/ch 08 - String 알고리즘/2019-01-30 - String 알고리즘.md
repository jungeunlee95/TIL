# 2019-01-30 - String



# 문자의 표현

![1548811327005](../typora-user-images/1548811327005.png)

# ↓

![1548812346596](../typora-user-images/1548812346596.png)

 # 

**big-endian, little-endian**

![1548812371537](../typora-user-images/1548812371537.png)

# ↓

![1548812396558](../typora-user-images/1548812396558.png)

---

---

---



# 문자열

![1548812459242](../typora-user-images/1548812459242.png)

![1548812756224](../typora-user-images/1548812756224.png)

![1548812790900](../typora-user-images/1548812790900.png)

![1548812848632](../typora-user-images/1548812848632.png)

![1548812856554](../typora-user-images/1548812856554.png)

![1548812865292](../typora-user-images/1548812865292.png)

![1548813117578](../typora-user-images/1548813117578.png)

---

![1548815136101](../typora-user-images/1548815136101.png)

![1548815144589](../typora-user-images/1548815144589.png)

---





---

![1548815177598](../typora-user-images/1548815177598.png)

---





---

### 타입 캐스팅

![1548815187795](../typora-user-images/1548815187795.png)

![1548815198336](../typora-user-images/1548815198336.png)

```python
ord('A')  # 65
chr(65)	  # 'A'
```



---





---

![1548815210825](../typora-user-images/1548815210825.png)

![1548815216899](../typora-user-images/1548815216899.png)

![1548815222839](../typora-user-images/1548815222839.png)

**python 식으로  구현해보기**

```python
def itoa(x):
    sr = ''
    while True:
        r = x % 10
        sr = sr + str(r + ord('0'))
        x //= 10
        if x == 0: break

    s = ''
    for i in range(len(sr) - 1, -1, -1):
        s = s + sr[i]
    return s


print(itoa(1234))
```



---















