[TOC]

# AWS Lambda 사용

### [1] function 만들기

![1578730435261](assets/1578730435261.png)

> create function 클릭

<br>

![1578730497146](assets/1578730497146.png)

> 보통 node.js, python으로 많이 생성함

<br>

---

### [2] 확인

![1578730547558](assets/1578730547558.png)

> Add trigger > 이벤트가 발생했을 때 
>
> Add destination > 처리

<br>

---

### [3] function code 작성

> trigger를 통해 이벤트 함수로 발생
>
> ```python
> import json
> 
> def lambda_handler(event, context):
>     # 이벤트가 발생하면 무조건 아래의 메세지 return
>     return {
>         'statusCode': 200,
>         'body': json.dumps('Hello Lambda!')
>     }
> ```

![1578730700255](assets/1578730700255.png)

<br>

---

### [4] Trigger 추가

![1578730774319](assets/1578730774319.png)

<br>

### [5] Trigger 확인

![1578730800337](assets/1578730800337.png)

<br>

---

### [6] API 확인

![1578730817674](assets/1578730817674.png)









