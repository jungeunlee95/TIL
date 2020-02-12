// 1. events module import
var events = require('events');

/* 2. EventEmitter(옵저버 패턴) 객체 생성
    eventEmitter.on(): 리스너를 등록하는데 사용.
    eventEmitter.emit(): 등록한 이벤트를 호출.
 */

var eventEmitter = new events.EventEmitter();

// 3. EventHandler 함수 생성
var connectHandler = function connected() {
    console.log("Connection Successful @@ ");

    // 4. data_received 이벤트 발생 시키기
    eventEmitter.emit("data_received");
}

// 4. connection 이벤트와 connectHandler 이벤트 핸들러 연동
eventEmitter.on('connection', connectHandler);

// 5. data_received 이벤트와 익명 함수 연동
// - 함수를 변수안에 담는 대신, .on() 메소드의 인자로 함수 직접 전달
eventEmitter.on('data_received', function () {
    console.log('Data Received !! ')
});

// 6. connection 이벤트 발생 시키기
eventEmitter.emit('connection');

console.log("Program has ENDED");

/*  console 실행
    $ node main.js
    Connection Successful @@
    Data Received !!
    Program has ENDED
 */