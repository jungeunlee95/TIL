# 2019-01-04 2-Flask(request data 주고받기)



------

------

------

### workspace 새로 만들기 [flask_app]

- flask 설치

```
$ sudo pip3 install flask
// sudo : '관리자로 해주세용' 이라는 뜻
```

**app.py**

```python
# 구글에 python flask 검색해보기~ 
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```

------

### 서버실행

------

**[[[ cloud9 Terminal ]]]**

```
$ flask run --host=0.0.0.0 --port=8080
```

**[[[ git bash ]]]**

```
$ mkdir flask_app
$ cd flask_app/
$ code .
  	# app.py 만든 후 
$ pip install flask
$ flask run
```

**vs code** app.py파일 만들기

```python
from flask import Flask
 
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"

@app.route("/hello/<name>")  
def hello(name):
    return "Hello, " + name + "!"
```

![1546579009741](..\typora-user-images\1546579009741.png)

![1546579016808](..\typora-user-images\1546579016808.png)

![1546580675217](..\typora-user-images\1546580675217.png)



- **vs code에서 git bash키기**

Terminal -> New Terminal -> customize -> git bash



------



![1546586224664](..\typora-user-images\1546586224664.png)

### pratice  in vscode

**app.py**

```python
from flask import Flask, render_template, send_file
from datetime import datetime as dt
import random

app = Flask(__name__)

@app.route("/")
def index():
    # return send_file('home.html')
    lotto_num = random.sample(range(1,46),6)
    return render_template('index.html', lotto = lotto_num)

@app.route("/hello/<name>")  
def hello(name):
    return "Hello, " + name + "!"

@app.route("/reverse/<word>")  
def rev_string(word):
    #return ''.join(reversed(word))
    return word[::-1]

@app.route("/cube/<int:num>")  
def cube_num(num):
    # return은 무조건 string
    # return str(num ** 3)
    return "{}의 세제곱은 {}입니다.".format(num,num ** 3)

# 팰린드롬 확인 -> 앞으로 해도, 뒤로 해도 똑같은 값인지
#       true   or   false
@app.route("/ispal/<word>")  
def ispal_word(word):
    # if(word == word[::-1]):
    #     return "TRUE"
    # else:
    #     return "FALSE"
    return "Palindrome이 맞습니다." if word == word[::-1] else  "palindrome이 아닙니다." 

# /isitnewyear ==> 1월1일이면 "예" 아니면 "아니오"
@app.route("/isitnewyear")  
def isitnewyear():
    # now = dt.now()
    # nowDate = now.strftime('%m-%d')
    # return "예" if nowDate == '01-01' else "아니요"
    if dt.now().month == 1 and dt.now().day == 1:
        return "예" 
    else:
        return "아니요"
```

**index.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>INDEX</title>
</head>
<body>
    <h1>HELLO</h1>
    <h2>로또 번호 : {{ lotto }}</h2>
</body>
</html>
```

**home.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>HOME</title>
</head>
<body>
    <h1>HHHHHOOOMMMMEEEE~~</h1>
</body>
</html>
```



------

------

- web와 요청을 주고 받기 - 궁합

![1546590088301](..\typora-user-images\1546590088301.png)

**app.py**

```python
from flask import Flask, render_template, send_file, request
from datetime import datetime as dt
import random

app = Flask(__name__)

@app.route("/")
def index():
    # return send_file('home.html')
    lotto = random.sample(range(1,46),6)
    return render_template('index.html', lotto = lotto)
    
# index.html에서 입력받은 값을 그대로 출력한다.
stupid = []
@app.route("/goonghap")
def goonghap():
    me = request.args.get('me')
    you = request.args.get('you')
    
    stupid.append([me,you])
    
    percent = str(random.sample(range(40,100),1))
    return render_template('goonghap.html', me=me, you=you, num=percent)
```

**index.html**

```html
<!DOCTYPE html>
<meta charset="utf-8">
<html lang="en">
<head>
    <title>INDEX</title>
</head>
<body>
    <h1>궁합</h1>
    <p>궁합을 알려드립니다.</p>
    <form action="/goonghap">
        <p>당신의 이름 : </p>
        <input name="me" type="text"></input>
        <p>상대방의 이름 : </p>
        <input name="you" type="text"></input>
        <input type="submit">
    </form>

</body>
</html>
```

 **goonghap.html**

```html
<!DOCTYPE html>
<meta charset="utf-8">
<html lang="en">
<head>
    <title>궁합</title>
</head>
<body>
    <h1>궁합</h1>
    <h2>{{me}}님과 {{you}}님의 궁합은 {{num}}%입니다. </h2>
</body>
</html>
```



