https://docs.spring.io/spring-hateoas/docs/current/reference/html/

리소스에 링크추가

```java
@Getter
@Relation(collectionRelation = "test")
public class TestResource extends ResourceSupport {
    private final Long id;

    public TestResource(TestEntity test) {
        this.id = test.getId();
    
        //url
        this.add(new Link("https://naver.com", "naverUrl"));
        this.add(new Link("https://google.com", "googleUrl"));

    }
}


```
