const EventEmitter = require('events');

class MyEmitter extends EventEmitter {}

const myEmitter = new MyEmitter();

myEmitter.on('event', function(a, b) {
    console.log(a, b, this);
});
myEmitter.emit('event', '@ Hello', 'World @');

/*
$ node 2_this.js
@ Hello World @ MyEmitter {
  _events: [Object: null prototype] { event: [Function] },
  _eventsCount: 1,
  _maxListeners: undefined }
 */

console.log('-------------------------------------------------')
/*
    ES6의 Arrow 함수를 리스너로 사용하는 것은 가능하지만,
    이 함수 내에서의 this는 더이상 EventEmitter 인스턴스를 참조하지 않는다.
 */
const myEmitter2 = new MyEmitter();
myEmitter2.on('event', (a, b) => {
    console.log(a, b, this);
});
myEmitter2.emit('event', 'a', 'b');

/*
    a b {}
 */