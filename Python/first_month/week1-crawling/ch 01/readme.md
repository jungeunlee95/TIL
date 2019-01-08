# 2018-12-17

## TYPORA 작성법

- 카카오톡 챗봇 친구 추가
  - @sspy-003 검색하기
    - 친구추가	

1. '미세먼지'를 입력하면 강남구의 미세먼지 농도를 알 수 있다.
   1. '미세먼지'는 미세먼지, '날씨'는 날씨를 알 수 있다.



코드블럭 : ``

`hello`

한줄 코드 블럭 : ```사용 언어

*app.py*  -> 밑의 코드는 이 파일에 넣어

```python
# app.py  -> 저장 파일 이름
hi="하이하이"
a = 0
while a < 5:
  print(hi)
  a+=1
```

```javascript
function(){
}
```



굵게 :  **bold**

링크 : [링크](https://www.naver.com)   => ctrl + click

이미지:

![그냥캡쳐](..\typora-user-images\1545021638497.png)



예외 : >

이것은 문서입니다.  

> 문서가 아닐수고 있습니다.



본문 -  표

| 안에 | 글자 | 정렬 | 가능 |
| ---- | ---- | ---- | ---- |
| 1    | 2    | 3    | 4    |



- **Chocolatey 설치**

  cmd 관리자 명령으로 실행-> cmd에 붙여넣기
  https://github.com/sspy2/set_python_window 

  @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin" 

 	 refreshenv 

  	 choco install git -y



- **git bash 설치**

  -> google -> git for windows -> git bash 설치 -> 실행

  cd 

  cd Documents/

  mkdir week2

  cd week2

  mkdir

  cd day1

  touch readme.md


- github - new repository

  git init

  git add .

  git config --global user.email "이메일주소"

  git config --global user.name "이름"

  git commit -m "first commit"     //버전이 하나 만들어 진 것 : first commit이란 이름으로 git에 저장

  --> git에 업로드

  git remote add origin https://github.com/jungeunlee95/ssafy_001.git

  git push -u origin master

  로그인

  -------업로드 성공----------

  - github 수정하기 (git status : 상태확인 / git diff : 어디 수정했는지)

    git add .

    git commit -m "second commit"  

    git push

    수정 성공!


# 2018/12/17

### python 기초

- 괄호 읽기

  () - brackets
  {} - curly brackets 
  [] - square brackets 
  <> - angle brackets 

- **&&, &, ||, | 차이**

  &&, || : 앞 조건이 맞으면 뒤의 값을 보지 않음

  &, | : 무조건 앞, 뒤의 값을 봄



- **API(Application Programming Interface)**



  - 날씨

  ```python
  import requests
  
  url = "https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&APPID="+key
  print(url)
  
  data = requests.get(url).json() # url주소의 값 json형태로 가져오기
  # requests => 기능 뭉탱이
  # .get => requests가 가진 기능 중 하나 => 또 하나의 기능 뭉탱이 
  # .json => 위의 뭉탱이 기능 중 하나
  #print(data)
  #print(type(data))
  
  weather = data['weather'][0]['description']
  temp = float(data['main']['temp'])-273.15 # 절대온도에서 -273.15
  temp_min = float(data['main']['temp_min'])-273.15
  temp_max = float(data['main']['temp_max'])-273.15
  wind = data['wind']['speed']
  visibility = data['visibility']
  
  print("""서울의 오늘 날씨는 [{}] 이며, 섭씨 {:.1f}도 입니다.
  최저/최고 온도는 {:.1f}/{:.1f}도 입니다.
  풍속은 {:.1f}m/s이며, 가시성은 {}m입니다.
  """.format(weather, temp, temp_min, temp_max)
  )
  ```

  ​     ->**data**

  ```python
  data = {'coord': 
   {'lon': 126.98, 'lat': 37.57},
   'weather': [{'id': 721, 'main': 'Haze', 'description': '연무', 'icon': '50d'}],
   'base': 'stations',
   'main': {'temp': 279.11, 'pressure': 1018, 'humidity': 30, 'temp_min': 278.15, 'temp_max': 279.95},
   'visibility': 10000, 
   'wind': {'speed': 3.1, 'deg': 280},
   'clouds': {'all': 0},
   'dt': 1545026400, 
   'sys': {'type': 1, 'id': 8105, 'message': 0.0065, 'country': 'KR', 'sunrise': 1545000046, 'sunset': 1545034526}, 
   'id': 1835848, 
   'name': 'Seoul', 
   'cod': 200}
  
  # 위에서 "연무" 찾기
  print(data["weather"])
  # [{'id': 721, 'main': 'Haze', 'description': '연무', 'icon': '50d'}]
  #  -> 배열에 감싸져 있음
  
  print(data["weather"][0])
  # {'id': 721, 'main': 'Haze', 'description': '연무', 'icon': '50d'}
  
  print(data["weather"][0]["description"])
  # 연무
  ```



- Random

  - random.choice : 임의의 값 1개, 

    random.sample(a, 3) :	a에서 임의의 값 3개

    **점심메뉴**

    ```python
    import random
    menu = ["순남시래기","20층","양자강","강남목장","시골집"]
    menu_detail = {"순남시래기" : "시래기국, 보쌈", "20층" : "오늘메뉴",
                   "양자강" : "차돌짬뽕", "강남목장" : "뚝불",
                   "시골집" : "쌈밥정식"}
    lunch = random.choice(menu)
    print(lunch + "에서는 " + menu_detail[lunch] + "가 먹을만 합니다.")
    ```






- python 다운

3.6.7버전

[Windows x86-64 executable installer](https://www.python.org/ftp/python/3.6.7/python-3.6.7-amd64.exe) 다운

![1545036113237](..\typora-user-images\1545036113237.png)

- vscode 다운

https://code.visualstudio.com/





path 확인

![1545036306560](..\typora-user-images\1545036306560.png)

내PC 우클릭 -> 속성->설정변경->고급->환경변수

--재시작--



- git dash - python -V 하면 버전나옴