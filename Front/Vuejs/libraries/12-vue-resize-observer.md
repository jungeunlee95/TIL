[TOC]

---

https://heropy.blog/2019/11/30/resize-observer/

---

### npm

`npm i @juggle/resize-observer`

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
import {ResizeObserver} from '@juggle/resize-observer'
export default {
    name: 'TestList',
    data: function () {
        return {
            test1: '',
            test2: '',
        }
    },
      watch: {
        test1: function () {
          console.log(this.test1)
        },
        test2: function () {
          console.log(this.test2)
        }
      },
      mounted () {
        let obj = this
        const table = document.getElementsByTagName('table')[0]
        const tr = table.getElementsByTagName('tr')[0]
        const aaa = tr.getElementsByTagName('th')[9]
        const bbb = tr.getElementsByTagName('th')[10]

        const ro1 = new ResizeObserver(entries => {
          entries.forEach(entry => {
            obj.test1 = entry.borderBoxSize[0].inlineSize
          })
        })
        ro1.observe(aaa)

        const ro2 = new ResizeObserver(entries => {
          entries.forEach(entry => {
            obj.test2 = entry.borderBoxSize[0].inlineSize
          })
        })
        ro2.observe(bbb)
      },
}
```

