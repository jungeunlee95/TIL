bootstrap modal 레이어에서 

valid 검사 필요 or close 버튼 클릭 외의 창이 닫히는 경우 이벤트 핸들링 필요함.

<br>

`bvModalEvt.preventDefault()`로 핸들링 할 수 있음

```html
<b-modal 
         title="MODAL" 
         v-model="modalOpen" 
         @ok="onSubmit" 
         @cancel="removeFormData"
>
    ...
</b-modal>
```

```js
submitCreateService (bvModalEvt) {

    bvModalEvt.preventDefault()

        ...

}
```
