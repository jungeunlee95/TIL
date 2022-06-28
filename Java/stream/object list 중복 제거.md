https://stackoverflow.com/questions/23699371/java-8-distinct-by-property

**MemberDto.java**

```java
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class SystemIPAddressDto {
    private Integer id;
    private String name;
    private String address;
}

```

```java
ArrayList<MemberDto> memberList = new ArrayList<>();
test.add(new MemberDto(1, "AA", "aa"));
test.add(new MemberDto(2, "BB", "bb"));
test.add(new MemberDto(1, "AA", "aa"));
test.add(new MemberDto(2, "CC", "cc"));
test.add(new MemberDto(3, "DD", "dd"));
test.add(new MemberDto(4, "EE", "ee"));
```



**1**

```java
ArrayList<MemberDto> deduplicationList = memberList.stream().collect(Collectors.collectingAndThen(
    Collectors.toCollection(() -> new TreeSet<>(Comparator.comparing(MemberDto::getId).thenComparing(MemberDto::getName))
                           ), ArrayList::new));
```

**2**

```java
private static <T> Predicate<T> distinctByKey(Function<? super T, ?> keyExtractor) {
    Map<Object, Boolean> seen = new ConcurrentHashMap<>();
    return t -> seen.putIfAbsent(keyExtractor.apply(t), Boolean.TRUE) == null;
}
```

```java
List<MemberDto> deduplicationList = memberList.stream()
    .filter(distinctByKey(pr -> Arrays.asList(pr.getIp(), pr.getType())))
    .collect(Collectors.toList());
```



**result**

```
1 AA aa
2 BB bb
2 CC cc
3 DD dd
4 EE ee

```

