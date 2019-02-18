from django.shortcuts import render
from faker import Faker
# from pastlife.models import Job #현재 같은 레벨에 있음
from .models import Job
import os
import requests
import json

# Create your views here.
def index(request):
    return render(request, 'pastlife/index.html')
    
def pastlife(request):
    # 이름을 받아, faker를 통해 가짜 데이터를 만들어 같이 보냄!
    name = request.GET.get('name')
    
    # 만약 해당 이름이 DB에 저장되어 있다면, 그 직업을 가져옴
    # (DB에서 해당 이름의 레코드가 있는지 찾아본다)!
    # 없으면, faker를 통해 DB에 추가하고, 그 값을 가져옴
    
    person = Job.objects.filter(name=name).first() # 칼럼name = 받은값name 인지 # 아래 코드와 같음!
    # person = Job.objects.get(name=name)
    if person : # None이 아니면,
        job = person.job
    else:
        job = Faker('ko_KR').job()
        new_person = Job(name=name, job=job)
        new_person.save()
     
    # gif
    GIPHY_KEY = os.getenv('GIPHY_KEY')
    
    url = "http://api.giphy.com/v1/gifs/search?api_key={}&q={}&limit=1&lang=ko".format(GIPHY_KEY,job)
    response = requests.get(url).json()
    img_url = response.get("data")[0].get("images").get("original").get("url")
    
    context =  {"name":name, "job":job, "img_url":img_url}
    
    return render(request, 'pastlife/pastlife.html', context)