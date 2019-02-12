# How To Start Django  

1. 프로젝트 진행 폴더 생성   `mkdir test`
2. 해당 폴더로 이동                `cd test`
3. 가상 환경 설정                    `pyenv virtualenv 3.6.7 test-venv`
4. 현재 위치 가상 환경 시작   `pyenv local test-venv`
5. 가상 환경에 장고 설치	     `pip install django`
6. 현재 폴더에 장고 시작       `django-admin startproject test  .`



**server 실행** :  `python manage.py runserver $IP:$PORT`

**app 만들기** : `python manage.py  startapp {pages}`

지우기

```
rm - rf  
rm manage.py
ls -al

```



pip list 확인 : `pip list`



------

settings.py

`INSTALLED_APPS` 에 app 추가 해줘야함 ! 

