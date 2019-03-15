from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Score, Genre

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/list.html', {
        'movies': movies,
    })

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    scores = movie.score_set.all().order_by('id')

    return render(request, 'movies/detail.html', {
        'movie': movie,
        'scores': scores,
    })

def create_movie(request):
    if request.method=='GET':
        return render(request,'movies/new.html')
    elif request.method=='POST':
        movie = Movie()
        movie.title = request.POST.get('title')
        movie.audience = request.POST.get('audience')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')
        genre_id = request.POST.get('genre_id')
        movie.genre_id = get_object_or_404(Genre, id=genre_id)
        movie.save()
        return redirect('movie:movie_detail', movie.id)

def update_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method=='GET':
        return render(request,'movies/edit.html', {
            'movie': movie,
        })
    else:
        movie.title = request.POST.get('title')
        movie.audience = request.POST.get('audience')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')
        genre_id = request.POST.get('genre_id')
        movie.genre_id = get_object_or_404(Genre, id=genre_id)
        movie.save()
        return redirect('movie:movie_detail', movie.id)

def delete_movie(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()
    return redirect('movie:movie_list')

# 평점
def create_score(request, movie_id):
    if request.method == 'POST':
        score = Score()
        score.movie_id = get_object_or_404(Movie, id=movie_id)
        score.content = request.POST.get('content')
        score.score = request.POST.get('score')
        score.save()
    return redirect('movie:movie_detail', movie_id)

def delete_score(request, movie_id, score_id):
    score = get_object_or_404(Score, id=score_id)
    score.delete()
    return redirect('movie:movie_detail', movie_id)