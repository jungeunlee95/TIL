from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3' # db or sqlite3
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db만들기---------------------------------------------------------
db = SQLAlchemy(app)

db.init_app(app)  # 데이터 베이스 시작하고 추가

# 위의 스키마와 같은 테이블 orm으로 만들기
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
    
    def __str__(self):
        return "제목:{}, 영어제목:{}, 관객수:{}, 개봉일:{},장르:{},관람등급:{},평점:{},포스트:{},설명:{}".format(self.id, self.title, self.title_en, self.audience, self.open_date, self.genre, self.watch_grade, self.score, self.poster_url, self.description)
        
db.create_all()  # 위의 테이블 만들어라 
# ------------------------------------------------------------------
# select * 
@app.route('/movies')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies = movies)
    
# 영화 생성 폼
@app.route('/movies/new')
def new():
    return render_template("new.html")
    
# insert
@app.route('/movies/create')
def create():
    title = request.args.get("title")
    title_en = request.args.get("title_en")
    audience = request.args.get("audience")
    open_date = request.args.get("open_date")
    genre = request.args.get("genre")
    watch_grade = request.args.get("watch_grade")
    score = request.args.get("score")
    poster_url = request.args.get("poster_url")
    description = request.args.get("description")
    
    # ORM을 사용해 새로운 Article 객체 만들어 DB에 저장
    a = Movie(title=title,title_en=title_en, audience=audience, open_date=open_date, genre=genre, watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
    db.session.add(a)
    db.session.commit()
    return redirect("/movies")
    
# detail  
@app.route('/movies/<int:movie_id>')
def detail(movie_id):
    a = Movie.query.filter_by(id=movie_id).first()

    return render_template('show.html', a= a)
    
# delete  
@app.route('/movies/<int:movie_id>/delete')
def delete(movie_id):
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect("/movies")
    
# edit  
@app.route('/movies/<int:movie_id>/edit')
def edit(movie_id):
    a = Movie.query.get(movie_id)
    return render_template('edit.html', a= a)
    
# update  
@app.route('/movies/<int:movie_id>/update')
def update(movie_id):
    title = request.args.get("title")
    title_en = request.args.get("title_en")
    audience = request.args.get("audience")
    open_date = request.args.get("open_date")
    genre = request.args.get("genre")
    watch_grade = request.args.get("watch_grade")
    score = request.args.get("score")
    poster_url = request.args.get("poster_url")
    description = request.args.get("description")
    
    a = Movie.query.get(movie_id)
    a.title = title
    a.title_en = title_en
    a.audience = audience
    a.open_date = open_date
    a.genre = genre
    a.watch_grade = watch_grade
    a.score = score
    a.poster_url = poster_url
    a.description = description
    db.session.commit()

    return redirect("/movies/{}".format(movie_id))