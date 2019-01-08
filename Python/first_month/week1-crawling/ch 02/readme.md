# 2018-12-18  01

### **랜덤 점심 메뉴**

```python
import random
menu = ["순남시래기","20층","양자강","강남목장","시골집","몰라"]
menu_detail = {"순남시래기" : "시래기국, 보쌈", "20층" : "오늘메뉴",
               "양자강" : "차돌짬뽕", "강남목장" : "뚝불",
               "시골집" : "쌈밥정식", "몰라" : "아무거나"}
# () brackets
# {} curly brackets 
# [] square brackets 
# <> angle brackets 
lunch = random.choice(menu)
print(lunch + "에서는 " + menu_detail[lunch] + "이(가) 먹을만 합니다.")
```

### **미세먼지**

```python
import requests
from bs4 import BeautifulSoup

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=%EC%84%9C%EC%9A%B8&ServiceKey={}&ver=1.3&pageNo=3'.format(key)
response = requests.get(url).text
#print(response)
soup = BeautifulSoup(response, 'xml')
#print(soup)
gn = soup('item')[7]
#print(gn)
location = gn.stationName.text
time = gn.dataTime.text
dust = int(gn.pm10Value.text)

print('{0} 기준: 서울시 {1}의 미세먼지 농도는 {2} 입니다.'.format(time, location, dust))

#조건문
if(dust > 150):
  condition = "매우 나쁨"
elif(dust > 80 and dust <= 150):
  # 80 < dust <= 150 가능
  condition = "나쁨"
elif(dust > 50 and dust <= 80):
  condition = "보통"
else: 
  condition = "좋음"
print("오늘의 미세먼지 농도는 {0}입니다.".format(condition))
```

### **반복문 기본**

```python
dish = ["삼겹살", "꽃등심", "파스타", "피자", "뚝불", "떡볶이"]

# 1. for문을 이용해 dish에 담겨있는 모든 음식을 먹는 코드 작성
for food in dish:
  print("{} 먹어야지".format(food))
print("-----")

# 2. while문을 이용해서 dish에 담겨있는 모든 음식을 두번씩 먹는 코드 작성
cnt = 0 
while cnt < 2:
  for food in dish:
    print("{} 먹어야지".format(food))
  cnt += 1
  print("--{0}번--".format(cnt))
  
print("-----------------------------")

for food in dish:
  cnt = 0 
  while cnt < 2:
    print("{} 먹어야지".format(food))
    cnt += 1
```

### **날씨**

```python
import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&APPID="+key
#print(url)
data = requests.get(url).json() # url주소의 값 json형태로 가져오기
# requests => 기능 뭉탱이
# .get => requests가 가진 기능 중 하나 => 또 하나의 기능 뭉탱이 
# .json => 위의 뭉탱이 기능 중 하나
#print(data)
#print(type(data))
#print(data["main"]["temp"])


weather = data['weather'][0]['description']
temp = float(data['main']['temp'])-273.15
temp_min = float(data['main']['temp_min'])-273.15
temp_max = float(data['main']['temp_max'])-273.15
wind = data['wind']['speed']
visibility = data['visibility']

print("""서울의 오늘 날씨는 [{}] 이며, 섭씨 {:.1f}도 입니다.
최저/최고 온도는 {:.1f}/{:.1f}도 입니다.
풍속은 {:.1f}m/s이며, 가시성은 {}m입니다.
""".format(weather, temp, temp_min, temp_max, wind, visibility)
)
```



### **로또**

```python
import random

# 1~45 numbers배열 - python  make long array / make number array
# numbers에서 숫자 6개 랜덤으로 뽑아 - 비복원추출
# 랜덤으로 뽑은 숫자들을 lotto변수에 담고 출력
# 추가 : 로또 변수에 담겨있는 숫자들을 오름차순으로 정렬 
numbers = list(range(1,46))
lotto = random.sample(numbers,6)
print (sorted(lotto))
      
# 1~45 numbers배열 - python  make long array / make number array
# 1 
lotto = []
for i in range(45):
  lotto.append(i+1)
print(lotto)
# 2
lotto2 = list(range(1,46))
print(lotto2)


```



### **다음 코스피**

![1545097131662](..\typora-user-images\1545097131662.png)

![1545097148817](..\typora-user-images\1545097148817.png)

#boxIndexes > div:nth-child(1) > span.num.down > strong

javascript로 data를 보내기 때문에 다른 url에 요청해야함

![1545097610660](..\typora-user-images\1545097610660.png)









### **로또**

string -> int : google- python conver String into int

int 비교 : python check array same (value)

값 비교 : python check array...

https://m.dhlottery.co.kr/common.do?method=main

```python
import random
import requests
from bs4 import BeautifulSoup as bs

# -------------------------랜덤 번호 추첨 ---------------------------
# 1~45 numbers배열 - python  make long array / make number array
# numbers에서 숫자 6개 랜덤으로 뽑아 - 비복원추출
# 랜덤으로 뽑은 숫자들을 lotto변수에 담고 출력
# 추가 : 로또 변수에 담겨있는 숫자들을 오름차순으로 정렬 
numbers = list(range(1,46))
lotto = random.sample(numbers,6)
print ("로또 추천 번호는 {} 입니다.". format(sorted(lotto)))

# --------------------------------------------------------------------


# -------------------------지난 주 당첨 번호--------------------------
url = 'https://m.dhlottery.co.kr/common.do?method=main'
response = requests.get(url).text
soup = bs(response, 'html.parser')

document = soup.select('.prizeresult')[0]
inum = document.select('span')

ns=[]
for number in inum :
  ns.append(int(number.text))
  
print ("저번주 당첨 번호는 {} 입니다.". format(sorted(ns)))
# --------------------------------------------------------------------


# ---------------추천 번호 & 지난 주 당첨 번호 비교-------------------
# 1번
count = 0
for num in ns:
  for l in lotto:
    if(l == num):
      count+= 1
         
print(count)

# 2번
count2 = 0 
for num in ns:
  if num in lotto:
    count2 += 1
print(count2)



# --------------------------------------------------------------------

```



#### [ 네이버웹툰 크롤링]

![1545111981712](..\typora-user-images\1545111981712.png)

```python
import requests
import time
from bs4 import BeautifulSoup as bs

today = time.strftime("%a").lower()
print(today)
# 1. 네이버 웹툰을 가져올 수 있는 주소를(url)파악하고, 변수에 저장
# 2. 해당 주소로 요청을 보내 정보 가져온다
# 3. 받은 정보를 bs를 이용해 검색하기 좋게 만든다.
# 4. 네이버 웹툰 페이지로 가서, 내가 원하는 정보가 어디에 있는지 파악
# 5. 3번에서 저장한 문서를 이용해 4번에서 파악한 위치를 뽑아내는 코드 작성
# 6. 출력

naver_url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=' + today
response = requests.get(naver_url).text
soup = bs(response, 'html.parser')

# 강사님 코드
toons =  []
li = soup.select('.img_list li')
for item in li:
  toon = {
    # "title" : item.select('dt a')[0].text,    # 아래와 같은 코드
    "title" : item.select_one('dt a').text,
    "url" : "https://comic.naver.com/" + item.select('dt a')[0]["href"],
    "img_ul" : item.select('.thumb img')[0]["src"]
  }
  toons.append(toon)
print (toons)
  
# 내 코드
document = soup.select('.img_list li')
#for i in range(32):
for i in range(len(document)):
  #print(document)
  title = document[i].find('dt').find('a')["title"]
  link = document[i].find('a')['href']
  picture = document[i].find('a').find('img')["src"]
  i += 1
  print(title)
  print("https://comic.naver.com"+link)
  print(picture)
  print("-------------------------------------------------------------------------------")



```





#### [ 다음 웹툰 크롤링]

json 형식 보기 : json formatter

![1545117124059](..\typora-user-images\1545117124059.png)

![1545118236864](..\typora-user-images\1545118236864.png)

**Network - slow 3G 로 가져올값이 있는 url 확인**

google : python parse json into dict

![json데이터 dict으로 가져오기](..\typora-user-images\1545118437513.png)

```python
import requests
import time
import json
from bs4 import BeautifulSoup as bs

# 1. 내가 원하는 정보를 얻을 수 있는 주소를 url 변수에 담는다.
# 2. 해당 url에 요청을 보내 응답을 받아 저장한다.
# 3. python으로 json을 파싱(딕셔너리 형으로 변환)해 가져오는 법

url = 'http://webtoon.daum.net/data/pc/webtoon/list_serialized/tue?timeStamp=1545117404316'
response = requests.get(url).text
#print(type(response))
print(response)
document = json.loads(response)
#print(type(document))

data = document["data"]

for toon in data:
  print(toon["title"])
  print(toon["pcThumbnailImage"]["url"])
  print("http://webtoon.daum.net/webtoon/view/{}".format(toon["nickname"]))


```

















