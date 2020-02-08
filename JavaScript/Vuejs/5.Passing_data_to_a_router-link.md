```
<router-link> </router-link> 를 통해 컴포넌트간 데이터를 교환하는 방법
```

<br>

### router 설정 예시
```js
import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Profile from '@/components/Profile'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile,
      props: true
    }
  ]
})
```
<br>

### roter-link를 통해 데이터를 **보낼** 컴포넌트 예시 1
```html
<template>
  <div class="hello">
      <router-link :to="{ name: 'Profile', params: { msg : 'Hello~ jungeun' } }">
         Go to your profile
      </router-link>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld'
}
</script>
```

### roter-link를 통해 데이터를 **보낼** 컴포넌트 예시 2
```html
<template>
  <div class="hello">
      <router-link :to="{ name: 'Profile', params: { msg } }">
         Go to your profile
      </router-link>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: `Hello~ jungeun`
    }
  }
}
</script>
```

### props를 통해 데이터를 **받을** 컴포넌트 예시

```html
<template>
    <div>
        {{ welcome }}  <!-- Hello~ jungeun 이 찍힘 -->
    </div>
</template>

<script>
export default {
    name: 'Profile',
    props: ['msg'],
    data() {
        return {
            welcome: 'This is my msg!!!!'
        }
    },
    mounted() {
        if (this.msg) {
            this.welcome = this.msg    
        }

    }
}
</script>
```
<br>

> 만약 위의 상황에서 props로 데이터를 받지 않고 welcome을 쓰고싶다면

> router 설정을 아래와 같이 해야함
> ```js
> {
>   path: '/profile',
>   name: 'Profile',
>   component: Profile,
>   props: false
> }
>
> ```
> 
