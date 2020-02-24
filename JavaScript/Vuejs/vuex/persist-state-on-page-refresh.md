npm: `npm install --save vuex-persistedstate`



**store.js 하위 추가**

```js
import createPersistedState from 'vuex-persistedstate'

  plugins: [
    createPersistedState({
      storage: window.sessionStorage
    })
  ],
```



**store.js 전체**

```js
// store.js
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export const store = new Vuex.Store({
  plugins: [
    createPersistedState({
      storage: window.sessionStorage
    })
  ],
  state: {
    test: []
  },
  getters: {
    getTest: function (state) {
      return state.test
    }
  },
  mutations: {
    setTest: function (state, payload) {
      state.test = payload.test
    }
  },
  actions: {
    getTest (context, payload) {
      axios.get(payload.url + '/test', {headers: {
        'Accept': 'application/hal+json',
        'Content-Type': 'application/json',
        'Authorization': payload.token
      }}).then(function (response) {
        if (response.status === 200) {
          context.commit('setTest', {
            test: response.data._embedded.test
          })
        }
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
})

```

