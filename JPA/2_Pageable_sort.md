https://www.logicbig.com/tutorials/spring-framework/spring-data/sorting-and-pagination.html

<br>

### `@PageableDefault(sort = "address")`

호출 parameter 형식 => `sort=personName,desc`

#### `?page=1&size=10&sort=personName,desc`

<br>



**controller**

```java
@GetMapping(value = "/test")
public ResponseEntity test(
    @RequestParam(value = "name", required = false) String name,
    @PageableDefault(sort = "address") Pageable pageable,
    PagedResourcesAssembler<TestVO> assembler,
    HttpServletRequest request
    ) {
        Page<TestVO> tests = testService.findAllTests(name, pageable);
        var pagedModel = assembler.toModel(tests, data -> new TestModel(data, getTimeZoneId(request)));

        pagedModel.add(linkTo(TestController.class).slash("/docs/index.html#get-tests").withRel("profile"));

        return new ResponseEntity(pagedModel, HttpStatus.OK);
    }
```



<br>



**service**

```java
@Transactional(readOnly = true)
public Page<TestVO> findAllTests(Pageable pageable, String name) {
    return testRepository.findByNameContaining(
        pageable,
        name == null ? "" : name);
}
```

