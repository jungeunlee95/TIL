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