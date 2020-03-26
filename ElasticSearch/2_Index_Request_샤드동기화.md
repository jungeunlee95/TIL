ISSUE

```
Elasticsearch에 문서 등록 후 바로 업데이트 시 elasticsearch id를 찾을 수 없음
```

<br>

```java
IndexRequest indexRequest = new IndexRequest(ElasticSearch.TODAY_INDEX.getValue(), ElasticSearch.TYPE.getValue(),
                docId).source(jsonMap)
                .waitForActiveShards(ActiveShardCount.ALL)
                .setRefreshPolicy(WriteRequest.RefreshPolicy.WAIT_UNTIL);
```

- elasticsearch shards가 현재 총 3개
- 3개에 다 insert 되면 응답 값을 주겠다는 의미
- ActiveShardCount.ALL = 모든 active 샤드