## 버튼 클릭 시, 변수 초기화 & 메소드 호출 동시에 해야 하는 경우
**ex**: 주소 리스트 검색용 name input 변수 초기화 & 주소 리스트 조회를 동시에

`@click="() => {findQuery.name=''; getAddress()}"`

> 검색 조건: 객체 내의 값

```html
<b-form-input 
              placeholder="name" 
              v-model="findQuery.name" 
              v-on:keyup="checkEnterKeyEvent" 
              v-on:blur="getAddress">
</b-form-input>
<b-btn 
       :disabled="!findQuery.name" 
       @click="() => {findQuery.name=''; getAddress()}" 
       class=".p-0">
    X
</b-btn>
```

---

<br>

### 변수 초기화 + 함수 실행 <br>

> 검색 조건: 일반 변수(searchValue) 경우

```html
<b-form-input 
              placeholder="name" 
              v-model="searchValue" 
              v-on:keyup="checkEnterKeyEvent" 
              v-on:blur="getAddress">
</b-form-input>
<b-btn 
       :disabled="!searchValue" 
       @click="() => {searchValue=''; getAddress()}" 
       class=".p-0">X</b-btn>
```
<br>
v-on:keyup="checkEnterKeyEvent" : 키보드의 키를 놓았을 때 실행 

> keyboard enter일 경우만 재검색

<br>
v-on:blur="getAddress" : 태그에 포커스를 잃었을 때 실행
<br>

```js
checkEnterKeyEvent (e) {
  if (e.keyCode === 13) this.getAddress()
}
```