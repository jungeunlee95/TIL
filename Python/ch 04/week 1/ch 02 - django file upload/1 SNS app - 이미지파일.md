crtl+shift : 줄이동

ctrl+d : 복사

---

db 삭제하고 다시 만들기

`$ python manage.py migrate sns zero`

`$ rm -rf media/`

`$ python manage.py migrate`

---

**admin.py**를 통해 admin페이지에서 다른 컬럼도 확인하고 싶으면

```python
class PostingModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at') # 레코드 개별화면 확인
    list_display = ('id', 'content', 'created_at', 'updated_at') # 리스트에서 표시할 컬럼들
    list_display_links = ('id', 'content')  # list 목록에서 clickable할 속성

admin.site.register(Posting, PostingModelAdmin)
```



`$   pip install django-imagekit`

**settings.py**  imagekit추가

```python
INSTALLED_APPS = [
    'imagekit',
    'django_extensions',
    'IPython',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'board',
    'sns',
]
```

**sns/models.py**

```python
# ImageKit
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFit

    # 원본 유지 저장
    # upload URL => /media/posting/origin/그날날짜
    # image = models.ImageField(blank=True, upload_to='posting/origin/%Y%m%d')

    # resize된 이미지 저장
    image = ProcessedImageField(
        upload_to='posting/resize/%Y%m%d',
        processors=[ResizeToFit(width=960, upscale=False)], # 크면 960으로줄이는데, 작은게 들어오면 늘리진 X
        format='JPEG',
    )

    # thumbnail
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFit(width=320, upscale=False)],
        format='JPEG',
        options={'quality':60},  # 원본 퀄리티의 60% 
    )
```

`$ python manage.py makemigrations`

`$ python manage.py migrate`

**thumbnail사진은 호출하는 순간 생성됨**

![1552369161071](../typora-user-images/1552369161071.png)

---

댓글

**sns/models.py**

```python
from django.db import models
# ImageKit
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFit

class Posting(models.Model):
    content = models.TextField(default='')
    icon = models.CharField(max_length=20)

    # 원본 유지 저장
    # upload URL => /media/posting/origin/그날날짜
    # image = models.ImageField(blank=True, upload_to='posting/origin/%Y%m%d')

    # resize된 이미지 저장
    image = ProcessedImageField(
        upload_to='posting/resize/%Y%m%d',
        processors=[ResizeToFit(width=960, upscale=False)], # 크면 960으로줄이는데, 작은게 들어오면 늘리진 X
        format='JPEG',
    )

    # thumbnail
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFit(width=320, upscale=False)],
        format='JPEG',
        options={'quality':60},  # 원본 퀄리티의 60%
    )


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} : {self.content[:20]}'

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        print()
        print(f'==== Save Posting with id : {self.id} ===')
        print(f'     content: {self.content}')
        if self.image:
            print(f'     image_size: {self.image.width}px * {self.image.height}px : {round(self.image.size / 1024)}kb')
        print('============================================')

class Comment(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.posting.content[:10] : {self.content[:20]}}'
```

`$ python manage.py makemigrations`

`$ python manage.py migrate`

**admin.py**

```python
from django.contrib import admin
from .models import Posting, Comment
# Register your models here.

class PostingModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at') # 레코드 개별화면 확인
    list_display = ('id', 'content', 'created_at', 'updated_at') # 리스트에서 표시할 컬럼들
    list_display_links = ('id', 'content')  # list 목록에서 clickable할 속성

admin.site.register(Posting, PostingModelAdmin)

class CommentModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('id', 'article', 'content', 'created_at', 'updated_at')
    list_display_links = ('id', 'content')

admin.site.register(Comment, CommentModelAdmin)
```

![1552370903993](../typora-user-images/1552370903993.png)

---

**sns/urls.py**

```python
from django.urls import path
from . import views

app_name='sns'

urlpatterns = [
    path('', views.posting_list, name='posting_list'),
    path('<int:posting_id>/', views.posting_detail, name='posting_detail'),
    path('create/', views.create_posting, name='create_posting'),
    
    path('<int:posting_id>/comment/create/', views.create_comment, name='create_comment'),
]
```

**sns/views.py**

```python
from django.shortcuts import render, get_object_or_404, redirect
from .models import Posting,Comment

def posting_list(request):
    # postings = Posting.objects.all().order_by('updated_at')  # 마지막 수정이 맨뒤
    postings = Posting.objects.all().order_by('-updated_at') # 마지막 수정이 맨위,
    return render(request, 'sns/list.html', {
        'postings':postings,
    })

def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comment_set.all().order_by('-created_at')
    return render(request, 'sns/detail.html', {
        'posting':posting,
        'comments':comments,
    })

def create_posting(request):
    if request.method == 'POST':
        posting = Posting.objects.create(
            content=request.POST.get('content'),
            icon = request.POST.get('icon'),
            image=request.FILES.get('image'),
        )
        return redirect('sns:posting_detail', posting.id)
    else:
        return redirect('sns:posting_list')

def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.method=='POST':
        comment = Comment()
        comment.content = request.POST.get('comment')
        comment.posting = posting
        comment.save()
    return redirect('sns:posting_detail', posting.id)
```



`touch sns/templates/sns/_forms.html`

**base.html**

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>
    {# ul.nav.nav-tabs>li.nav-item*2 #}
    <ul class="nav nav-tabs">
        <li class="nav-item">
            <a href="{% url 'sns:posting_list' %}" class="nav-link active">SNS</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" aria-disabled="true">Posting</a>
        </li>
    </ul>
    <br>

    <div class="container">
        {% block body %}
        {% endblock %}
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
```

**list.html**

```html
{% extends 'sns/base.html' %}

{% block body %}
{% include 'sns/_forms.html' %}
<hr>
    {% if postings %}
        <section class="card-columns">
            {% for posting in postings %}
                <article class="card mb-2">
                    <a href="{% url 'sns:posting_detail' posting.id %}">
                        <img src="{{ posting.image_thumbnail.url }}" alt="{{ posting.image }}"
                             class="card-img-top image-fluid">
                    </a>
                    <div class="card-body">
                        <i>{{ posting.icon }}</i>
                    </div>
                </article>
            {% endfor %}
        </section>
    {% endif %}
{% endblock %}
```

**detail.html**

```html
{% extends 'sns/base.html' %}

{% block body %}
    <div class="row mt-3">
        <div class="col-12 col-md-6">
            <div class="card">
                <img src="{{ posting.image.url }}" alt="{{ posting.image }}"
                class="card-img-top image-fluid">

                <div class="card-body">
                    <i>{{ posting.icon }}</i>
                    <hr>
                    <p class="card-text">
                        {{ posting.content }}
                    </p>
                </div>
            </div>
        </div>
        {# TODO: Comment form & list #}
        <div class="col-12 col-md-6">
            <div class="card mb-2">
                <div class="card-body">
                    <form action="{% url 'sns:create_comment' posting.id %}" method="post">
                        {% csrf_token %}
                        <label for="comment">Leave Comment</label>
                        <input type="text" name="comment" id="comment" class="form-control" autofocus>
                    </form>
                </div>
            </div>
            <div class="card">
                <ul class="list-group list-group-flush">
                    {% if comments %}
                        {% for comment in comments %}
                            <li class="list-group-item mb1">
                            {{ comment.id }} : {{ comment.content }}
                            </li>
                        {% endfor %}
                    {% else %}
                        <li class="list-group-item mb-1"></li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </div>
{% endblock %}
```

**_forms.html**

```html
<header class="mt-3">
    <form action="{% url 'sns:create_posting' %}" method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {# div.form-row.align-items.center #}
        <div class="form-row align-items center">
            <!-- icon select tag -->
            <div class="col-auto my-1">
                <label for="icon" class="sr-only">icon</label>
                <select name="icon" id="icon" class="custom-select mr-sm-2">
{#                    TODO: change icon value to FontAwesome icons #}
                    <option value=":)">:)</option>
                    <option value=":(">:(</option>
                    <option value=";)">;)</option>
                    <option value="?">?</option>
                </select>
            </div>

            <!-- content input tag -->
            <div class="col-sm-6 my-1">
                <label for="content" class="sr-only">content</label>
                <input type="text" name="content" id="content" class="form-control" placeholder="Feels like...">
            </div>

            <!-- image/file input tag -->
            <div class="col-sm-4 my-1 input-group">
                <div class="input-group-prepend">
                    <span class="input-group-text">
                        Upload
                    </span>
                </div>
                <div class="custom-file">
                    <label for="image" class="custom-file-label">Choose image</label>
                    <input type="file" id="image" name="image" class="custom-file-input" accept="image/*">
                </div>
            </div>

            <!--  submit button -->
            <div class="col-auto my-1">
                <button type="submit" class="btn btn-primary">submit</button>
            </div>
        </div>
    </form>
</header>
```



---

### 랜덤이미지 넣기

**list.html**

```html
<a href="{% url 'sns:posting_detail' posting.id %}">
    {#                    이미지가 없을 때 #}
    {% if posting.image %}
    <img src="{{ posting.image_thumbnail.url }}" alt="{{ posting.image }}"
         class="card-img-top image-fluid">
    {% else %}
    <img src="https://picsum.photos/32{{ forloop.counter }}/580/?random"
         alt="random_image_{{ forloop.counter }}"
         class="card-img-top image-fluid">
    {% endif %}
</a>
```

**detail.html**

```html
{% if posting.image %}
<img src="{{ posting.image.url }}" alt="{{ posting.image }}"
     class="card-img-top image-fluid">
{% else %}
<img src="https://picsum.photos/960/580/?random"
     alt="random_image"
     class="card-img-top image-fluid">
{% endif %}
```

---



---

**fontawesome**

**base.html**

```html
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
```

**_forms.html**

```html
<select name="icon" id="icon" class="custom-select mr-sm-2">
    <option value="fas fa-question">?</option>
    <option value="far fa-smile">:)</option>
    <option value="far fa-angry">:(</option>
    <option value="far fa-smile-wink">;)</option>
    <option value="fab fa-angrycreative">angrycreative</option>
</select>
```

**sns/models.py** 수정

```python
icon = models.CharField(max_length=20, default='fas fa-question')
```

**detail.py**  17번라인 수정

```html
<i class="{{ posting.icon }}"></i>
```

**list.py** 22번라인 수정

```html
<i class="{{ posting.icon }} fa-2x"></i>
```

**db 삭제하고 다시 만들기**

`$ python manage.py migrate sns zero`

`$ rm -rf media/`

`$ python manage.py migrate`

![1552380486611](../typora-user-images/1552380486611.png)

---



---

**navbar active 효과**

**base.html**

```html
<ul class="nav nav-tabs">
    <li class="nav-item">
        <a class="nav-link {% block is_list %}{% endblock %}" href="{% url 'sns:posting_list' %}" >SNS</a>
    </li>
    <li class="nav-item">
        <a class="nav-link {% block is_detail %}{% endblock %}" aria-disabled="true">Posting</a>
    </li>
</ul>
```

**detail.html**

```html
{% block is_detail %}
    active
{% endblock %}
```

**list.html**

```html
{% block is_list %}
    active
{% endblock %}
```



![1552380696834](../typora-user-images/1552380696834.png)

![1552380702922](../typora-user-images/1552380702922.png)