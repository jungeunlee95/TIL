# 06 - Django

`$ mkdir 06_django`

`$ cd 06_django/`

` $ pyenv virtualenv 3.6.7 06_django-venv`

`$ pyenv local 06_django-venv`

` $ pip install django`

` $ pip install django_extensions ipython`

**project** : `$ django-admin startproject django_06 .`

**pages** : `python manage.py  startapp csvpratice`

**server 실행** :  `python manage.py runserver $IP:$PORT`



---

### 초반 설정

**settings.py**

```python
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'csvpratice',
    'django_extensions', 
]
```

**csvpratice/templates/index.html**

```html
<h1>하이</h1>
```

**views.py**

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
```

**django_06/urls.py**

```python
from django.contrib import admin
from django.urls import path, include

from csvpratice import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('csvpratice.urls')),
]
```

**csvpratice/urls.py**

```python
from django.urls import path
from . import views

app_name = 'movies'   # html에서  href="{% url 'movies:new' %}" 이런식으로

urlpatterns = [
    path('', views.index, name='index'),
]
```



**csvpractice/templates/csvpratice/ ... html파일들**



---



---

## model 만들기

**models.py**

```python
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.TextField()
    audience = models.IntegerField()
    genre = models.TextField()
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
    
    def __repr__(self):
        return f"<{self.title} : {self.genre}>"
    
    def __str__(self):
        return f"<{self.title} : {self.genre}>"
```

`$ python manage.py makemigrations`   

`$ python manage.py sqlmigrate`      : 실제  sql문 확인

`$ python manage.py migrate`

###  csv 파일 넣기 (06_django/data.csv)

`$ python manage.py dbshell`  

> `>>> .mode csv`
>
> `>>> .tables`   : 테이블 실제 이름 확인
>
> `>>> .import data.csv csvpratice_movie`



---

### 영화 views, templates

**views.py**

```python
from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    print(movies)
    return render(request, 'csvpratice/index.html', {'movies':movies})
    
def new(request):
    return render(request, 'csvpratice/new.html')
    
def create(request):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    
    movie = Movie(title=title, audience=audience, genre=genre, score=score, poster_url=poster_url, description=description)
    movie.save()
    
    return redirect('movies:detail', movie_id = movie.id)

def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'csvpratice/detail.html', {"movie":movie})
    
def edit(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'csvpratice/edit.html', {'movie': movie})
    
def delete(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    
    return redirect('movies:index')
```

**csvpratice/urls.py**

```python
from django.urls import path
from . import views

app_name = 'movies'   # html에서  href="{% url 'movies:new' %}" 이런식으로

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('<int:movie_id>/edit', views.edit, name='edit'),
    path('<int:movie_id>/delete', views.delete, name='delete'),
    
]
```

**base.html**

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <!--부트스트랩-->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.0/css/bootstrap.min.css" integrity="sha384-PDle/QlgIONtM1aqA2Qemk5gPOE7wFq8+Em+G/hmo5Iq0CCmYZLv3fVRDJ4MMwEA" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.0/js/bootstrap.min.js" integrity="sha384-7aThvCh9TypR7fIc2HV4O/nFMVCBwyIUKL8XCtKE+8xgCgl/PQGuFsvShjr74PBp" crossorigin="anonymous"></script>
    <!-- font awesome-->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    
    <link rel="stylesheet" href="{% static 'style.css' %}">
    <title>First Django!</title>
</head>
<body>
       <nav class="navbar navbar-expand-lg navbar-light bg-light sticky" style="z-index: 1;">
        <a class="navbar-brand" href="#">MySite</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        
         <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item active">
                <a class="nav-link" href="#">Q&A <span class="sr-only">(current)</span></a>
              </li>
            </ul>
        </div>
        
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
            <ul class="navbar-nav ml-auto">
            <li class="nav-item">
                <a class="nav-link" href="/movies/">영화목록 <span class="sr-only"></span></a>
            </li>
            <!--<li class="nav-item">-->
            <!--    <a class="nav-link" href="/">전생앱 <span class="sr-only"></span></a>-->
            <!--</li>-->
            </ul>
        </div>
        </nav>
    {% block body %}
    
    {% endblock %}
    
    
</body>
</html>
```



**index.html**

```html
{% extends 'csvpratice/base.html' %}
{% block body %}


<div class="container" style="text-align:center;">
    <hr>
    <h1>영화</h1>
    <br>
    <a href="{% url 'movies:new' %}" style="text-align:center;" class="btn btn-success">새 영화 등록 </a>
    <hr>
</div>
<div class="container">
    <h2>영화 목록</h2>
    <table class="table">
      <thead class="thead-dark">
        <tr>
          <th scope="col">no</th>
          <th scope="col">title</th>
          <th scope="col">score</th>
        </tr>
      </thead>
      <tbody>
        {% for i in movies %}
        <tr>
          <th scope="row">{{i.id}}</th>
          <td>
            <a href="{% url 'movies:detail' i.id %}">{{i.title}}</a>
          </td>
          <td>{{i.score}}점   
              <a href="#" class="btn btn-dark btn-sm">수정</a>
              <a href="#" class="btn btn-dark btn-sm">삭제</a>
          </td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
</div>

{% endblock %}
```



**new.html**

```html
{% extends "csvpratice/base.html" %}

{% block body %}
<div class="container">
    <h1> 새 영화 등록</h1>
    
    <form action="{% url 'movies:create' %}" method="POST">
    {% csrf_token %}        
      <div class="form-group">
        <label for="exampleFormControlInput1">제목</label>
        <input type="text" class="form-control" id="exampleFormControlInput1" name="title">
      </div>
      <div class="form-group">
        <label for="exampleFormControlInput1">관객</label>
        <input type="text" class="form-control" id="exampleFormControlInput1" name="audience">
      </div>
      <div class="form-group">
        <label for="exampleFormControlInput1">장르</label>
        <input type="text" class="form-control" id="exampleFormControlInput1" name="genre">
      </div>
      <div class="form-group">
        <label for="exampleFormControlInput1">평점</label>
        <input type="text" class="form-control" id="exampleFormControlInput1" name="score">
      </div>
      <div class="form-group">
        <label for="exampleFormControlInput1">post_url</label>
        <input type="text" class="form-control" id="exampleFormControlInput1" name="poster_url">
      </div>
      
      <div class="form-group">
        <label for="exampleFormControlTextarea1">내용</label>
        <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" name="description"></textarea>
      </div>
      
      <button type="button" class="btn btn-warning" onClick="location.href='/articles'">취소</button>
      <input type="submit" class="btn btn-warning" value="글쓰기"/>
    </form>
</div>

{% endblock %}
```



**detail.html**

```html
{% extends 'csvpratice/base.html' %}

{% block body %}

<div class="container" style="text-align:center;">
    <br><br>
    <div class="card">
      <h5 class="card-header">{{movie.title}}</h5>
      <div class="card-body">
        <img src="{{movie.poster_url}}" style="width:200px; height:300px;"></img>
        <h5 class="card-title">관객 : {{movie.audience}}</h5> <br>
        <h5 class="card-title">장르 : {{movie.genre}}</h5> <br>
        <h5 class="card-title">평점 : {{movie.score}}</h5> <br>
        <h5 class="card-title">줄거리 : {{movie.description}}</h5> <br>
        
        <a href="{% url 'movies:edit' movie.id %}" class="btn btn-dark btn-sm">수정</a>
        <a href="{% url 'movies:delete' movie.id %}" class="btn btn-dark btn-sm">삭제</a></td>
        <a class="btn btn-dark btn-sm" href="{% url 'movies:index' %}">목록</a>
      </div>
    </div>
    <br>
</div>



{% endblock %}

```



































