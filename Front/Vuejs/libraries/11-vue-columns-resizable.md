[TOC]

---

https://www.npmjs.com/package/vue-columns-resizable

---

### npm

`https://www.npmjs.com/package/vue-columns-resizable`

----

### main.js or Plugin

```js
import VueColumnsResizable from 'vue-columns-resizable'
Vue.use(VueColumnsResizable)
```

---

### Example

html

```html
<div :style="datas.length > 0 ? 'overflow-x: scroll' : ''">
    <b-table 
             :items="datas" 
             :fields="fields" 
             class="table-bordered"
             v-columns-resizable>
    </b-table>
</div>    

<div v-if="datas.length === 0" class="text-center m-3 font-weight-bold">data does not exist.</div>
```

script

```js
export default {
    name: 'TestList',
    data: function () {
        return {
            datas: [],
            fields: [
                {key: '#', label: '#', class: 'text-left', tdClass: 'body-padding', thStyle: {width: '60px'}},
                {key: 'id', label: 'ID', class: 'text-left', sortable: true, tdClass: 'body-padding', thStyle: {width: '80px'}},
                {key: 'name', label: 'Name', class: 'text-left', sortable: true, tdClass: 'body-padding', thStyle: {width: '270px'}},
                {key: 'password', label: 'Password', class: 'text-left', sortable: true, tdClass: 'body-padding', thStyle: {width: '250px'}}
            ]
        }
    }
}
```

style

```css
table {
  min-width: 1800px;
  table-layout: fixed;
}
.table th, .table td {
  min-width: 10px;
  overflow: hidden;
  white-space: nowrap;
  -moz-text-overflow: ellipsis;
  -ms-text-overflow: ellipsis;
  -o-text-overflow: ellipsis;
  text-overflow: ellipsis;
}
```





































