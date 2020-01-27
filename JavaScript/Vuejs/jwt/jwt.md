
## jwt
npm install: 
1. `npm install jsonwebtoken`
2. `npm install vue-cookies --save`

<br>

## get cookies token
```javascript

import VueCookies from 'vue-cookies'
import JsonWebToken from 'jsonwebtoken'

export default {

  checkAuth() {
    const jwt = VueCookies.get('test')
    const jwtDecode = JsonWebToken.decode(jwt)
    if(jwt) {
      // 만료시간 체크
      if (jwtDecode.exp < (new Date().getTime() + 1) / 1000) return false
      return true
    } else {
      return false
    }
  },

  logout: function () {
    VueCookies.remove('test')
    VueCookies.remove('user-name')
    VueCookies.remove('user-id')
    VueCookies.remove('user-dept')

    alert('로그아웃 되었습니다.')

    window.location.href = '/signin'
  }
}

```

## router 인증 거치기
순서 
> 인증 필요 X 컴포넌트 <br>
> 인증 필요 컴포넌트 <br>
> 그외 /** 처리

```javascript
import Vue from 'vue'
import Router from 'vue-router'

// Containers
const DefaultContainer = () => import('@/containers/DefaultContainer')

// Views
const Dashboard = () => import('@/views/Dashboard')

import auth from './auth'

Vue.use(Router)

const requireAuth = () => (from, to, next) => {
  if (auth.checkAuth()) {
    return next()
  }
  next('/signin')
}

function configRoutes() {
  return [
    {
      path: '/signin',
      name: 'SignIn',
      component: SignIn
    },
    {
      path: '/',
      redirect: '/dashboard',
      name: 'Home',
      component: DefaultContainer,
      beforeEnter: requireAuth(),
      children: [
        {
          path: 'dashboard',
          name: 'Dashboard',
          component: Dashboard
        }
      ]
    },
    {
        path: '/**',
        beforeEnter: requireAuth()
    }
  ]
}

export default new Router({
  mode: 'history', // https://router.vuejs.org/api/#mode
  linkActiveClass: 'open active',
  scrollBehavior: () => ({ y: 0 }),
  routes: configRoutes()
})

```

> 모든 router 권한시 아래 코드 추가
```js
router.redirect({
  '*': '/'
})
```

<br>


### 로그인 html
```html
<template>
    <div class="app flex-row">
        <div class="container">
            <b-row class="justify-content-center">
                <b-col md="5">
                    <b-card-group>
                        <b-card no-body class="p-4">
                            <b-card-body>
                                <b-form v-on:submit.prevent="getToken">
                                    <h1>Sign In</h1>
                                    <p class="text-muted">Sign In</p>
                                    <b-input-group class="mb-3">
                                        <b-input-group-prepend><b-input-group-text><i class="icon-user"></i></b-input-group-text></b-input-group-prepend>
                                        <b-form-input type="text" class="form-control" placeholder="Login ID" autocomplete="username" v-model="loginId" autofocus required/>
                                    </b-input-group>
                                    <b-input-group class="mb-4">
                                        <b-input-group-prepend><b-input-group-text><i class="icon-lock"></i></b-input-group-text></b-input-group-prepend>
                                        <b-form-input type="password" class="form-control" placeholder="Password" autocomplete="current-password" v-model="password" required/>
                                    </b-input-group>
                                    <p v-if="errMsg" class="text-danger">{{ errMsg }}</p>
                                    <b-row>
                                        <b-col cols="8">
                                            <b-button variant="primary" class="px-4 float-right" type="submit">Sign In</b-button>
                                        </b-col>
                                    </b-row>
                                </b-form>
                            </b-card-body>
                        </b-card>
                    </b-card-group>
                </b-col>
            </b-row>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import VueCookies from 'vue-cookies'

export default {
    name: "SignIn",
    data(){
        return {
            loginId: '',
            password: '',
            errMsg: '',
            envURL: process.env.VUE_APP_API
        }
    },
    methods: {
        getToken : function() {
            var obj = this

            axios.post(obj.envURL+'/oauth/token', {
                    loginId: this.loginId,
                    password: this.password
                },
                {
                    headers: {
                        'Accept': 'application/hal+json',
                        'Content-Type': 'application/json'
                    }
                })
                .then(function (response) {
                    const data = response.data

                    if (response.status == 200 && data.code == "0000") {
                        const user = data._embedded.user
                        const token = user.token
                        // set cookie
                        VueCookies.set('Authorization', token)
                        VueCookies.set('user-name', user.name)
                        VueCookies.set('user-id', user.loginId)
                        VueCookies.set('user-dept', user.department)
                        window.location.href = '/'
                    } else {
                        obj.errMsg = data.message
                    }
                })
                .catch(function (error) {
                    obj.errMsg = error
                })
            return false
        }
    }
}
</script>

<style scoped>
.flex-row{
    padding-top: 100px
}
</style>

```