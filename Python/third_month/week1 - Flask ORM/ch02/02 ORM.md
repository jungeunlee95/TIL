# ORM

`$ sudo pip3 install flask`

`$ sudo pip3 install flask-sqlalchemy`

` $ flask run --host=0.0.0.0 --port=8080`

```python
print(app.config)

<Config {'SQLALCHEMY_BINDS': None, 'SQLALCHEMY_POOL_SIZE': None, 'SQLALCHEMY_POOL_RECYCLE': None, 'SESSION_REFRESH_EACH_REQUEST': True, 'JSON_AS_ASCII': True, 'JSONIFY_MIMETYPE': 'application/json', 'SESSION_COOKIE_PATH': None, 'JSON_SORT_KEYS': True, 'SECRET_KEY': None, 'SESSION_COOKIE_HTTPONLY': True, 'SESSION_COOKIE_DOMAIN': None, 'SQLALCHEMY_RECORD_QUERIES': None, 'SQLALCHEMY_COMMIT_ON_TEARDOWN': False, 'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(0, 43200), 'SESSION_COOKIE_SAMESITE': None, 'SQLALCHEMY_TRACK_MODIFICATIONS': False, 'JSONIFY_PRETTYPRINT_REGULAR': False, 'USE_X_SENDFILE': False, 'DEBUG': False, 'PREFERRED_URL_SCHEME': 'http', 'MAX_CONTENT_LENGTH': None, 'SQLALCHEMY_NATIVE_UNICODE': None, 'SESSION_COOKIE_NAME': 'session', 'TRAP_HTTP_EXCEPTIONS': False, 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 'SQLALCHEMY_DATABASE_URI': 'sqlite:///blog.sqlite3', 'TEMPLATES_AUTO_RELOAD': None, 'TESTING': False, 'SESSION_COOKIE_SECURE': False, 'PROPAGATE_EXCEPTIONS': None, 'MAX_COOKIE_SIZE': 4093, 'TRAP_BAD_REQUEST_ERRORS': None, 'ENV': 'production', 'EXPLAIN_TEMPLATE_LOADING': False, 'SERVER_NAME': None, 'APPLICATION_ROOT': '/', 'SQLALCHEMY_MAX_OVERFLOW': None, 'PRESERVE_CONTEXT_ON_EXCEPTION': None, 'SQLALCHEMY_ECHO': False, 'SQLALCHEMY_POOL_TIMEOUT': None}>

```

---

`__str__`

app.py

```python
 def __str__(self):
        return "글번호: {} , 제목 : {}, 내용 : {}".format(self.id, self.title, self.content)
```

idex.html

```html
   {%for a in articles%}
       <p>{{a}}</p>
   {% endfor %}
```

글번호: 1 , 제목 : hh, 내용 : rr

글번호: 2 , 제목 : hh, 내용 : rr

글번호: 3 , 제목 : gg, 내용 : 22

---

`__repr__`

app.py

```python
    def __repr__(self):
        return "글번호: {} , 제목 : {}, 내용 : {}".format(self.id, self.title, self.content)
```

idex.html

```html
{{articles}}
```

[글번호: 1 , 제목 : hh, 내용 : rr, 글번호: 2 , 제목 : hh, 내용 : rr, 글번호: 3 , 제목 : gg, 내용 : 22]

---



## 기본적인 CRUD

**app.py**

```python
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.sqlite3' # db or sqlite3
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db만들기---------------------------------------------------------
db = SQLAlchemy(app)

db.init_app(app)  # 데이터 베이스 시작하고 추가
'''
CREATE TABLE articles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
''' 
# 위의 스키마와 같은 테이블 orm으로 만들기
class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return "글번호: {} , 제목 : {}, 내용 : {}".format(self.id, self.title, self.content)


db.create_all()  # 위의 테이블 만들어라 
# ------------------------------------------------------------------
# select * 
@app.route('/')
def index():
    articles = Article.query.all()
    
    return render_template('index.html', articles = articles)
    
# insert table
@app.route('/create')
def create():
    title = request.args.get("title")
    content = request.args.get("content")
    
    # ORM을 사용해 새로운 Article 객체 만들어 DB에 저장
    a = Article(title=title, content=content)
    db.session.add(a)
    db.session.commit()
    return redirect("/")
 
# delete  
@app.route('/delete/<int:article_id>')
def delete(article_id):
    article = Article.query.get(article_id)
    db.session.delete(article)
    db.session.commit()
    return redirect("/")
    
# edit  
@app.route('/edit/<int:article_id>')
def edit(article_id):
    a = Article.query.filter_by(id=article_id).first()

    return render_template('edit.html', a= a)
    
# update  
@app.route('/update/<int:article_id>')
def update(article_id):
    title = request.args.get("title")
    content = request.args.get("content")
    
    a = Article.query.get(article_id)
    a.title = title
    a.content = content
    db.session.commit()

    return redirect("/")
```

**edit.html**

```html
...
    <form action="/update/{{a.id}}">
        제목 : <input type="text" name="title" value="{{a.title}}"/>
        내용 : <input type="text" name="content" value="{{a.content}}"/>
        <input type="submit" value="Submit"/>
    </form>
...
```

**index.html**

```html
...
    <form action="/create">
        제목 : <input type="text" name="title"/>
        내용 : <input type="text" name="content"/>
        <input type="submit" value="Submit"/>
    </form>
    {%for a in articles%}
        <p>글번호: {{a.id}}, 제목: {{a.title}}, 내용: {{a.content}}
            <a href="/delete/{{a.id}}">[삭제]</a>
            <a href="/edit/{{a.id}}">[수정]</a>
        </p>
    {% endfor %}
...
```

































