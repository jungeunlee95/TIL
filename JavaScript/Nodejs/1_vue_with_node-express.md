[TOC]

### [1] Node Express 생성

https://medium.com/hivelab-dev/vue-express-mysql-part1-98f68408d444

```shell
[1] node express 생성
npm install -g express-generator
express --view=pug backend // backend 폴더 생성

[2] 서버 실행
cd backend 
npm install 
npm start
```

<br>

### [2] vue-router 와 node 연동

[https://router.vuejs.org/kr/guide/essentials/history-mode.html#%EC%84%9C%EB%B2%84-%EC%84%A4%EC%A0%95-%EC%98%88%EC%A0%9C](https://router.vuejs.org/kr/guide/essentials/history-mode.html#서버-설정-예제)

```shell
/d/odin-codes/odin-admin-front/backend
$ npm install connect-history-api-fallback -save
```

#### backend/app.js

```js
app.use(require('connect-history-api-fallback')()); // connect vuejs
```

<br>

### [3] env

```shell
npm install --save dotenv
```

















