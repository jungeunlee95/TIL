from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/articles/')
def index():
    '''db에 저장된 모든 글들을 보여줄거야'''
    # 1. db에 접속하여
    db = sqlite3.connect('blog.db')
    c = db.cursor()
    
    # 2. 저장된 모든 글들을 가져온다.(fetchall())
    sql = "SELECT * FROM articles;"
    c.execute(sql)
    articles = c.fetchall()
    
    # 3. index.html에 넣어서 보여준다.
    return render_template('index.html', articles = articles)
    
@app.route("/articles/new/")
def new():
    return render_template('new.html')


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
    
@app.route("/articles/<int:article_id>")
def detail(article_id):
    db = sqlite3.connect('blog.db') # db생성,연결
    c = db.cursor()

    sql = "SELECT * FROM articles WHERE id = {} ".format(article_id)
    c.execute(sql)
    article = c.fetchone()
    
    db.commit()
    return render_template('detail.html', article = article)
    
@app.route("/articles/<int:article_id>/edit")
def edit(article_id):
    
    db = sqlite3.connect('blog.db')
    c = db.cursor()

    sql = "SELECT * FROM articles WHERE id = {} ".format(article_id)
    c.execute(sql)
    
    article = c.fetchone()
    return render_template('edit.html', article = article)
    
@app.route("/articles/<int:article_id>/update")
def update(article_id):
    db = sqlite3.connect('blog.db') # db생성,연결
    c = db.cursor()

    title = request.args.get('title')
    content = request.args.get('content')
    author = request.args.get('author')

    sql = "UPDATE articles SET title = '{}' , content = '{}', author='{}' WHERE id = {} ".format(title,content,author,article_id)
    c.execute(sql)

    db.commit()
    return redirect('/articles')
    
@app.route("/articles/<int:article_id>/delete")
def delete(article_id):
    db = sqlite3.connect('blog.db') # db생성,연결
    c = db.cursor()

    sql = "DELETE FROM articles WHERE id = {} ".format(article_id)
    c.execute(sql)

    db.commit()
    return redirect('/articles')
    
