[TOC]

---

성모님이 알려주심

```java
import com.cafe24.bnc.admin.domain.common.ListPage;
import com.querydsl.core.types.Order;
import com.querydsl.core.types.OrderSpecifier;
import com.querydsl.core.types.Path;
import com.querydsl.core.types.dsl.BooleanExpression;
import com.querydsl.core.types.dsl.Expressions;
import com.querydsl.core.types.dsl.SimpleExpression;
import com.querydsl.core.types.dsl.StringPath;
 
import java.util.List;
 
/**
 * Querydsl Eq() method util
 */
public class ExpressionUtil {
    /**
     * Querydsl의 eq메소드를 전체적으로 사용할 수 있도록 만든 util.<br/>
     *
     * @param path  QClass.variable
     * @param value value
     * @return return null or BooleanExpression
     */
    public static <T> BooleanExpression eq(SimpleExpression<T> path, T value) {
        if (value == null) {
            return null;
        }
 
        // if value is String type, must check "".
        if (value instanceof String) {
            if ("".equals(value)) {
                return null;
            }
        }
 
        return path.eq(value);
    }
 
 
    /**
     * Querydsl의 like메소드를 전체적으로 사용할 수 있도록 만든 util.<br/>
     *
     * @param stringPath  QClass.variable
     * @param value value ( %가 없는 경우 %value% , %가 있다면 해당 value를 조건 그대로 넣음)
     * @return return null or BooleanExpression
     */
    public static BooleanExpression like(StringPath stringPath, String value) {
        if (value == null) {
            return null;
        }
 
        if (!value.contains("%")) {
            return stringPath.contains(value);
        }
 
        return stringPath.like(value);
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
 
 
    @SuppressWarnings("unchecked")
    public static <T> OrderSpecifier<?> orderBy(String field, Order order) {
 
        return new OrderSpecifier(order, Expressions.path(Object.class, field));
    }
 
 
    @SuppressWarnings("unchecked")
    public static <T> OrderSpecifier<?> orderBy(Path<T> path, String field, Order order) {
 
        return new OrderSpecifier(order, Expressions.path(Object.class, path, field));
    }
 
 
    /**
     * @param path     QClass 의 Entity 변수
     * @param listPage List Paging 객체
     * @return OrderExpression
     *
     * @see {@literal} SecurityAuthorityLogLRepoImpl.java 참고
     */
    @SuppressWarnings("unchecked")
    public static <T> OrderSpecifier<?> orderBy(Path<T> path, ListPage listPage) {
        // TODO OrderBy 여러개 들어오는 경우가 있다면 그에 대한 처리가 필요함.
 
        return new OrderSpecifier(listPage.getOrderByAdc(),
                Expressions.path(Object.class, path, listPage.getCamelCaseOrderByColumn()));
    }
}
```

### eq 사용예시

```java
@Override
public Page<TestEntity> findAllBySearch(String testId, TestDto testDto, Pageable pageable) {
    JPAQuery query = queryFactory
        .selectFrom(testEntity).distinct()
        .innerJoin(testEntity.testEntity2, testEntity2).fetchJoin()
        .where(
        testEntity.testEntity2.id.eq(testId),
        ExpressionUtil.eq(testEntity.aaa, testDto.getAaa()),
        ExpressionUtil.eq(testEntity.bbb, testDto.getBbb()),
        ExpressionUtil.eq(testEntity.ccc, testDto.getCcc()),
        ExpressionUtil.eq(testEntity.ddd, testDto.getDdd()),
        ExpressionUtil.eq(testEntity.eee, testDto.getEee())
    );

    long totalCount = query.fetchCount();

    query
        .orderBy(testEntity.id.asc())
        .offset(pageable.getOffset())
        .limit(pageable.getPageSize());

    return new PageImpl<>(query.fetch(), pageable, totalCount);
}
```

