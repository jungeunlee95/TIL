Node.js 기반으로 만들어진 서버가 가동되면, 

- 변수들을 initialize 하고, 
- 함수를 선언하고, 
- 이벤트가 일어날때까지 기다린다.

이벤트 위주 (Event-Driven) 어플리케이션에서는, 이벤트를 대기하는 메인 루프가 있다.

그리고 이벤트가 감지되었을시 **Callback함수를 호출**한다.

> 이벤트가 콜백과 비슷해 보일 수 도 있다. 
>
> 차이점은, 콜백함수는 **비동기식 함수에서 결과를 반환할때 호출**되지만,
>
> 이벤트핸들링은 **옵저버 패턴에 의해 작동**됩니다.
>
> 이벤트를 대기하는 (EventListeners)  함수들이 옵저버 역할. 
>
> 옵저버들이 이벤트를 기다리다가, 이벤트가 실행되면 이벤트를 처리하는 함수가 실행.

```
observer pattern? 
객체의 상태 변화를 관찰하는 관찰자들, 즉 옵저버들의 목록을 객체에 등록하여 상태 변화가 있을 때마다 메서드 등을 통해 객체가 직접 목록의 각 옵저버에게 통지하도록 하는 디자인 패턴이다. 
주로 분산 이벤트 핸들링 시스템을 구현하는 데 사용된다. 발행/구독 모델로 알려져 있기도 하다.

이 패턴의 핵심은 
1. 옵저버 또는 리스너(listener)라 불리는 하나 이상의 객체를 관찰 대상이 되는 객체에 등록시킨다. 
2. 그리고 각각의 옵저버들은 관찰 대상인 객체가 발생시키는 이벤트를 받아 처리한다.
3. 이벤트가 발생하면 각 옵저버는 콜백(callback)을 받는다.
```

<br>

Node.js 에는 **events** 모듈과 **EventEmitter** 클래스가 내장되어있다,
이를 사용하여 이벤트와 이벤트핸들러를 연동(bind) 시킬 수 있다

```
// events 모듈 사용
var events = require('events');

// EventEmitter 객체 생성
var eventEmitter = new events.EventEmitter();
```

이벤트 핸들러와 이벤트를 연동

```
// event와 EventHandler 를 연동(bind)
// eventName 은 임의로 설정 가능
eventEmitter.on('eventName', eventHandler);
```

프로그램안에서 이벤트를 발생

```
eventEmitter.emit('eventName');
```

 































