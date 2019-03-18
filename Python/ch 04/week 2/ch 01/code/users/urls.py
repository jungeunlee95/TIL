from django.urls import path
from . import views

app_name = 'users'
# '/users/' => 홈페이지
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout")
]