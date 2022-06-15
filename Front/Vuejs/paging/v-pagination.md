**ref**

```
https://github.com/cichy380/vue-plain-pagination
	> https://github.com/cichy380/vue-plain-pagination/blob/master/src/App.vue
```

<br>

**package install**

```powershell
npm install --save vue-plain-pagination
```

<br>

**Example**

properties

| name        | description                                                 |
| ----------- | ----------------------------------------------------------- |
| v-model     | binding with current page data                                   |
| :page-count | total page count (total data count, data per page cal) |

```html
<template>
  <div>
      <v-pagination 
                  v-model="currentPage"      
                  :page-count="pageCount"    
                  @change="changeSelectedPage" 
                  :classes="bootstrapPaginationClasses">
      </v-pagination>
  </div>
</template>

<script>
import axios from 'axios'
import vPagination from 'vue-plain-pagination'

export default {
    components: { vPagination },
    data() { 
        return {
            keyword: 'aaa',
            currentPage: 1,
            pageSize: 10,
            bootstrapPaginationClasses: {
                ul: 'pagination',
                li: 'page-item',
                liActive: 'active',
                liDisable: 'disabled',
                button: 'page-link'
            }
        }
    },
    methods: {
        getNewPageList () {
            let obj = this
            axios.get('baseUrl/list', obj.getSearchParam()).then(function (response) {
                if (response.status === 200) {
                   alert('success')
                }
            }).catch(function (error) {
                console.log(error)
            })
        },
        getSearchParam () {
            let params = {
                size: this.pageSize,
                page: this.currentPage
            }
            return params
        },
        urlRefresh () {
            this.$router.push({
                path: '/path',
                query: {
                    keyword: this.keyword,
                    page: this.currentPage
                }
            }).catch(err => err)
        },
        changeSelectedPage () {
            this.urlRefresh()
            this.getNewPageList()
        }
    },
    computed: {
        pageCount () {
            return Number((this.page.totalElements/this.pageSize + 1).toFixed())
        }
    }
}
</script>
```

