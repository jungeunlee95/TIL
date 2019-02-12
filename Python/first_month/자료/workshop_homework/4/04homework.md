### 04homework

1. Python에서 사용할 수 없는 식별자(예약어)를 찾아 3개만 작성하세요.

``` 
for
if
not
```

2. 파이썬에서 float는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다. (floating point rounding error) 따라서, 아래의 값을 비교하기 위해 작성해야하는 코드를 작성하세요.
    a = 0.1 * 3 

  b = 0.3

```
print(round(a,2) == b)
```

3. “ 안녕, 철수야 ” 를 String Interpolation을 사용하여 출력하세요.

```
name = "철수"
print('안녕, %s야' % name)
```

4. 다음 중 형변환시 오류가 발생하는 것은?     5

​      1) str(1)      2) int(‘30’)    3) int(5)       4) bool(‘50’)      5) int(‘3.5’)

5. 변경할 수 있는(mutable) 것과 변경 불가능한 것(immutable)을 분류하시오.

   mutable	        : List, Set, Dictionary

   immutable	: Tuple, String, Range





### 04workshop

두 개의 정수 n과 m이 주어집니다. 반복문을 사용하지 않고 별(*) 문자를 이용해 가로 의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요

```python
a = '*'* 4 + '\n'
print(a*9) 
```



 다음 딕셔너리에서 평균 점수를 출력하시오

```python
student = {'python' : 80, 'algorithm' : 99, 'django' : 89, 'flask' : 83}
sum1 = 0 
for i in student:
    sum1 += student[i]
print(sum1/len(student))
```



다음은 학생들의 혈액형(A, B, AB, O)에 대한 데이터이다. for문을 이용하여 각 혈액형 별 학생수의 합계를 구하시오.

```python
blood_types = ['A','B','A','O','AB','AB','O','A','B','O','B','AB']
A = blood_types.count('A')
B = blood_types.count('B')
AB = blood_types.count('AB')
O = blood_types.count('O')
print(" A : {}명 \n B : {}명\n AB : {}명\n C : {}명\n".format(A,B,AB,O))
        
        
```

