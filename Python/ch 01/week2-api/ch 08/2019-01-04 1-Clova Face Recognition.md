# 2019-01-04 1-Clova Face Recognition

https://developers.naver.com/docs/clova/api/CFR/API_Guide.md#UsingAPI

Document -> Clova A.I. APIs -> CFR API 사용하기

## CFR API 사용하기 

CFR API는 REST API이며, 얼굴 인식을 수행할 이미지 데이터를 HTTP 통신으로 음성 합성 서버에 전달하면 됩니다. 음성 합성 서버가 제공하는 REST API의 URI는 다음과 같으며 POST 방식으로 연결을 시도해야 합니다.

```
// 유명인 얼굴 인식 API
https://openapi.naver.com/v1/vision/celebrity

// 얼굴 감지 API
https://openapi.naver.com/v1/vision/face
```

HTTP 요청으로 얼굴 인식을 요청할 때 [사전 준비사항](https://developers.naver.com/docs/clova/api/CFR/API_Guide.md#Preparation)에서 발급받은 **Client ID**와 **Client Secret** 정보를 헤더에 포함시켜야 합니다. 또한 요청을 *multipart* 형식으로 보내야 하며, 메시지의 이름은 `image`여야 합니다. 다음은 유명인 얼굴 인식 API를 호출할 때 보내는 HTTP 요청 메시지 예입니다.

```
[HTTP Request Header]
POST /v1/vision/celebrity HTTP/1.1
Host: openapi.naver.com
Content-Type: multipart/form-data; boundary={boundary-text}
★X-Naver-Client-Id: {앱 등록 시 발급받은 Client ID}★
★X-Naver-Client-Secret: {앱 등록 시 발급 받은 Client Secret}★ 
					★headers에 포함시킬 내용★
Content-Length: 96703

--{boundary-text}
Content-Disposition: form-data; name="image"; filename="test.jpg"
Content-Type: image/jpeg

{image binary data}
--{boundary-text}--
```

HTTP 요청을 통해 보내는 이미지의 포맷에 대한 제약은 없습니다. 다만, **GIF와 같은 이미지 포맷은 첫 번째 프레임의 이미지**를 기준으로 얼굴 인식을 수행합니다.



-> 밑으로 내리면 친절하게 언어별로 사용 방법까지 나와요 ~~



---

		### 						 도전

---



유명인 jpg파일  c9에 업로드 (드래그하면됨)

**face.py** - 파일보내기

```python
# 인식시킬 사진을 Clova API를 통해 요청을 보내, 인식 결과를 받아온다.
# req(파일)   : 파일 데이터 전송 

# 1. requests를 통해 Clova API 주소에 요청을 보낸다.
# 2. 응답 받은 json을 파싱하여 원하는 결과를 출력한다.

import requests
import os 
from pprint import pprint as pp

naver_id = os.getenv('NAVER_ID')
naver_secret = os.getenv('NAVER_SECRET')

url = "https://openapi.naver.com/v1/vision/celebrity"

headers = {
    'X-Naver-Client-Id': naver_id ,
    'X-Naver-Client-Secret': naver_secret
}

files = {
    'image': open('jung.jpg', 'rb')   # open : 파일을 열때 쓰는 함수 = image에 파일을 넣어줌
}

res = requests.post(url, headers=headers, files=files)
result = res.json()

name = result['faces'][0]['celebrity']['value']
percent =  round(result['faces'][0]['celebrity']['confidence']*100)

print("닮은 연예인은 {}입니다.\n{}% 확신할 수 있습니다.".format(name,percent))


```



**face.py** - 이미지 주소로 받아오기

```python
...
print(dir(image_res.raw))
```

- print 결과

```
['CONTENT_DECODERS', 'REDIRECT_STATUSES', '__abstractmethods__', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_abc_cache', '_abc_negative_cache', '_abc_negative_cache_version', '_abc_registry', '_body', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_connection', '_decoder', '_fp', '_original_response', '_pool', 'close', 'closed', 'data', 'decode_content', 'fileno', 'flush', 'from_httplib', 'get_redirect_location', 'getheader', 'getheaders', 'headers', 'isatty', 'read', 'readable', 'readline', 'readlines', 'reason', 'release_conn', 'seek', 'seekable', 'status', 'stream', 'strict', 'tell', 'truncate', 'version', 'writable', 'writelines']
```

- 코드

```python
# 인식시킬 사진을 Clova API를 통해 요청을 보내, 인식 결과를 받아온다.
# req(파일)   : 파일 데이터 전송 

# 1. requests를 통해 Clova API 주소에 요청을 보낸다.
# 2. 응답 받은 json을 파싱하여 원하는 결과를 출력한다.

import requests
import os 
from pprint import pprint as pp

naver_id = os.getenv('NAVER_ID')
naver_secret = os.getenv('NAVER_SECRET')

url = "https://openapi.naver.com/v1/vision/celebrity"

headers = {
    'X-Naver-Client-Id': naver_id ,
    'X-Naver-Client-Secret': naver_secret
}   

# 1. 해당하는 image_url에 요청을 보낸다\
image_url = "http://www.kbstve.com/news/photo/201604/681_616_1746.jpg"
image_res = requests.get(image_url, stream=True)  # 옵션 아는 법 google : python requests 문서 찾아보기
# print(image_res.raw.read())

# 2. 파일 데이터를 받아 저장해둔다
files = {
    #'image': open('momo.jpg', 'rb')   # open : 파일을 열때 쓰는 함수 = image에 파일을 넣어줌
    'image' : image_res.raw.read()
}

res = requests.post(url, headers=headers, files=files)
result = res.json()

name = result['faces'][0]['celebrity']['value']
percent =  round(result['faces'][0]['celebrity']['confidence']*100)

print("닮은 연예인은 {}입니다.\n{}% 확신할 수 있습니다.".format(name,percent))

```

