[TOC]

persist-state-on-page-refresh

<br>

### Nuxt.js에서 Store state 유지 (localStorage 사용)

<br>

### [1] npm 설치

`npm install --save vuex-persistedstate`

<br>

### [2] plugins/localStorage.js

```js
import createPersistedState from 'vuex-persistedstate'

export default ({store}) => {
  createPersistedState({
    storage: window.sessionStorage
  })(store)
}
```

<br>

### [3] nuxt.config.js

```js
  plugins: [
    { src: '~/plugins/axios', ssr: false },
    { src: '~/plugins/localStorage.js', ssr: false }
      ...
  ],
```

