[TOC]

------

https://github.com/PeachScript/vue-infinite-loading

------

### npm

`npm install vue-infinite-loading -S`

------

### Component

```html
<template>
  <infinite-loading></infinite-loading>
</template>

<script>
import InfiniteLoading from 'vue-infinite-loading';

export default {
  components: {
    InfiniteLoading,
  },
};
</script>
```

### main.js or Plugin

```js
// main.js or index.js
import InfiniteLoading from 'vue-infinite-loading';

Vue.use(InfiniteLoading, { /* options */ });
```

------

### Example

html

```html
<CSelect
         class="mb-1"
         @change="selectChange"
         :value.sync="findQuery.keyword"
         :options="testOptions"
         />

<div v-for="testItem in testItems" :key="testItem.id"></div>

<infinite-loading
                  ref="InfiniteLoading"
                  @infinite="infiniteHandler"></infinite-loading>
```

script

```js
export default {
  name: 'TestList',
  data: function () {
    return {
      testItems: [],
      currentPage: 1,
      page: {
        size: 10,
        totalElements: 0,
        totalPages: 1,
        number: 0
      },
      testOptions: [],
      findQuery: {
        keyword: ''
      }
    }
  },
  methods: {
    getOptions () {
      let obj = this
      Api.get('/options').then(function (response) {
        if (response.data.page.totalElements > 0) {
          response.data._embedded.testOptions.forEach(function (data) {
            obj.testOptions.push({value: data.value, label: data.name})
          })
        }
      }).catch(function (error) {
        console.log(error)
      })
    }
    infiniteHandler($state) {
      this.currentPage += 1;
      this.getDatas($state)
    },
    getDatas ($state) {
      let obj = this
      Api.get('/datas', this.getSearchParam()).then(function (response) {
        if (response.status === 200) {
          obj.page = response.data.page
          if (response.data.page.totalElements === 0) {
            obj.testItems = []
            if ($state !== undefined) $state.complete()
          } else {
            obj.testItems.push(...response.data._embedded.testItems)
            if ($state !== undefined) $state.loaded()
            if ((obj.currentPage == obj.page.totalPages) && $state !== undefined) $state.complete()
          }
          obj.routerPush()
        }
      }).catch(function (error) {
        if ($state !== undefined) $state.complete()
        console.log(error)
      })
    },
    getSearchParam () {
      let params = {
        size: this.page.size,
        page: this.currentPage
      }
      if (this.findQuery.keyword !== '') params['keyword'] = this.findQuery.keyword
      return params
    },
    routerPush () {
      this.$router.push({path: '/test/list', query: this.getUrlQuery()}).catch(err => err)
    },
    getUrlQuery () {
      return {
        keyword: this.findQuery.keyword
      }
    },
    selectChange () {
      this.testItems = []
      this.currentPage = 0
      this.routerPush()
      // InfiniteLoading 초기화
      this.$refs.InfiniteLoading.stateChanger.reset()
    }
  },
  created() {
    if (this.$route.query.keyword !== undefined) this.findQuery.keyword = this.$route.query.keyword
  },
  mounted () {
    this.getOptions()
  }
}
```





































