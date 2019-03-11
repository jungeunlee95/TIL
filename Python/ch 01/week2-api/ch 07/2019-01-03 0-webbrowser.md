# 2019-01-03 0-webbrowser

**git bash**

```
$ mkdir git_practice
$ cd git_practice
$ code .
-> 프로젝트에 new file : browser.py
```

**browser.py**

```python
import webbrowser

# 1. 사용자 입력 받아 검색하는 코드
# url = "https://search.daum.net/search?q=" 
# keyword = input("검색어 입력 : ")
# webbrowser.open(url + keyword)

# 여러 검색 페이지를 한 번에 여는 코드
url = "https://search.daum.net/search?q=" 
menu = ["피자", "파스타", "떡볶이", "케이크", "마카롱", "사탕"]
for food in menu :
    webbrowser.open(url + food)



```

