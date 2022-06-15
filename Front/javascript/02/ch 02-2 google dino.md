[TOC]

---

# 구글 dino 만들기 - 점프 구현

구글 dino 게임은 브라우저에서 space bar로 점프를 뛰는 것이다.

이말인 즉 브라우저가 우리가 어떤 키를 누르는지 인식한다는 뜻이다.

브라우저 리스너를 사용할 것이다.



---

## 0. 추가 도구 설치

우리가 JS에 뭘 추가할 때마다 홈페이지를 새로고침  - 이걸 안 할려고 extension을 하나 깔 거다

vscode market place에서 Live Server라는 것을 install

그리고 괄호마다 색을 칠해줘서 코딩 쉽게 해주는 Bracket Pair Colorizer



이제 index.html 페이지에서 오른쪽 마우스로  open with live server를 눌러서 브라우저 킨다.

이러면 항상 새로고침하여 수정할 필요가 없이, 바로 바로 라이브로 적용된다.

JS 파일을 save하면 바로 적용.



---

## 1. 둘리 이미지 출력

둘리 이미지를 가져와 `<div>` 태그 안에 넣어준다. (png 형식 권장)

감싸고 있는 `<div>` 에 row 클래스 넣어주면 이미지는 알아서 flex가 되지만, 지금은 아니니 display를 flex로 스타일링 해줘야 한다. 그래야 `justify-content` 사용 가능.

vh 는 배율 단위, % 라고 보면 된다. 이걸로 둘리를 높이 가운데로 위치시킨다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Dooly</title>
    <style>
        .bg {
            background-color: #F7F7F7;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
    </style>
</head>
<body>
    <div class="bg">
        <img height="150px" width="150px" src="dooly.png">
    </div>
    <script src="app.js"></script>
</body>
</html>
```



---

## 2. 트릭구조

콘솔에서 document를 치면 소스코드가 나온다.

document.title하면 이 HTML의 title이 나온다.

document.body를 치면 body 태그가 다 나온다.

html 요소를 트리화 해서 모델링? 시킨 것이 다큐먼트 모델이라고 한다.



html 태그가 맨 위에 있고

head, body가 그 아래로 나뉜다.

그리고 그 head 아래에 meta, style 존재.

이런식으로 html을 트리처럼 짤 수 있고 head 찾은 뒤 title 찾고 하는 식의 탐색도 가능하다.



그런데 결국 내부 구현체는 JS object에 불과하다.

파이썬의 딕셔너리 처럼 표현!

```javascript
document = {
    head: {
        style: {
        }
    }
}
```

브라우저가 다루는 형태는 위와 같을 것이다. Document Object Model인 DOM이라고 한다. 중요한 것은 중간 중간에 있는 Object라는 말이다.

background-color 라고 우린 쓰지만, 오브젝트 안에는 backgroundColor!@@#%@#$ 로 키와 값으로 될 듯.

h1 태그에 둘리가 쓰자.

콘솔창에서 `document.body.` 쓰면 여러가지 쓸 수 있는게 목록이 보인다.



Document Object Model 즉 js 가 html 문서를 다루는 패턴??

트리구조도 결국 js의 객체로 구현되어 있다는 것이다. 정말 document라는 것은 많은게 있어서 우리가 명세서를 하나하나 읽어보는 것은 거의 불가능.



우리는 style에서 marginTop 조작하고 결과를 볼 것인데, 이걸 오브젝트로 접근하여 조작할거니 참조.



---

## 3. 둘리 선택하기

무언가가 일어난다. => 얘 혼자 가만히 있는게 아니라 어떤 사건이 그 전에 있다. Trigger가 조건을 만족해야 구동.

그 조건이 마우스 클릭일 수도 있고, 키보드를 누르기 일 수도 있다.



방향키를 눌러서 둘리 이동시켜야 함.

1. 키 누른걸 인식시키기
2. 인식되면 그 방향데로 둘리 움직이기



```javascript
document.querySelector('img') // 이건 별로다. 이미지 한 개만 쓸것도 아니고.
document.querySelector('#dooly') // html에 있는 둘리에게 id 부여
console.log(document.querySelector('#dooly'))
// 이러면 콘솔창에 img 태그가 보인다.
```



---

## 4. const, let, var 다시 알기

const는 업데이트 가능한가?

가능하다!!! 리 바인딩이 안 될 뿐이지

```javascript
const me = {name: 'john', age: 34}
undefined
me
{name: "john", age: 34}
me.name = "ashley"
"ashley"
me
{name: "ashley", age: 34}
```

다만 const가 int 자료형이라면 조작 불가능. 이것은 immutable이기 때문.

python 에서 mutable, immutable 외우는거 헷갈림.



하지만 js는

* immutable : 원시자료형(number, string, boolean, ...)

  => 우리가 정의하지 않은 자료형

* mutable : 사용자정의 자료형 == 객체

JS는 모든 것이 객체다. 원시 자료형 빼고. 즉 대부분 mutable.



javascript tutor에서 아래 코드 실행해보자

```javascript
const age = 34
age++
```

그동안 변수에 숫자를 넣은 것이 마치 age라는 박스에 34를 담은 거라 생각해옴.

하지만 bind라는 것이 었다. 상자속에 넣은게 아니라 age라는 바구니에 34가 가리키는 주소가 들어간 것이다.

즉 age에 +1하는 것은 age가 현재 binding한 값에 1 더한 것과 같은데, 이는 새로운 숫자를 가리키는 주소가 들어가야 한다는 것이다. 

34가리키던 값이 35로 바뀌면 rebind라고 한다.



마찬가지로 위에서 me라는 곳에 object를 가리키는 주소값이 들어간다. 포인터라고 하기도 한다. me.name 의 값을 바꾸면 const여도 바뀐다. 왜냐하면 가리키고 있는 주소는 바뀌지 않기 때문이다.

const가 막는 것은 특정한 변수가 설정이 되었을 때 다른 놈을 가리키지 못하게 하는 것이다. 즉 rebind를 막는 것과 같다.

const는 rebind를 막고 let은 rebind를 허용하고, var와 let은 사실상 scope 차이밖에 없다.



3가지 데이터 조작 종류가 있다.

reassign(초기화) - 유니크한 공간 차지

rebind

update

|          | var  | let  | const |
| :------: | :--: | :--: | :---: |
| reassign |  O   |  X   |   X   |
|  rebind  |  O   |  O   |   X   |
|  update  |  O   |  O   |   O   |

var와 let, const는 scope 차이가 있다.



---

## 5. 둘리 이미지 클릭시 반응

어떤 사건이 발생하는 걸 Event가 발생했다고 한다.

지금까지 수많은 Event를 무시해왔었는데 이제 열어주고자 한다.

`addEventListener`

아래사이트는 각종 이벤트 종류는 설명

<https://developer.mozilla.org/ko/docs/Web/Events>

**app.js**

**마우스 클릭시 반응하기**

```javascript
const dooly = document.querySelector('#dooly')

console.log(typeof(dooly))
// 둘리를 클릭하면, 호이라고 말한다.
dooly.addEventListener('click', function() { alert('호이')})
```

갑자기  click??  공식문서 들어가면 click.

왼쪽에는 어떤 event에 반응할지 쓰고, 오른쪽은 익명함수를 쓴다.

이제 둘리를 누르면 팝업 창이 '호이'라는 글자를 가지고 출력된다.



**키보드 눌렀을 때 event 종류 출력**

```javascript
document.addEventListener('keydown', function(event) {
    console.log(event)
})
```

이러면 키보드가 입력한 내용을 알아먹고, 위 코드를 통해 어떤 이벤트가 발생했는지 볼 수 있다. event는 object 형태로 결과를 내놓는다.

어떤 키를 눌렀는지 다 구분함.

자판은 문자마다 고유의 코드값이 있어서, 나라마다 다르게 인식시킬 필요는 없다.

zzu.ly/keycode 이 주소를 통해 키마다 고유 키 코드값을 출력해 볼 수 있다.



**키보드 눌렀을 때 key이름, 고유 key code 출력**

```javascript
document.addEventListener('keydown', function(event) {
    console.log(event.key) // 이벤트
    console.log(event.keyCode) // 키 코드
})
```



**키보드 눌렀을 때, 페이지에 keycode 출력**

아래 사이트에 들어가면 내 키에 따른 고유 keycode를 볼 수 있다.

zzu.ly/keycode

```javascript
document.addEventListener('keydown', function(event) {
    document.write(`<h1>${event.keyCode}</h1>`)
})
```

딱 한 번 밖에 출력 안 함. 그냥 write하고 마니까. 여러개를 써보고 싶으면 document를 말고 다른 걸 써야 한다.



---

## 6. 둘리 움직이기

JS 는 문자와 숫자를 비교해도, 강제로 타입 코올젼, implicit type casting으로 자기가 알아서 같게 한 다음 비교한다. 그래서 문제가 생기기도 하는데...

zzu.li/jseq

왠 그림을 보여준다. 등호 2개짜리, 등호 3개짜리에 따라 초록바가 채워지는게 달라진다.

JS는 자료형에 대해 좀 관대하다보니 서로 다른 자료형인데도 같은 값이라고 true를 반환하는 경우가 생긴다.



콘솔창에서 실제로 확인.

```javascript
if (1 == '1') {
    console.log("1과 '1'이 같다니!!")
}
// VM661:2 1과 '1'이 같다니!!
```

하지만 등호 3개라면 어떨까? 등호 3개는 아니라고 반환한다.



둘리를 움직인다? => 둘리의 margin을 조작하는 것은 어떨까?

둘리 공중부양

**1**

```javascript
document.addEventListener('keydown', function(event) {
    console.log(event.keyCode)
    if (event.keyCode === 38 ) {
        dooly.style.marginBottom = '300px'
    } else if (event.keyCode === 40) {
        dooly.style.marginBottom = '0px'
    } else if (event.keyCode === 37) {
        dooly.style.marginRight = '150px'
    } else if (event.keyCode === 39) {
        dooly.style.marginRight = '0px'
    }
})
```



**2**

```javascript
let x = 0
let y = 0

document.addEventListener('keydown', function(event) {
    console.log(event.keyCode)
    if (event.keyCode === 38 ) {
        y += 30
        dooly.style.marginBottom = `${y}px`
    } else if (event.keyCode === 40) {
        y -= 30
        dooly.style.marginBottom = `${y}px`
    } else if (event.keyCode === 37) {
        x -= 30
        dooly.style.marginLeft = `${x}px`
    } else if (event.keyCode === 39) {
        x += 30
        dooly.style.marginLeft = `${x}px`
    }
})
```



---

## 7. json, object 차이

JSON은 단순한 문자열로 되어있어서 이 상태로는 컴퓨터가 아무런 작업을 할 수 없다.

이걸 읽고 조작할 수 있는 형태로 바꾸는 것이 object로 변환한다는 뜻이다.



실제 통신에 있어서 요청에 따른 응답 내용이 JSON으로 전송된다면, 컴퓨터에는 이를 string으로 변환한 뒤에, Object로 변환하여 원하는데로 작업할 수 있게 한다.



참고로 json을 parsing 할 때 쌍따옴표(`""`) 를 기준으로 탈출한다. 따라서 반드시 홑따옴표가 바깥을 둘러쌓은 뒤 쌍따옴표가 안의 key, value를 감싸야 한다.

```javascript
// JSON & javascript object
/*
1. JSON : 파일 포맷 & 단순 문자열(string)
"{
    coffee: 'Americano',
    iceCream: 'Red Velvet',
}"

2. Javascript Object: Javascript 코드가 읽을 수 있는 오브젝트
*/

stringObject = JSON.stringify({ 'coffee': 'Americano', 'iceCream': 'Red Velvet' })

console.log(stringObject) // {"coffee":"Americano","iceCream":"Red Velvet"} 출력

JSONData = '{ "coffee": "Americano", "iceCream": "Red Velvet" }'

const parsedData = JSON.parse(JSONData)

console.log(parsedData.coffee) // Americano 출력

console.log(typeof(JSONData)) // String
console.log(typeof(parsedData)) // Object
console.log(typeof(stringObject)) // String
```


