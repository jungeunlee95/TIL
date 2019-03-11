from django.urls import path
from . import views    # 현재폴더의 views 파일

urlpatterns = [
    path('info/', views.info),
    path('student/<str:name>', views.student),
    path('isval/', views.isval),
    path('grad/', views.grad),
    path('image/', views.image),
    path('', views.index),
    path('catch/', views.catch),
    path('translate/', views.translate),
    path('result/', views.result),
]