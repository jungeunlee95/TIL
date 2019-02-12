from django.shortcuts import render
import random
import math

# Create your views here.
def index(request):
    return render(request, "index.html")
    
    
def lotto(request):
    lucky = random.sample(range(1, 46), 6)
    return render(request, "lotto.html", {"lucky": lucky})
    
def hello(request, name):
    return render(request, "hello.html", {"name" : name })
    
def dinner(request):
    menu = ['짜장면','김치찌개','비빔밥','불고기','굶기']
    a = random.choice(menu)
    return render(request, "dinner.html", {"menu" : a})

def reverse(request, word):
    return render(request, "reverse.html", {"word" : word[::-1]})
    
def sqrt(request, num):
    a = math.sqrt(num)
    return render(request, "sqrt.html", {"num" : a})
    