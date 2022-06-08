[TOC]

axios cors

nuxt axios cors



#### nuxt.config.js proxy 추가

```js
  // axios proxy 추가
  axios: {
    // See https://github.com/nuxt-community/axios-module#options
    // baseURL: process.env.apiUrl
    proxy: true
  },
  
  // proxy 추가
  proxy: {
    "/dev": {
      target: "https://api-dev.test.com", // target api
      pathRewrite: { "^/dev": "" }  // /dev를 ""로
    },
    "/prod": {
      target: "https://api.test.com", // target api
      pathRewrite: { "^/prod": "" } // /prod를 ""로
    },
  },
```



#### plugins/axios.js proxy 추가
> proxy 허용 axios는 baseUrl 설정X -> proxy target으로 호출
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

