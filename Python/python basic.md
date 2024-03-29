# tkinter

```python
from tkinter import *
import webbrowser

def browser():
    webbrowser.open("https://www.google.com")

root = Tk()

label = Label(root, text="Hi, how are you?", fg="white", bg="black") #Label은 인자 두 개를 받는 클래스. 첫 번째 인자는 어떤 tkinter 윈도우/프로그램에 넣을지. 두 번째 인자는 text="")

label2 = Label(root, text="Mister Woo's widget", fg="grey", bg="white")

btn = Button(root, text="I'm working hard", command = browser)

label.pack() #pack()은 method다. 
label2.pack()
btn.pack()

root.mainloop()
```

tkinter가 OOP의 대표적인 예시. 인터넷에 찾아보면 더 많은 자료가 있으니 참고하기를 바란다. 



# 일급객체

```python
def hello():
    return "hello"

def greeter(f):
    func()
    
greeter(hello)
```

함수 값을 hello라는 이름에 할당한 것. 

함수를 호출(call)한다는 것은 hello()를 호출하는 것. 

```python
sum()
```

이 함수는 input값으로 iterable(for 문을 돌릴 수 있는 친구)을 받는다. 

이 내장함수에 다른 값을 넣어줄 수 있다. 그리고 출력하면 새로운 값이 나온다. 이후 내장함수 기능을 사용하려고 해도 에러가 발생한다. 왜 호출하지 못하는가? sum에는 함수가 들어가있었는데 다른 값으로 대체되었기 때문이다. 

함수 프로시저가 변수에 들어가 있다고 생각하면 된다. 함수는 결국 어떤 알고리즘의 순서고 이것의 결과값이 함수명이라는 하나의 변수에 들어가 있는 것. 따라서 어떤 함수가 들어가있는 변수는 변수명 뒤에 ''()''을 붙여서 실행이 가능한 것. 일반적인 변수는 실행이 당연히 불가능하다. 

greeter()는 함수가 담긴 인자명을 변수로 받는 것. 그리고 그 변수명으로 명명된 함수를 실행한다.  그래서 우리가 아는 모든 함수를 넣기만 하면 error가 발생하지 않는다. 그래서 sum()을 넣어도 실행은 된다. 다만 sum은 인자를 필요로 하기 때문에 오류가 발생한다. 인자를 받지 않는 함수는 오류가 발생지 않는다. 그리고 뭔가 들어오는데 그거를 f로 쓰겠다는 것. 그리고 안에 인자로 들어온 함수를 f로 넣고 함수 f를 실행만 하는 친구.  

greeting(hello)는 f = hello가 되고 hello를 실행한 꼴이 되는 것이다. 

```python
def hello():
    print("hello")
 
```

hello() 함수는 입력값도 없고 출력값도 없다. 다만 화면에 "hello"를 출력하는 것을 실행할 뿐이다. 그래서 '화면에 "hello"를 출력'한다는 어떤 알고리즘에 hello라는 변수명이 붙은 것일 뿐이다. hi = hello로 할당하면 hi라는 변수명이 앞서의 알고리즘에 붙게 된다. 

```python
def hello():
    return "hello"
def greeter(f):
    func()
   
print(greeter(hello)) ==> None

def hello():
    return "hello"
def greeter(f):
    return func()

print(greeter(hello)) ==> hello
```

hello라는 함수를 정의하는 것 == hello를 출력하는 함수에 hello라는 이름을 붙이는 것. 

func.py 파일을 참고할 것. (return과 print의 차이점을 생각해보자. 별거는 없음 ㅋㅋ)

---

High Order Function

```python
# print(list(map(int, ["1" , "2"])))

def my_map(func, input_list):
    # 0. 빈 리스트를 만들고
    # 1. 인자로 받은 리스트를 돌면서
    # 2. 인자로 받은 함수를 각각의 요소에 적용한 값을 빈 리스트에 넣어서
    # 3. 빈 리스트를 리턴한다. 

    return [ func(i) for i in input_list] # 

a = ['1', '2', '3', '4', '5', '6']
print(my_map(int, a))

def is_even(num):

    return num %2 == 0

aa = filter(is_even, [1,2,3,4,5,6,7,8,9,10])
print(list(aa))

def my_filter(func, input_list):
    new_list = []
    for i in input_list:
        if func(i):
            new_list.append(func(i))
    return new_list

print(my_filter(is_even, aa))

def my_filter2(func, input_list):
    return [i for i in input_list if func(i)]

print(my_filter2(is_even, aa))
print(my_filter2(lambda num: num%2 == 0, [1,2,3,4,5,6,7,8]))
```



# lamda function

lambda 입력값 : 출력값, input

```python
add_three = lambda num : num+3
```

람다는 조건이 까다로워지면 쓰지 말 것! 아주 간단한 경우에만 사용하자. 



# Class & Instance / 변수 / method

#### 클래스 - 인스턴스간의 이름공간

- 클래스를 정의하면, 클래스 객체가 생성되고 해당되는 이름 공간이 생성된다.
- 인스턴스를 만들게 되면, 인스턴스 객체가 생성되고 해당되는 이름 공간이 생성된다.
- 인스턴스의 어트리뷰트가 변경되면, 변경된 데이터를 인스턴스 객체 이름 공간에 저장한다.
- 즉, 인스턴스에서 특정한 어트리뷰트에 접근하게 되면 인스턴스 -> 클래스 순으로 탐색을 한다.



결론: (self.~)는 인스턴스에서 찾다가 없으면 클래스, 그래도 없으면 글로벌에서 탐색.

```python
class Person:
    species = '인간'
    population = 0
    def __init__(self, name):
        population = 15          # 얘는 instance도 class도 아니다.  지금 이 def __init__ 안에서 외에는 print 할 수 없다.
        self.name = name         # 그냥 name = name
        self.population += 1     # 인스턴스 변수를 생성한 것처럼 만듬 조회만 하는 것이 아니다.
        Person.population += 1   # 클래스 변수를 접근하여 변경
    def greeting(self):
        print(f"{self.name}")    # self.name은 조회만 하는 method : 인스턴스를 찾고 => 클래스를 찾는다.
        print(f'{self.species}')

Person.population = 10

cr = Person('호날두')
john = Person('john')

print(cr.population)        # 11 (처음엔 class 변수에서 가져왔지만 이후 인스턴스)
print(Person.population)    # 12
```



#### 함수일 때와 class 일 때의 차이

함수는 절대 죽었다 깨어나도 def 함수 내부의 인자를 접촉할 수 없다.

class는 기본적으로 접근할 수 없지만 class.~ 를 통해 내부의 인자와 접촉할 수 있다.



#### 생성자 / 소멸자

- 생성자는 인스턴스 객체가 생성될 때 호출되는 함수이며, 소멸자는 객체가 소멸되는 과정에서 호출되는 함수입니다.

```python
def __init__(self):
    print('생성될 때 자동으로 호출되는 메서드입니다.')

def __del__(self):
    print('소멸될 때 자동으로 호출되는 메서드입니다.')
__someting__
```

위의 형식처럼 양쪽에 언더스코어가 있는 메서드를 스페셜 메서드 혹은 매직 메서드라고 불립니다.



```python
class Person:
    def __init__(self, name):
        print("사람이 생성되었습니다.")
        self.name = name
    def __del__(self):
        print("사람이 죽었습니다.")
```

```python
cr = Person("호날두")
cr = Person("우리형")
'''
사람이 생성되었습니다.
사람이 생성되었습니다.
사람이 죽었습니다.'''
```

cr = Person("우리형") 이 등장하면서 cr = Person(" 호날두") 는 우주미아처럼 메모리를 방황한다.

python은 이를 감지하여 garbage collector로 이를 제거한다.

참고로 garbage collector로 제거된 녀석은 본래 자신의 클래스 상태를 유지하여 `__del__` 역시 수정된 내용이 아닌 본래 자신의 메서드 실행.

- 아래와 같이 모두 사용할 수 있습니다!

```python
def __init__(self, parameter1, parameter2):
    print('생성될 때 자동으로 호출되는 메서드입니다.')
    print(parameter1)

def __init__(self, *args):
    print('생성될 때 자동으로 호출되는 메서드입니다.')

def __init__(self, **kwagrs):
    print('생성될 때 자동으로 호출되는 메서드입니다.')
```



- 따라서, 생성자는 값을 초기화하는 과정에서 자주 활용됩니다.
- 아래의 클래스 변수와 인스턴스 변수를 통해 확인해보겠습니다.



#### 클래스 변수 / 인스턴스 변수

```python
class Person:
    population = 0              # 클래스 변수 : 모든 인스턴스가 공유함.

    def __init__(self, name):   
        self.name = name        # 인스턴스 변수 : 인스턴스별로 각각 가지는 변수
```

```python
class Person:
    name = "john"            # 클래스 변수 : 모든 인스턴스가 공유함.
    population = 0

    def __init__(self, name="timmy"):
        self.name = name
        Person.population += 1
        # 인스턴스 변수 : 인스턴스별로 각각 가지는 변수
        print(f'인구가 증가하여 {Person.population} 명이 되었습니다.')
        
    def __del__(self):
        Person.population -= 1
        print(f'인구가 감소하여 {Person.population}명이 되었습니다.')
```

```python
john = Person("john")        # 인구가 증가하여 1 명이 되었습니다.
print(john.name)             # john
sangone = Person("sangone")  # 인구가 증가하여 2 명이 되었습니다.
print(sangone.name)          # sangone
print(Person.population)     # 2
```



#### 정적 메서드 / 클래스 메서드

- 메서드 호출을 인스턴스가 아닌 클래스가 할 수 있도록 구성할 수 있습니다.
- 이때 활용되는게 정적 메서드 혹은 클래스 메서드입니다.
- 정적 메소드는 객체가 전달되지 않은 형태이며, 클래스 메서드는 인자로 클래스를 넘겨준다.

#### 인스턴스 method

첫 번째 인자로 **인스턴스**를 받는 메서드

```python
class Person:
    # 인스터스 메서드
    def greeting(self):
```

#### 클래스 method

첫 번째 인자로 **클래스**를 받는 메서드

```python
class Person:
    @classmethod
    def count(cls):
```

#### static method

인자를 아무것도 받지 않는 메서드 (데이터 조작을 하지 않는 함수/메서드)

```python
class Person:
    @staticmethod
    def info():
```



```python
class Dog:
    num_of_dogs = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.num_of_dogs += 1
    
    def bark(self):
        print(f"멍멍, 저는 {self.name}, {self.age}살 입니다.")
    
    @staticmethod  # 얘가 없으면서 self가 없으면 객체는 실행 불가능.
    def info():    # self를 넣지 않은 메소드, class를 안 넣어줘도 메소드 실행 가능.
        print("강아지입니다.")
    
    @classmethod    # 얘가 없으면 사실상 self를 넣은 것과 똑같다.
    def count(cls): # 첫 번째 인자로 클래스를 넣어준다.
        print(f"{cls.num_of_dogs}마리 생존 중")
```

```python
puppy = Dog('멍멍이', 1)
puppy.info()           # 강아지 입니다.
Dog.info()             # 강아지 입니다.
Dog.count()            # 1마리 생존 중
# 만약 @classmethod가 없으면 error 난다. 따라서 Dog.count(Dog)라도 해야 한다.
puppy.count()          # 1마리 생존 중
Dog.bark()             # => Error
Dog.bark(nurung)       # => bark() 실행
```



#### 실습문제 - 정적 메소드

> 계산기 class인 `Calculator`를 만들어봅시다.

- 정적 메소드 : 두 수를 받아서 각각의 연산을 한 결과를 반환(return)
  1. `add()` : 덧셈
  2. `sub()` : 뺄셈
  3. `mul()` : 곱셈
  4. `div()` : 나눗셈

```python
class Calculator:
    
    def add(a, b):       # instance 시선에는 self 대신 a가 들어간 셈.
        return a + b
    
    @staticmethod
    def sub(a, b):
        return a - b
```

```python
Calculator.add(5, 3)   # 8 class는 self의 영향을 안 받는다
Calculator.sub(5, 3)   # 2

cal = Calculator()
cal.sub(5, 3)          # 2 static 덕분에 instance나 class가 안 들어감
cal.add(5, 3)          # a가 self처럼 적용하여 error
''' 만약에 def add를 수정한다면
def add(a, b, c):
    return b + c
라고 고치면 cal.add(5, 3) 이 8 나온다.'''
```





# 연산자 오버로딩(중복 정의)

- 파이썬에 기본적으로 정의된 연산자를 직접적으로 정의하여 활용할 수 있습니다.
- 몇가지만 소개하고 활용해봅시다.

```
+  __add__   
-  __sub__
*  __mul__
<  __lt__
<= __le__
== __eq__
!= __ne__
>= __ge__
>  __gt__
```

```python
class Person:
    def __init__(self, name, age, asset, height, gpa):
        self.name = name
        self.age = age
        self.asset = asset
        self.height = height
        self.gpa = gpa
    
    def __gt__(self, obj):
        if self.age > obj.age:
            return True
        else:
            return False
    
    def __add__(self, obj):
        print("하트 뿅뿅")
    
minsu = Person('minsu', 28, 700000, 178, 4.2)
insung = Person('insung', 38, 70000000000, 189, 1.8)
# insung.__gt__(minsu)
print(insung > minsu)      # True

minsu+insung     # insung.__add__(minsu)
```

**python operator overloading list** 를 검색하여 오버로딩 할 수 있는 목록 볼 수 있다.



# 상속

#### 기초

- 클래스에서 가장 큰 특징은 '상속' 기능을 가지고 있다는 것이다.
- 부모 클래스의 모든 속성이 자식 클래스에게 상속 되므로 코드재사용성이 높아집니다.

```python
class DerivedClassName(BaseClassName):
    code block
```



```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def sleep(self):
        print("쿨쿨")

class Student(Person):
    def study(self):
        print("열공열공")

john = Person('john')
john.sleep()    # 쿨쿨

sehwan = Student('sehwan')
sehwan.sleep()  # 쿨쿨
sehwan.study()  # 열공열공
```

- 이처럼 상속은 공통된 속성이나 메소드를 부모 클래스에 정의하고, 이를 상속받아 다양한 형태의 사람들을 만들 수 있습니다.

```python
issubclass(Student, Person) # (자식, 부모)True. 나머지는 False
```



#### super()

- 자식 클래스에 메서드를 추가 구현할 수 있습니다.
- 부모 클래스의 내용을 사용하고자 할 때, `super()`를 사용할 수 있습니다.

**아래 2개를 비교하라**

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')
        
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        self.student_id = student_id
        
p1 = Person('홍길동', 200, '0101231234', 'hong@gildong')
s1 = Student('학생', 20, '12312312', 'student@naver.com', '190000')
```

- 위의 코드를 보면, 상속을 했음에도 불구하고 동일한 코드가 반복됩니다.

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email)    # super()(self까지 옮김) 대신 Person을 써도 가능. 대신 self 추가 해야 한다.
        self.student_id = student_id
        
p1 = Person('홍길동', 200, '0101231234', 'hong@gildong')
s1 = Student('학생', 20, '12312312', 'student@naver.com', '190000')
```



#### method 오버라이딩

- 메서드를 재정의할 수도 있습니다.

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email)    # super()(self까지 옮김) 대신 Person을 써도 가능. 대신 self 추가 해야 한다.
        self.student_id = student_id
    
    def greeting(self):
        print(f"안녕하세요. 저는 {self.name}입니다.")

p1 = Person('홍길동', 200, '0101231234', 'hong@gildong')
s1 = Student('학생', 20, '12312312', 'student@naver.com', '190000')

p1.greeting()
s1.greeting()
'''
안녕, 홍길동
안녕하세요. 저는 학생입니다.'''
```



코드를 복사해 온다는 것 보단 자식 클래스에 없으면 부모 클래스에서 찾는다고 보는게 더 정확하다.

#### 상속관계에서의 이름공간

- 기존에 인스턴스 -> 클래스순으로 이름 공간을 탐색해나가는 과정에서 상속관계에 있으면 아래와 같이 확장됩니다.
- 인스턴스 -> 자식 클래스 -> 부모 클래스 -> 전역



# 선택 문제

> 사실 이전에 작성한 Mylist는 완벽하지 않았습니다.
>
> 한번 제대로 된 자료구조를 만들어보겠습니다.
>
> `Stack` 클래스를 간략하게 구현해봅시다.

> [Stack](https://ko.wikipedia.org/wiki/%EC%8A%A4%ED%83%9D) : 스택은 LIFO(Last in First Out)으로 구조화된 자료구조를 뜻합니다.

1. `empty()`: 스택이 비었다면 참을 주고,그렇지 않다면 거짓이 된다.
2. `top()`: 스택의 가장 마지막 데이터를 넘겨준다. 스택이 비었다면 None을 리턴해주세요.
3. `pop()`: 스택의 가장 마지막 데이터의 값을 넘겨주고 해당 데이터를 삭제한다. 스택이 비었다면 None을 리턴해주세요.
4. `push()`: 스택의 가장 마지막 데이터 뒤에 값을 추가한다. 리턴값 없음

**다 완료하신 분들은 repr을 통해 예쁘게 출력까지 해봅시다.**



# 기타

dir() 를 출력된 애들을 더 자세히 알아보고 싶다면 