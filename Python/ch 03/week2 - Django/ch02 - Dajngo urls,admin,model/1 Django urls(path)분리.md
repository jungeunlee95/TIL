## urls.py 나누기

**서버 실행** : ` $ python manage.py runserver $IP:$PORT`

![1549945413666](../typora-user-images/1549945413666.png)

**urls.py 만들기!**

------

**/first_workshop/urls.py**

```python
from django.contrib import admin
from django.urls import path, include
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('pages.urls')),
]
```



**/pages/urls.py**

```python
from django.urls import path
from . import views    # 현재폴더의 views 파일

urlpatterns = [
    path('info/', views.info),
    path('student/<str:name>', views.student),
    path('isval/', views.isval),
    path('grad/', views.grad),
    path('image/', views.image),
    path('', views.index)
]
```



![1549946004831](../../week2%20-%20Django/typora-user-images/1549946004831.png)

------

------

## 연습

`pip install requests`

**first_workshop/urls.py**

```python
from django.contrib import admin
from django.urls import path, include
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]
```

![1549949052731](../../week2%20-%20Django/typora-user-images/1549949052731.png)



**pages/urls.py**

```python
from django.urls import path
from . import views    # 현재폴더의 views 파일

urlpatterns = [
    path('info/', views.info),
    path('student/<str:name>', views.student),
    path('isval/', views.isval),
    path('grad/', views.grad),
    path('image/', views.image),
    path('', views.index),
    path('catch/', views.catch),
]
```

**pages/views.py**

```python
from django.shortcuts import render
import requests
import random
from datetime import datetime

# Create your views here.
def info(request):
    return render(request, "info.html")
    
def student(request, name):
    age = random.randint(20,30)
    student={"이정은":25, "바보":26, "멍청이": 27, "해삼":28}
    if name in student.keys():
        age = student[name]
        
    return render(request, "student.html", {"name":name, "age":age})

def isval(request):
    an = "아니요"
    today = datetime.now()
    month = today.month
    day = today.day
    if month==2 and day ==14:
        an="예"
    return render(request, "isval.html", {"an":an})
    # return render(request, "isval.html", {"month":month, "day":day})
    
def grad(request):
    # 졸업까지 며칠남음?
    now = datetime.now()
    end = datetime(2019, 5, 19)
    days = end - now
    return render(request, "grad.html", {"days":days.days})
    
def image(request):
    return render(request, "image.html")
    
def index(request):
    return render(request, "index.html")
    
def catch(request):
    message = request.GET.get("message")
    styles=['rounded', 'cosmic', 'gothic', 'alligator']
    style = random.choice(styles)
    url = "http://artii.herokuapp.com/make?text={}&font={}".format(message, style)
    result = requests.get(url).text
    return render(request, "catch.html", {"message":result})
```



------

## PAPAGO 만들어보기

**내 key값 환경변수에 넣기 Terminal**

```
touch telegram.py  #파이썬파일
vi ~/.bashrc
o 누르면 --INSERT-- 뜸

export 저장할이름=키값
```

```
ESC연타 =>
:wq 로 나오기
```

**잘 들어갔는지 확인하기**

```
$ source ~/.bashrc
$ echo $키설정이름
```

------

**pages/urls.py**

```python
from django.urls import path
from . import views    # 현재폴더의 views 파일

urlpatterns = [
    path('info/', views.info),
    path('student/<str:name>', views.student),
    path('isval/', views.isval),
    path('grad/', views.grad),
    path('image/', views.image),
    path('', views.index),
    path('catch/', views.catch),
    path('translate/', views.translate),
    path('result/', views.result),
]
```

**views.py**

```python
from django.shortcuts import render
import requests
import json
import os
''''''
def translate(request):
    return render(request, "translate.html")

def result(request):
    message = request.GET.get("word")
    
    naver_id = os.getenv('NAVER_ID')
    naver_secret = os.getenv('NAVER_SECRET')
    
    url = "https://openapi.naver.com/v1/papago/n2mt"
    
    headers = {
        'X-Naver-Client-Id': naver_id ,
        'X-Naver-Client-Secret': naver_secret
    }
    
    data = {
        'source': 'ko',
        'target': 'en',
        'text': message
    }
    
    result = requests.post(url, headers=headers, data=data).text
    result = json.loads(result)
    word = result["message"]["result"]["translatedText"]
    
    return render(request, "result.html", {"word":word})
```

























