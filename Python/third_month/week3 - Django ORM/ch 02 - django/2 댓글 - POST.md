**django docs :** https://docs.djangoproject.com/en/2.1/ref/csrf/

> POST 
>
> client -> server에 form에 data를 담아 요청을 보낼 때, token을 함께 보내야함.



>## POST를 쓰는 이유,
>
> GET을 사용하면 누구나 쉽게 사이트에 데이터를 넣을 수 있음
>
>ex )
>
>```python
>import requests
>from time import sleep
>
>content="사이트 접속 안하고 댓글 남기기"
>url = 댓글 남기는 url
>
>while True:
>    sleep(10)  # 10초에 한번씩 수행
>    requests.get(url) # 댓글 계속 남겨짐
>```



**detail.html**  {% csrf_token %}

```html
<form action="/articles/{{article.id}}/comment/" method="POST">
      {% csrf_token %}
      <input type="text" name="content" placeholder="댓글"/>
      <input type="text" name="author" placeholder="작성자"/>
      <input type="submit" class="btn btn-warning" value="댓글쓰기"/>
</form>
```

**views.py ** request.POST.get(' ')

```python
def comment(request, aid):
    content = request.POST.get('content')
    author = request.POST.get('author')
    
    comment = Comment(author=author, content=content, article_id=aid)
    comment.save()
    
    return redirect('articles:detail', aid=aid)
```



> ## CSRF 토큰도 받아와서 댓글달기,
>
> ex )
>
> ```python
> import requests
> from time import sleep
> 
> content = "사이트 접속 안하고 댓글 남기기"
> author = "작성자"
> url = f"http://first-django-juneun.c9users.io:8080/articles/30/comment/?content={content}&author={author}"
> 
> while True:
>  sleep(10)  # 10초에 한번씩 수행
>  # 이 식으로 csrf토큰 가져와서 같이 보내기
>  requests.get(url) # 댓글 계속 남겨짐
>     
>     
> # csrf_token 가져오기
> res = requests.get('http://first-django-juneun.c9users.io:8080/articles/31/').text
> data = bs(res, 'html.parser')
> csrfmiddlewaretoken = data.find_all("input")[0].get("value")
> 
> params = {
>     'content' : "메로롱",
>     'author' : "메롱",
>     'csrfmiddlewaretoken' : csrfmiddlewaretoken
> }
> 
> url = "http://first-django-juneun.c9users.io:8080/articles/31/comment/"
> print(requests.post(url=url, data=params) )
> ```



