from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def qna(request):
    return render(request, 'qna.html')
    
def mypage(request):
    return render(request, 'mypage.html')

def signup(request):
    return render(request, 'signup.html')
    
def page_not_found_page(request, not_found):
    return render(request, '404.html', {"url":not_found})
    
    