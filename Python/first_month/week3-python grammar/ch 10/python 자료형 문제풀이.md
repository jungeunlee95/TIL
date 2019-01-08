#  2019-01-08

### 문제1

> 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하세요. 

warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

```python
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
a = input("투자 종목명 입력 : ")
if a in warn_investment_list :
    print("투자 경고 종목입니다.")
else :
    print("투자 경고 종목이 아닙니다.")
```



---

### 문제2

> 다음 리스트에서 10 이상인 수를 전부 더해서 출력하세요.

> exNumber = [43, 2, 6, 34, 12, 32, 7, 9, 81, 51]

```python
exNumber = [43, 2, 6, 34, 12, 32, 7, 9, 81, 51]
sum1 = 0
for i in exNumber :
    if (i > 9) :
        sum1 += i
print(sum1)
        
```



---

### 문제3

> A 기업의 입사 시험은 필기 시험 점수가 80점 이상이면서 코딩 시험을 통과해야 합격이라고 정했습니다. (코딩 시험 통과 여부는 True, False로 구분) 사용자로부터 필기시험 점수를 입력받아 '합격' 혹은 '불합격' 여부를 판단하는 코드를 작성하세요.

```python
# 1
a = int(input("필기점수:"))
b = input("코딩시험통과?(Y / N) : ")
if(a>79):
    if(b.lower()=="y"):
        print("합격")
    else :
        print("불합격")
else :
 print("불합격")

# 2
written_test = int(input("필기점수 : "))
coding_test = 'True'
if written_test >= 80 and coding_test == 'True':
    print("합격")
else : 
    print("불합격")
```



---

### 문제4

> 다음 소스 코드를 완성하여 1부터 100까지의 숫자를 출력하면서 2의 배수일 때는 'Fizz', 11의 배수일 때는 'Buzz', 2와 11의 공배수일 때는 'FizzBuzz'가 출력되게 만드세요.

```python
for i in range(1,101):
    if(i%2==0 and i%11 ==0):
        print(i , "FizzBuzz")
    elif(i%2==0):
        print(i , "Fizz")
    elif(i%11==0):
        print(i , "Buzz")
    else:
        print(i)
```



---

### 문제5

> 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하세요.

```python
# 1
a = input("숫자 3개를 입력하세요 : ")
b = a.split(' ')
print(max(b))

# 2
num1 = input("숫자 1 입력하세요 : ")
num2 = input("숫자 2 입력하세요 : ")
num3 = input("숫자 3 입력하세요 : ")

if num1 > num2:
    max_num = num1
else:
    max_num = num2

if num3 > max_num:
    max_num = num3
print(max_num)
```



---

### 문제6

> 다음은 학생들의 혈액형(A, B, AB, O)에 대한 데이터입니다. 각 혈액형 별 학생수의 합계를 구하세요.

```python
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

result = {}
result2 = {}

# 1
for i in blood_types:
    if i in result:
        continue
    else:    
        result[i] = blood_types.count(i)   
print(result)

# 2
for blood_type in blood_types:
    if blood_type in result2:
        result2[blood_type] += 1
    else:
        result2[blood_type] = 1
print(result2)
```



---

### 문제7

> 다음 리스트의 요소값 중에서 중복되는 값만 뽑아서 새로운 리스트로 옮기고 요소의 개수를 출력하세요. 

> some_lists = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

```python
some_lists = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# 1 중복된 값만 출력
copy_list = []
for alpa in some_lists :
    if some_lists.count(alpa) > 1:
        copy_list.append(alpa)
print(list(set(copy_list)))

# 2  중복된 값을 따로 뽑아 개수 출력
copy_dict2 = {}
for alpa in some_lists:
    if some_lists.count(alpa) > 1:
        copy_dict2[alpa] = some_lists.count(alpa)
print(copy_dict2)

# 3 중복된 값을 뺀 나머지 리스트, 개수 출력
lists = []
for some_list in some_lists:
    if some_list not in lists:
        lists.append(some_list)
print(lists, len(lists))
```



---

### 문제8

> 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다. 네 과목의 평균 점수가 80점 이상일 때 합격이라고 정했습니다. 평균 점수에 따라 '합격', '불합격'을 출력하는 프로그램을 만드세요.  단, 점수는 0점부터 100점까지만 입력받을 수 있으며 범위를 벗어났다면 '잘못된 점수'를 출력하고 합격, 불합격 여부는 출력하지 않아야 합니다. 

```python
# 1
scores = input("국어, 영어, 수학, 과학 점수 입력 : ")
scores_list = scores.split()

for i in scores_list:
    if(int(i) > 100 ) :
        print("잘못된 점수입니다")
        break
else: 
    sum1 = 0
    for i in scores_list:
        sum1 += int(i)
    avg = sum1/4

    if(avg>79):
        print(avg, "합격!")
    else:
        print(avg, "불합격!")
        
# 2
kor, eng, math, sci = map(int, input("국어, 영어, 수학, 과학 점수 입력 : ").split())
avg = (kor + eng + math + sci) / 4

if 0<= kor <=100 and 0<= eng <=100 and 0<= math <=100 and 0<= sci <=100 :
    if avg >= 80:
        print("합격")
    else:
        print("불합격")
else:
    print("잘못된 점수")
```



---

### 문제9

> 문자열 요소로만 이루어진 리스트에서 문자열 길이가 2 이상이고 주어진 문자열의 첫번째와 마지막 문자가 같은 요소를 모아 새로운 리스트를 만들고 해당 리스트 요소의 개수를 구하세요.

> samples = ['level', 'asdwe', 's', 'abceda', 'gsdwrtfg'] -> 결과값: 3 

```python
samples = ['level', 'asdwe', 's', 'abceda', 'gsdwrtfg'] 
# 1
lists = []
for i in samples:
    if len(i)>1 and i[0] == i[-1]:
        lists.append(i)  
print(lists, len(lists))

```



---

### 문제10

> 다음 리스트에서 중복된 요소를 제거한 리스트를 출력하세요. 

> items = [10,20,40,20,10,30,50,60,40,80,50,40,20,30,10] 

```python
items = [10,20,40,20,10,30,50,60,40,80,50,40,20,30,10] 
# 1
lists = []
for i in items:
    if i in lists:
        continue
    else:
        lists.append(i)
print(lists)

# 2
number = []
for item in items:
    if item not in number:
        number.append(item)
print(number)
```



---

### 문제11

> 다음 리스트에서 0번째 4번째 5번째 요소를 지운 새로운 리스트를 생성하세요.

> colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']

```python
colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']
# 1 
delteindex = [0,4,5]
fruit = []
# for color in colors:
#     if colors.index(dolors) not in (0,4,5) :
for i in range(0, len(colors)):   
    if i not in delteindex:
        fruit.append(colors[i])
print(fruit)

# 2
fruit = []
for a, colors in enumerate(colors):
    if a not in (0,4,5):
        fruit.append(colors)
print(fruit)
```



---

### 문제12

> 세 정수 A, B, C가 입력값으로 주어질 때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하세요. 

```python
# 1
a, b, c = map(int, input("정수 3개를 입력하세요").split())
numbers = [a, b, c]
print(sorted(numbers)[1])

# 2
a, b, c = map(int, input("정수 3개를 입력하세요").split())
if((a>=b and b >= c) or (c >= b and b >= a)):
    print(b)
elif((b>=c and c >= a) or (a >= c and c >= b)):
    print(c)
else:
    print(a)
```



---

### 문제13

> 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하세요. 각 통화별 환율은 다음과 같습니다. (사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정합니다.)

```python
currency = {
    'USD': 1167, 'JPY': 1.096, 'EURO': 1268, 'CNY': 171
} 
# 1
money = input("금액 : ").split()
if(money[1]=="달러"):
    result = int(money[0]) * int(currency["USD"])
elif(money[1]=="엔"):
    result = int(money[0]) * int(currency["JPY"])
elif(money[1]=="유로"):
    result = int(money[0]) * int(currency["EURO"])
elif(money[1]=="위안"):
    result = int(money[0]) * int(currency["CNY"])
else:
     print("등록되지 않은 통화입니다.")
print(result)

# 2
name = {
    '달러':'USD', '엔':'JPY','유로':'EURO', '위안':'CNY'
}
money = input("금액 : ").split()
result = int(money[0]) * int(currency[name[money[1]]])

print(result, "원")

# 3
user_in = input("금액 입력 : ").split()
amount = user_in[0]
currencys = user_in[1]

if currencys == '달러':
    ratio = 1167
elif currencys == '엔':
    ratio = 1.096
elif currencys == '유로':
    ratio = 1268
else:
    ratio = 171
    
print(ratio * int(amount), "원")

```

