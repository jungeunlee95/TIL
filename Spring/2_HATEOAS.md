https://docs.spring.io/spring-hateoas/docs/current/reference/html/

## HATEOAS (Hypermedia As The Engine Of Application State)

#### (응용 프로그램 상태 엔진으로서의 하이퍼 미디어) 

- Restful한 api 리소스를 제공할때 도움을 주는 라이브러리

- 기본적인 아이디어는 하이퍼미디어를 애플리케이션의 상태를 동적으로 관리하기 위한 매커니즘으로 사용한다는 것입니다.

  - 하이퍼미디어?

    > 하이퍼미디어 정보는 이용자가 정보를 탐색할 때 어떤 제목에서 **관련 제목으로 넘어 갈 수 있도록 연결**되어 있다. 

- 사용자 정보를 생성(POST)하는 요청 이후, 이를 조회(GET), 수정(PUT), 삭제(DELETE)할 때, 이러한 모든 동작을 URI를 이용하여 동적으로 알려준다 는 의미입니다.

- 장점? 클라이언트를 개발하는 사람들이 특정 메소드로부터 올 수 있는 결과 동작에 대해 **예측하는 것이 가능**해지고, 
- API가 변경되더라도 키가 바뀌지 않는 한 URI로 주어진 링크(link)만 유지하면 되므로 별도의 대응이 요구되지 않게 됩니다. 

- 즉, 클라이언트가 제공되는 API의 변화에 일일이 대응하지 않아도 되는 엄청난 편리함을 제공받게 되는 것이죠.



```
ResourceSupport
```

왜?

https://pjh3749.tistory.com/260
HAL은 가벼운 mediatype으로 데이터와 하이퍼미디어들을 인코딩할수 있고 API의 다른 부분으로 이동할 수 있도록 소비자에게 알려준다. 다음 예는 self 링크와 aggregate root로 가는 링크까지 포함한다.
Resource<>는 Spring HATEOAS의 또다른 컨테이너로 컬렉션을 캡슐화한다. 이것 또한 링크를 포함하게 해준다. 여기서 컬렉션을 자바의 컬렉션개념을 생각하면 안된다. REST 관점에서 컬렉션 캡슐화는 employee 리소스들에 대한 것이다.

그것이 모든 employees를 fetch하는 이유이다. 결과는 다음과 같다.

이 aggregate root로는 employee 리소스들의 컬렉션을 제공하고 top-level에 self링크가 있는 것을 볼 수 있다. "컬렉션"은 "_embedded" 섹션에 리스트업되어 있는데 이것이 HAL이 컬렉션을 표현하는 방법이다.

그리고 각각의 컬렉션 멤버들은 각자의 연관된 링크 정보들을 가지고 있다.

도대체 왜 이런 모든 링크들을 추가하는 것일까? 이것은 REST 서비스를 시간이 지남에 따라 발전 가능하게 해준다. 기존의 링크는 남아있되 새로운 링크는 미래에 추가되는 것이다. 새로운 클라이언트는 새로운 link들의 정보를 얻고, 레거시한 클라이언트들은 이전 링크를 가질수가 있다. 이것은 서비스가 relocated되거나 moved around할 때 매우 도움이 된다. 링크 구조가 남아 있다면 클라이언트는 이런것들과 상호작용을 할 수 있다.

정리하자면 REST는 예쁜 URI에 XML이 아닌 JSON을 내려준다고 해서 REST라고는 할 수 없다. 대신에 다음 전략을 따르며 기존 고객을 빠져나가지 않게 하는 것을 돕는 것이다.

1. 이전 필드를 삭제하지 말고 지원해라.
2. rel-based한 링크를 사용하여 client가 URI를 하드코드하지 않게 한다.
3. old 링크들을 가능한 한 오래 보유해라. URI가 바뀐다고 하더라도 기존 rels를 보유하여 기존 고객들이 새로운 기능으로 연결되게 하라.
4. 클라이언트에게 다양한 상황에서 행동들을 알려주기 위해 데이터를 단순 적재 하지말고 Link를 사용해라.