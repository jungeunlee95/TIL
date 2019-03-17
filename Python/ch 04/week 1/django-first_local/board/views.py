from django.shortcuts import render, redirect, get_object_or_404
from .models import Article,Comment
from IPython import embed

# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html', {
        'articles':articles,
    })

def article_detail(request, article_id):
    # 값이 없을 때 404 error!
    article = get_object_or_404(Article, id=article_id)
    comments = article.comment_set.all()
    return render(request, 'board/detail.html', {
        'article':article,
        'comments':comments,
    })

# def new_article(request):
#     return render(request, 'board/new.html')

def create_article(request):
    if request.method=='GET':
        return render(request,'board/new.html')
    elif request.method=='POST':
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('board:article_detail', article.id)

def update_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method=='GET':
        return render(request,'board/edit.html', {
            'article':article,
        })
    else:
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('board:article_detail', article.id)

def delete_article(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(Article, id=article_id)
        article.delete()
    return redirect('board:article_list')

# 댓글부분!
def create_comment(request, article_id):
    if request.method == 'POST':
        comment = Comment()
        # 이 댓글의 글은 이 글이야
        comment.article = get_object_or_404(Article, id=article_id)
        comment.content = request.POST.get('comment')
        comment.save()
    return redirect('board:article_detail', article_id)

def delete_comment(request, article_id, comment_id):
    # article = get_object_or_404(Article, article_id)
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
    return redirect('board:article_detail', article_id)