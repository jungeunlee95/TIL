[TOC]

axios cors

nuxt axios cors



#### nuxt.config.js proxy 추가

```js
  proxy: {
    "/dev": {
      target: "https://api-dev.test.com",
      pathRewrite: { "^/dev": "" }
    },
    "/prod": {
      target: "https://api.test.com",
      pathRewrite: { "^/prod": "" }
    },
  },
```



#### plugins/axios.js proxy 추가

```js
  // CORS 허용을 위한 proxy 설정 axios
  const api2 = $axios.create({
    proxy: true,
    headers: {
      common: {
        'Content-Type': 'application/json',
        'Authorization': token,
        'Accept': 'application/hal+json;charset=UTF-8',
        'Timezone': Intl.DateTimeFormat().resolvedOptions().timeZone
      }
    }
  })
  
  
  api2.setToken(token)

  inject('api2', api2)
```



#### api 호출 시

```js
// 기존 api
this.$api.get(...)
              
// proxy 적용 api
 let apiUrl = ''
let hostname = window.location.hostname
if (hostname === 'prod.test.com') apiUrl = '/prod/board/1'
else apiUrl = '/dev/board/1'

this.$api2.get(apiUrl)   
```

