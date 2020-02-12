const EventEmitter = require('events');

class MyEmitter extends EventEmitter {}

/*
    EventListener는 모든 리스너를 등록한 순서대로 동기적으로 처리한다.
    즉 이벤트를 적절한 순서로 처리하는 것을 보장해 경쟁 조건(race condition)이나 로직 오류를 피하는 것이 중요하다.
    이 모든 것이 적절하게 구현되었을 때, setImmediate()이나 process.nextTick()메소드를 사용해 리스너 함수를 비동기도 동작하도록 전환할 수 있다.
 */

const myEmitter = new MyEmitter();
myEmitter.on('event', (a, b) => {
    setImmediate(() => {
        console.log('this happens asynchronously');
    });
});
myEmitter.emit('event', 'a', 'b');