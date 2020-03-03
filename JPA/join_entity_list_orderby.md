entiy에 

`@OrderBy("")` 어노테이션 적용

```java
@OneToMany(mappedBy = "sample", fetch = FetchType.LAZY)
@OrderBy("type asc")
private Set<TestEntity> tests = new HashSet<>();
```

