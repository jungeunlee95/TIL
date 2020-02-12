// 1. 필요한 모듈 import : require
var http = require("http"); // "http" 모듈을 불러와 http변수에 저장

/* 2-1. 1번에서 만든 http 인스턴스를 이용해 http.createServer()실행
   2-2. listen()으로 8081포트 바인딩
 */
http.createServer(function(request, response){
    /*
        HTTP 헤더 전송
        HTTP Status: 200 : OK
        Content Type: text/plain
    */
    response.writeHead(200, {'Content-Type': 'text/plain'});

    /*
        Response Body 를 "Hello World" 로 설정
    */
    response.end("Hello World\n");
}).listen(8081);


/* 3.서버 실행 후 접근
$ node 2_simple_server.js

> http://127.0.0.1:8081/ 접근 후 확인
 */
