#### b-table field에 formatter 사용

ex) 숫자의 경우 3자리마다 콤마(,) 찍기 formatter 적용

```js
export default {
  name: 'Test',
  data: function () {
    return {
      fields: [
        '#',
        {key: 'testNum', label: 'testNum', sortable: true, class: 'text-left', formatter: 'numberWithCommas'}
      ]
    }
  },
  methods: {
    numberWithCommas (num) {
      return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
    }
  }
```

