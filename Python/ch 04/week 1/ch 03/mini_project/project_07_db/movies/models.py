from django.db import models

class Genre(models.Model):
    name = models.TextField(default='')

    def __str__(self):
        return f'{self.id}: {self.name[:20]}'

class Movie(models.Model):
    title = models.TextField(default='')
    audience = models.IntegerField(default=0)
    poster_url = models.TextField(default='')
    description = models.TextField(default='')
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}:{self.genre_id.name}'

class Score(models.Model):
    content = models.TextField(default='')
    score = models.IntegerField(default=0)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.score}:{self.content}:{self.movie_id.title}'

