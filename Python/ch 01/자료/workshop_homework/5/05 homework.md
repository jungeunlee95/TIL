# 05 homework

## 학습해야 할 내용

 • 조건문 및 반복문

 • 함수



1. **List는 for 문을 실행하면 모든 요소를 순차적으로 돌면서 반복문을 수행합니다. 임의의 리스트 my_list의 값을 하나씩 출력하는 코드를 아래에 작성하시오.**


```python
my_list = [1,2,3,4,5]
for i in my_list:
    print(i)
```



2. **위에 작성한 코드를 인덱스(index) 값과 함께 출력하는 코드로 변경하시오.**

```python
my_list = [1,2,3,4,5]
for idx, value in enumerate(my_list):
    print(f'{idx} : {value}')
```



3. **딕셔너리는 key, value로 구성되어 있습니다. 따라서, 딕셔너리 my_dict 각각의 상 황에 따라 반복문을 수행할 수 있도록 빈칸을 채우시오.**

   key : for key in ______: 

   value : for value in ___________:

   key와 value : for key, value in _________:

```python
my_dict = {'a':1}

for key in my_dict:
    print(key)
for value in my_dict.values():
    print(value)
for key,value in my_dict.items():
    print(key, value)
```



4. **result에 저장된 값은?  0 : return이 없음 **

   ```python
   def my_func(a, b):
   	 c = a + b 
   	 print(c) 
   result = my_func(1, 5)
   ```



### workshop

```python
def is_palindrome(word):
    list_word = list(word)
    for i in range(len(list_word) // 2):
        if list_word[i] != list_word[-i-1]:
            return False
    return True
print(is_palindrome('level'))  # True
print(is_palindrome('apple'))  # False
```

