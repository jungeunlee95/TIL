[TOC]

# AWS Lambda 공통 라이브러리 관리

### [1] Layer 만들기

![1578734818219](assets/1578734818219.png)

#### file upload

![1578734957443](assets/1578734957443.png)



<br>

### [2] create function

![1578734574045](assets/1578734574045.png)

<br>

### [3] add Layer to function

![1578735004778](assets/1578735004778.png)

![1578735061064](assets/1578735061064.png)



<br>

### [4] 실행 (ERROR)

```python
import json
import urllib.request
from bs4 import BeautifulSoup


def lambda_handler(event, context):
    url = "https://www.naver.com"
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
    
    a_tags = soup.find_all('a')
    
    result_list = []
    
    for i in a_tags:
        result_list.append(i.get_text())
        
    return {
        'statusCode': 200,
        'body': json.dumps(result_list)
    }
```

```
Response:
{
  "errorMessage": "Unable to import module 'lambda_function'"
}
```

> 이유. bs4를 그냥 압축하면 안되고 최상위 폴더가 `Library/python/`인 경로로 압축을 해줘야함

![1578735248703](assets/1578735248703.png)

![1578735269255](assets/1578735269255.png)

<br>

### [5] Layer Version 추가

![1578735333531](assets/1578735333531.png)

![1578735376409](assets/1578735376409.png)

<br>

### [6] retry

![1578735410545](assets/1578735410545.png)

![1578735436357](assets/1578735436357.png)



