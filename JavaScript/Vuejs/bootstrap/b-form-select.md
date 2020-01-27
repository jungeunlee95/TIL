## 1. :options 조건에서 특정 option만 disabled

```html
<template>
    <b-form-select
                   v-bind:disabled="a === b"
                   :plain="true"
                   :options="['APPLE','BANANA','MELON',{ value: 'GRAPE', text: 'GRAPE', disabled: true }]"
                   :value=value
                   v-on:change="modify($event)"
                   >
    </b-form-select>
</template>
```

`v-bind:disabled` 버튼 자체 disable

`:options` > `disabled: true` 해당 옵션만 선택 불가능 

`:value` : 옵션과 바인딩 될 데이터

`v-on:change` 클릭시 `$event` > 선택한 option의 value를 method

