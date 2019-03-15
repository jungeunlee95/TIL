from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('create/', views.create_movie, name='create_movie'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_id>/update/', views.update_movie, name='update_movie'),
    path('<int:movie_id>/delete/', views.delete_movie, name='delete_movie'),

    # 평점
    path('<int:movie_id>/scores/new/', views.create_score, name='create_score'),
    path('<int:movie_id>/scores/<int:score_id>/delete/',
         views.delete_score,
         name='delete_score'),
]