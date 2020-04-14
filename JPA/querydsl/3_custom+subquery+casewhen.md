[TOC]

------

1. `CaseBuilder cases = new CaseBuilder();`
2. `cases.when(secondTestVO.kind.eq("001")).then(1).otherwise(0).sum().as("001Counts")`

### 전체

```java
    @Override
    public Page<TestCustomVO> findAllBySearch(Integer searchId, TestSearchDTO testSearchDTO, Pageable pageable) {
        CaseBuilder cases = new CaseBuilder();
        JPAQuery query = queryFactory
                .select(Projections.fields(TestCustomVO.class,
                        testVO.id.as("testId"),
                        testVO.searchId,
                        testVO.name,
                        testVO.phoneNumber,
                        testVO.creationTime,
                        testConditionsVO.status,
                        testLabelsVO.value.as("testLabel"),
                        secondTestVO.id.count().as("totalSeconds"),
                        cases.when(secondTestVO.kind.eq("001")).then(1).otherwise(0).sum().as("001Counts"),
                        cases.when(secondTestVO.kind.eq("002")).then(1).otherwise(0).sum().as("002Counts"),
                        cases.when(secondTestVO.kind.eq("003")).then(1).otherwise(0).sum().as("003Counts"),
                        cases.when(secondTestVO.kind.eq("004")).then(1).otherwise(0).sum().as("004Counts"),
                        cases.when(secondTestVO.kind.eq("005")).then(1).otherwise(0).sum().as("005Counts"),
                        cases.when(secondTestVO.kind.eq("006")).then(1).otherwise(0).sum().as("006Counts")
                )).distinct()
                .from(testVO)
                .innerJoin(testVO.conditions, testConditionsVO).on(testVO.id.eq(testConditionsVO.testId), testConditionsVO.type.eq("up"))
                .leftJoin(testVO.labels, testLabelsVO).on(testVO.id.eq(testLabelsVO.testId), testLabelsVO.key.eq("key01"))
                .leftJoin(testVO.secondTest, secondTestVO).on(testVO.searchId.eq(secondTestVO.searchId), testVO.name.eq(secondTestVO.name), secondTestVO.isDeleted.eq(false))
                .where(
                        testVO.searchId.eq(searchId),
                        QuerydslUtil.eq(testVO.name, testSearchDTO.getName()),
                        QuerydslUtil.eq(testVO.phoneNumber, testSearchDTO.getPhoneNumber()),
                        QuerydslUtil.eq(testLabelsVO.value, testSearchDTO.getTestLabel())
                );

        long totalCount = query.fetchCount();

        query
                .groupBy(testVO.id)
                .orderBy(QuerydslUtil.o)
                .offset(pageable.getOffset())
                .limit(pageable.getPageSize());

        return new PageImpl<>(query.fetch(), pageable, totalCount);
    }
```

