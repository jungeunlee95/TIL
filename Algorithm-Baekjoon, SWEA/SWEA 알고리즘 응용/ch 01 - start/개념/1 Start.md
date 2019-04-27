### Start

![1553046751585](../typora-user-images/1553046751585.png)

![1553046766648](../typora-user-images/1553046766648.png)

![1553046797338](../typora-user-images/1553046797338.png)

![1553047607391](../typora-user-images/1553047607391.png)

![1553047740044](../typora-user-images/1553047740044.png)

![1553047749252](../typora-user-images/1553047749252.png)

![1553047760236](../typora-user-images/1553047760236.png)

![1553047765673](../typora-user-images/1553047765673.png)

![1553047773327](../typora-user-images/1553047773327.png)

![1553047779284](../typora-user-images/1553047779284.png)

![1553047917806](../typora-user-images/1553047917806.png)

![1553047944241](../typora-user-images/1553047944241.png)

![1553047953990](../typora-user-images/1553047953990.png)

​		숫자 i의 j번째 비트가 1인지 아닌지.

![1553047959817](../typora-user-images/1553047959817.png)

![1553047968142](../typora-user-images/1553047968142.png)

![1553047977286](../typora-user-images/1553047977286.png)

```python
def B(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output, end = ' ')

a = 0x10
x = 0x01020304

print("%d = " % a, end='')
B(a)
print()
print("0%X = " % x, end='')
for i in range(0, 4):
    B((x>>i*8)&0xff)
    
''' 출력 '''
# 16 = 00010000 
# 01020304 = 00000100 00000011 00000010 00000001 
```



![1553047983907](../typora-user-images/1553047983907.png)

![1553047990643](../typora-user-images/1553047990643.png)

![1553047997224](../typora-user-images/1553047997224.png)

![1553048002743](../typora-user-images/1553048002743.png)

```python
def B(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output)

a = 0x86 #1000 0110
key = 0xAA

print("a       => ", end='')
B(a)

print("a^=key  => ", end='')
a ^= key
B(a)

print("a^=key  => ", end='')
a ^= key
B(a)

'''출력'''
# a       => 10000110
# a^=key  => 00101100
# a^=key  => 10000110
```

![1553048010469](../typora-user-images/1553048010469.png)

![1553048032053](../typora-user-images/1553048032053.png)

![1553048040496](../typora-user-images/1553048040496.png)

![1553048047451](../typora-user-images/1553048047451.png)

![1553048057147](../typora-user-images/1553048057147.png)

![1553048063063](../typora-user-images/1553048063063.png)



![1553048068195](../typora-user-images/1553048068195.png)



![1553048073335](../typora-user-images/1553048073335.png)



![1553048078831](../typora-user-images/1553048078831.png)

![1553048084506](../typora-user-images/1553048084506.png)

![1553048091438](../typora-user-images/1553048091438.png)

![1553048099106](../typora-user-images/1553048099106.png)

![1553048105606](../typora-user-images/1553048105606.png)



