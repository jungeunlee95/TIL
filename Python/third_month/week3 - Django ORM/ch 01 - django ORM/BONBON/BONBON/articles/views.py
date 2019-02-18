from django.shortcuts import render, redirect
from .models import Article

# /articles          -> 모든 글을 보여주는 곳
# /articles/1        -> 글 상세하게 보는 곳
# /articles/new      -> 새 글 작성
# /articles/create   -> 새 글 저장
# /articles/1/edit   -> 글 편집
# /articles/1/update -> 글 수정
# /articles/1/delete -> 글 삭제 

def index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {"articles":articles})
    
def new(request):
    return render(request, 'articles/new.html')
    
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    article = Article(title=title, content=content)
    article.save()

    # return redirect('articles:detail', aid = article.id)
    return redirect('articles:index')
    
def detail(request, aid):
    article = Article.objects.get(id=aid)
    return render(request, 'articles/detail.html', {"article":article})   
    
def edit(request, aid):
    article = Article.objects.get(id=aid)
    return render(request, 'articles/edit.html', {"article":article}) 
    
def update(request, aid):
    article = Article.objects.get(id=aid)
    article.title = request.GET.get('title')
    article.content = request.GET.get('content')
    article.save()
    
    # return redirect('articles:detail', aid = article.id)
    return redirect('articles:index')
    
def delete(request, aid):
    article = Article.objects.get(id=aid)
    article.delete()
    
    # return redirect('/articles')   
    return redirect('articles:index')
    