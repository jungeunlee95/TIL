from django.urls import path
from . import views 

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:aid>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:aid>/edit/', views.edit, name='edit'),
    path('<int:aid>/update/', views.update, name='update'),
    path('<int:aid>/delete/', views.delete, name='delete'),
]