## 1 db 생성

`sqlite3 blog.db`

`CREATE TABLE articles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    author TEXT
    );`



**app.py**

```python
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# 글 목록
@app.route('/articles')
def index():
    db = sqlite3.connect('blog.db')
    c = db.cursor()

    sql = "SELECT * FROM articles;"
    c.execute(sql)
    articles = c.fetchall()
    
    return render_template('index.html', articles = articles)
  
# 글 쓰기 폼
@app.route("/articles/new/")
def new():
    return render_template('new.html')

# 글 등록
@app.route('/articles/create')
def create():
    title = request.args.get('title')
    author = request.args.get('author')
    content = request.args.get('content')
    
    db = sqlite3.connect('blog.db') 

    c = db.cursor()
    
    sql = "INSERT INTO articles (title, author, content) VALUES ('{}', '{}','{}')".format(title,author,content)
    c.execute(sql)
    
    db.commit()
    
    return redirect('/articles')
 
# 글 상세페이지   
@app.route("/articles/<int:article_id>")
def detail(article_id):
    db = sqlite3.connect('blog.db') 
    c = db.cursor()

    sql = "SELECT * FROM articles WHERE id = {} ".format(article_id)
    c.execute(sql)
    article = c.fetchone()
    
    db.commit()
    return render_template('detail.html', article = article)
    
# 글 수정 폼
@app.route("/articles/<int:article_id>/edit")
def edit(article_id):
    
    db = sqlite3.connect('blog.db')
    c = db.cursor()

    sql = "SELECT * FROM articles WHERE id = {} ".format(article_id)
    c.execute(sql)
    
    article = c.fetchone()
    return render_template('edit.html', article = article)
    
# 글 수정!
@app.route("/articles/<int:article_id>/update")
def update(article_id):
    db = sqlite3.connect('blog.db')
    c = db.cursor()

    title = request.args.get('title')
    content = request.args.get('content')
    author = request.args.get('author')

    sql = "UPDATE articles SET title = '{}' , content = '{}', author='{}' WHERE id = {} ".format(title,content,author,article_id)
    c.execute(sql)

    db.commit()
    return redirect('/articles')
   
# 글 삭제  
@app.route("/articles/<int:article_id>/delete")
def delete(article_id):
    db = sqlite3.connect('blog.db') # db생성,연결
    c = db.cursor()

    sql = "DELETE FROM articles WHERE id = {} ".format(article_id)
    c.execute(sql)

    db.commit()
    return redirect('/articles')
    

```



**index.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <!-- 합쳐지고 최소화된 최신 CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <!-- 부가적인 테마 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">
    <!-- 합쳐지고 최소화된 최신 자바스크립트 -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
    <title>글 목록</title>
</head>
<body>
    <h1>글목록</h1>
    <a href="/articles/new/"><button type="button" class="btn btn-success">새글등록</button></a>
    <br><br>
    <ul class="list-group">
    {% for a in articles %}
       <li class="list-group-item">
          <p>
              <a href="/articles/{{ a[0] }}">제목 : {{ a[1] }}</a>
          </p>
       </li><br>
    {% endfor %}
    </ul>
</body>
</html>
```



**new.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <!-- 합쳐지고 최소화된 최신 CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <!-- 부가적인 테마 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">
    <!-- 합쳐지고 최소화된 최신 자바스크립트 -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
    <title> 글등록 </title>
</head>
<body>
    <h1>새 글 등록</h1>
    
    <form action="/articles/create">
      <div class="form-group">
        <label for="exampleFormControlInput1">제목</label>
        <input type="text" class="form-control" name="title" placeholder="제목을 입력하세요">
      </div>
     <div class="form-group">
        <label for="exampleFormControlInput1">작성자</label>
        <input type="text" class="form-control" name="author" placeholder="작성자를 입력하세요">
      </div>
      <div class="form-group">
        <label for="exampleFormControlTextarea1">내용</label>
        <textarea class="form-control" rows="3" name="content"></textarea>
      </div>
      <input type="submit" value="Submit" class="btn btn-outline-dark"/>
        <a href="/articles">
            <button type="button" class="btn btn-outline-dark">작성취소</button>
        </a>
    </form>
</body>
</html>
```



**detail.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <!-- 합쳐지고 최소화된 최신 CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <!-- 부가적인 테마 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">
    <!-- 합쳐지고 최소화된 최신 자바스크립트 -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
    <title>Document</title>
</head>
<body>
    <ul class="list-group">
      <li class="list-group-item disabled">글번호 : {{article[0]}}</li>
      <li class="list-group-item">제목 : {{article[1]}}</li>
      <li class="list-group-item">글쓴이 : {{article[4]}}</li>
      <li class="list-group-item">작성일 : {{article[3]}}</li>
      <li class="list-group-item">내용 : {{article[2]}}</li>
    </ul>
    
    <a href="/articles">
        <button type="button" class="btn btn-outline-dark">글목록</button>
    </a>
    <a href="/articles/{{article[0]}}/edit">
        <button type="button" class="btn btn-outline-dark">수정</button>
    </a>
    <a href="/articles/{{article[0]}}/delete">
        <button type="button" class="btn btn-outline-dark">삭제</button>
    </a>
</body>
</html>
```



**edit.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <!-- 합쳐지고 최소화된 최신 CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <!-- 부가적인 테마 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">
    <!-- 합쳐지고 최소화된 최신 자바스크립트 -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
    <title> 글등록 </title>
</head>
<body>
    <h1>새 글 등록</h1>
    
    <form action="/articles/{{article[0]}}/update">
      <div class="form-group">
        <label for="exampleFormControlInput1">제목</label>
        <input type="text" class="form-control" name="title" value="{{article[1]}}">
      </div>
     <div class="form-group">
        <label for="exampleFormControlInput1">작성자</label>
        <input type="text" class="form-control" name="author"  value="{{article[4]}}">
      </div>
      <div class="form-group">
        <label for="exampleFormControlTextarea1">내용</label>
        <textarea class="form-control" rows="3" name="content"  placeholder="내용을 입력해주세요">{{article[2]}}</textarea>
      </div>
      <input type="submit" value="Submit" class="btn btn-outline-dark"/>
      <a href="/articles">
        <button type="button" class="btn btn-outline-dark">글목록</button>
      </a>
    </form>
</body>
</html>
```



















