[TOC]

------

- api- pageable sort 사용 (ex) ?sort=name,desc)

------

```html
<b-table :items="items" :fields="fields" class="table table-hover" responsive
         :sort-by.sync="sortBy"
         :sort-desc.sync="sortDesc"
         >
</b-table>

<b-pagination-nav
                  align="center"
                  v-model="currentPage"
                  :linkGen="linkGen"
                  :number-of-pages="page.totalPages"
                  @input="getTestData"
                  use-router>
</b-pagination-nav>
```

```js
export default {
  name: 'Test',
  data: function () {
    return {
      sortBy: '',
      sortDesc: '',
      currentPage: 1,
      page: {
        size: 15,
        totalElements: 0,
        totalPages: 1,
        number: 0
      },
      fields: [
        '#',
        {key: 'id', label: 'ID', class: 'text-left', sortable: true},
        {key: 'name', label: 'Name', class: 'text-left', sortable: true,
        {key: 'address', label: 'Address', class: 'text-left'}
      ],
      findQuery: {
        address: '',
        name: ''
      }
    }
  },
  methods: {
    linkGen (pageNum) {
      let params = {
        page: pageNum
      }
      if (this.findQuery.address !== '') params['address'] = this.findQuery.address
      if (this.findQuery.name !== '') params['name'] = this.findQuery.name
      return {
        path: '/test',
        query: params
      }
    },
    getTestData () {
      let obj = this
      obj.loading = true
      Api.get('/test', obj.getSearchParam()).then(function (response) {
        if (response.status === 200) {
          obj.page = response.data.page
          if (obj.page.totalPages === 0) obj.page.totalPages = 1
          if (response.data.page.totalElements === 0) {
            obj.tests = []
          } else {
            obj.tests = response.data._embedded.tests
          }
        }
        obj.routerPush()
        obj.loading = false
      }).catch(function (error) {
        console.log(error)
        obj.loading = false
      })
    },
    routerPush () {
      this.$router.push({path: '/test', query: this.getUrlQuery()}).catch(err => err)
    },
    getUrlQuery () {
      let params = {}
      if (this.findQuery.address !== '') params['address'] = this.findQuery.address
      if (this.findQuery.name !== '') params['name'] = this.findQuery.name
      if (this.currentPage !== 1) params['page'] = this.currentPage
      return params
    },
    getSearchParam () {
      let params = {
        sort: this.sortDesc ? this.sortBy + ',desc' : this.sortBy + ',asc',
        size: this.page.size,
        page: this.currentPage
      }
      if (this.findQuery.address !== '') params['address'] = this.findQuery.address
      if (this.findQuery.name !== '') params['name'] = this.findQuery.name
      return params
    }
  },
  watch: {
    sortBy: function () {
      this.getTestData()
    },
    sortDesc: function () {
      this.getTestData()
    }
  }
}
```

