from django.shortcuts import render
import requests
import random
import json
import os
from datetime import datetime
import urllib.request

# Create your views here.
def info(request):
    return render(request, "info.html")
    
def student(request, name):
    age = random.randint(20,30)
    student={"이정은":25, "바보":26, "멍청이": 27, "해삼":28}
    if name in student.keys():
        age = student[name]
        
    return render(request, "student.html", {"name":name, "age":age})

def isval(request):
    an = "아니요"
    today = datetime.now()
    month = today.month
    day = today.day
    if month==2 and day ==14:
        an="예"
    return render(request, "isval.html", {"an":an})
    # return render(request, "isval.html", {"month":month, "day":day})
    
def grad(request):
    # 졸업까지 며칠남음?
    now = datetime.now()
    end = datetime(2019, 5, 19)
    days = end - now
    return render(request, "grad.html", {"days":days.days})
    
def image(request):
    return render(request, "image.html")
    
def index(request):
    return render(request, "index.html")
    
def catch(request):
    message = request.GET.get("message")
    styles=['rounded', 'cosmic', 'gothic', 'alligator']
    style = random.choice(styles)
    url = "http://artii.herokuapp.com/make?text={}&font={}".format(message, style)
    result = requests.get(url).text
    return render(request, "catch.html", {"message":result})
    
def translate(request):
    return render(request, "translate.html")

def result(request):
    message = request.GET.get("word")
    
    naver_id = os.getenv('NAVER_ID')
    naver_secret = os.getenv('NAVER_SECRET')
    
    url = "https://openapi.naver.com/v1/papago/n2mt"
    
    headers = {
        'X-Naver-Client-Id': naver_id ,
        'X-Naver-Client-Secret': naver_secret
    }
    
    data = {
        'source': 'ko',
        'target': 'en',
        'text': message
    }
    
    result = requests.post(url, headers=headers, data=data).text
    result = json.loads(result)
    word = result["message"]["result"]["translatedText"]

    return render(request, "result.html", {"word":word})
    
    