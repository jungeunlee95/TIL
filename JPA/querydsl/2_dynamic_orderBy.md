[TOC]

### Util

```java
/**
 * order specifier. querydsl로 pageable sort 처리할 때 사용
 * 객체 그래프를 타야 하는 속성들을 넣으면 오류가 발생한다.(ex) serviceEntity.gitlab.id)
 *
 * @param property 정렬하고 싶은 속성(QEntity field에 맞춰서 써줘야 함)
 * @param orderDirection 오름차순? 내림차순?
 * @param basePath QEntity 객체(ex) serviceEntity, appEntity, ...)
 * @return
 */
public static <T> OrderSpecifier<?> toOrderSpecifier(String property, Sort.Direction orderDirection, PathBuilder<T> basePath) {
    StringPath path = basePath.getString(property);
 
    Order querydslOrder = null;
    if(orderDirection == Sort.Direction.ASC) {
        querydslOrder = Order.ASC;
    }
    if(orderDirection == Sort.Direction.DESC) {
        querydslOrder = Order.DESC;
    }
 
    return new OrderSpecifier(querydslOrder, path);
}
```



### 사용

```java
List<OrderSpecifier<?>> orderSpecifiers = new ArrayList<>();
for (Sort.Order order : pageable.getSort()) {
    orderSpecifiers.add(QuerydslUtil.toOrderSpecifier(order.getProperty(), order.getDirection(), new PathBuilder<>(TestEntity.class, "testEntity")));
}

query
    .orderBy(orderSpecifiers.toArray(new OrderSpecifier[orderSpecifiers.size()]))
    .offset(pageable.getOffset())
    .limit(pageable.getPageSize());

return new PageImpl<>(query.fetch(), pageable, totalCount);
```



### Util 전체

```java
public class QuerydslUtil {
 
    /**
     * Querydsl의 eq메소드를 전체적으로 사용할 수 있도록 만든 util
     * optional한 경우 사용
     *
     * @param path  QClass.variable
     * @param value value
     * @return return null or BooleanExpression
     */
    public static <T> BooleanExpression eq(SimpleExpression<T> path, T value) {
        if(StringUtils.isEmpty(value)) {
            return null;
        }
 
        return path.eq(value);
    }
 
    /**
     * Querydsl의 like메소드를 전체적으로 사용할 수 있도록 만든 util
     * 부분일치 검색용, optional한 경우 사용
     *
     * @param stringPath  QClass.variable
     * @param value value
     * @return return null or BooleanExpression
     */
    public static BooleanExpression like(StringPath stringPath, String value) {
        if(StringUtils.isEmpty(value)) {
            return null;
        }
 
        return stringPath.contains(value);
    }
 
    public static <T> BooleanExpression in(SimpleExpression<T> path, List<T> value) {
        if (value.isEmpty()) {
            return null;
        }
 
        // Size가 1인 경우 값이 없는 경우에도 1이므로 체크
        if (value.size()==1 && value.iterator().next() == null){
            return null;
        }
 
        return path.in(value);
    }
 
    /**
     * order specifier. querydsl로 pageable sort 처리할 때 사용
     * 객체 그래프를 타야 하는 속성들을 넣으면 오류가 발생한다.(ex) serviceEntity.gitlab.id)
     *
     * @param property 정렬하고 싶은 속성(QEntity field에 맞춰서 써줘야 함)
     * @param orderDirection 오름차순? 내림차순?
     * @param basePath QEntity 객체(ex) serviceEntity, appEntity, ...)
     * @return
     */
    public static <T> OrderSpecifier<?> toOrderSpecifier(String property, Sort.Direction orderDirection, PathBuilder<T> basePath) {
        StringPath path = basePath.getString(property);
 
        Order querydslOrder = null;
        if(orderDirection == Sort.Direction.ASC) {
            querydslOrder = Order.ASC;
        }
        if(orderDirection == Sort.Direction.DESC) {
            querydslOrder = Order.DESC;
        }
 
        return new OrderSpecifier(querydslOrder, path);
    }
}
```

