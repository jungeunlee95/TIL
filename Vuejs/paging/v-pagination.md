**참고**

```
https://github.com/cichy380/vue-plain-pagination
	> https://github.com/cichy380/vue-plain-pagination/blob/master/src/App.vue
```

<br>

**package 설치**

```powershell
npm install --save vue-plain-pagination
```

<br>

**Example**

properties

| name        | description                                                 |
| ----------- | ----------------------------------------------------------- |
| v-model     | 현재 페이지 정보와 바인딩                                   |
| :page-count | 총 페이지 버튼 수 (전체 데이터수, 페이지 당 데이터 수 계산) |

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
    }.
    computed: {
        pageCount () {
            return Number((this.page.totalElements/this.pageSize + 1).toFixed())
        }
    }
}
</script>
```

