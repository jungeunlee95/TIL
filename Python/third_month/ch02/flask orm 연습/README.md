# orm 연습

**app.py**

**import**

```python
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
```

**orm 기본 틀**

```python
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
```



**app.py 스키마 Class 만들기** 

```python
class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=True, nullable=False)
    title_en = db.Column(db.String, nullable=False)
    audience = db.Column(db.Integer, nullable=False)
    open_date = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    watch_grade = db.Column(db.String, nullable=False)
    score = db.Column(db.Float, nullable=False)
    poster_url = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
        
db.create_all()  # 위의 테이블 만들어라 
```





## Flask ORM

---

select * from (table) : `클래스이름.query.all()`

---

insert : `a = 클래스이름(컬럼=값, 컬럼=값 ...)`

​	     `    db.session.add(a)`
​	    `db.session.commit()`

---

select ... where =? : `클래스이름.query.filter_by(id=값).first()`

​				or `클래스이름.query.get(값)`

---

delete :  `클래스이름.query.get(값)`

​		`db.session.delete(movie)`

 		`db.session.commit()`

---

update : `a = 클래스이름.query.get(값)`

​		`a.title="바꾸기"`

​		`db.session.commit()`

---





















