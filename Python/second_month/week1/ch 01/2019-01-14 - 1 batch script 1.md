

# 2019-01-14 - batch script

> >  **batch script**
>
> ![1547425720850](..\typora-user-images\1547425720850.png)

![1547426005357](../typora-user-images/1547426005357.png)

---

**hello.bat**

```bat
:: 윈도우즈 커맨드들을 모아 한번에 실행해주는 스크립트 
python c:\Users\student\scripts\hello.py %*
pause
```



![1547426105589](../typora-user-images/1547426105589.png)

> ---
>
> **경로 줄이기 -> 환경변수에 넣기**
>
> ---

### 환경변수설정

![1547426405680](../typora-user-images/1547426405680.png)

![1547426414238](../typora-user-images/1547426414238.png)

![1547426421131](../typora-user-images/1547426421131.png)

​								**>> 환경변수 <<**

![1547426482999](../typora-user-images/1547426482999.png)

​								**>> 편집  <<**



![1547426625948](../typora-user-images/1547426625948.png)

​								**>> 새로만들기<<**

![1547426689501](../typora-user-images/1547426689501.png)

​								**>> 그 경로 추가 <<**

---

​						이제 윈도우 + R 에 bat파일 이름만 치면 됨

---

**hello.py**

```python
# 자동화 할 기능들을 파이썬으로 구현.
import webbrowser

url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%AA%A8%EB%AA%A8%EB%9E%9C%EB%93%9C+%EC%97%B0%EC%9A%B0"
webbrowser.open(url)
```

![1547426762785](../typora-user-images/1547426762785.png)

​								**자동으로 창이 뜸 !**  

---

**bello.bat**

```bat
:: 윈도우즈 커맨드들을 모아 한번에 실행해주는 스크립트 
@python c:\Users\student\scripts\hello.py %*
@pause
:: @를 넣으면 깔끔하게 바뀜

:: %*는 뭐지? 
:: --> arguments, 모든 파라미터는 %* 를 의미
```

![1547427157646](../typora-user-images/1547427157646.png)

​					▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼

![1547427144057](../typora-user-images/1547427144057.png)

---




