from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.article_list, name='article_list'),                             # 글목록
    # path('new/', views.new_article, name='new_article'),                         # new.html
    path('create/', views.create_article, name='create_article'),                  # 글쓰기

    path('<int:article_id>/', views.article_detail, name='article_detail'),        # detail.html
    # path('<int:article_id>/edit', views.edit_article, name='edit_article'),        # edit.html
    path('<int:article_id>/update/', views.update_article, name='update_article'),  # update
    path('<int:article_id>/delete/', views.delete_article, name='delete_article'),  # delete

    # 댓글
    path('<int:article_id>/create_comment/', views.create_comment, name='create_comment'),
    path('<int:article_id>/delete_comment/<int:comment_id>',
         views.delete_comment,
         name='delete_comment'),
]