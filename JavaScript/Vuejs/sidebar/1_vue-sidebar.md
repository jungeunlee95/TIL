https://yaminncco.github.io/vue-sidebar-menu/#/

https://github.com/yaminncco/vue-sidebar-menu/blob/master/src/components/SidebarMenu.vue

npm

`npm i vue-sidebar-menu --save`



<br>



main.js

```js
import VueSidebarMenu from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'

Vue.use(VueSidebarMenu)
```



<br>

component

```html
<sidebar-menu :menu="menu" :theme="theme"/>
```

```js
import { SidebarMenu } from 'vue-sidebar-menu'

export default {
    name: 'test',
    components: {SidebarMenu},
    data: function () {
        return {
            menu: [
                {
                    href: '/',
                    title: 'Dashboard',
                    icon: 'fa fa-user'
                },
                {
                    href: '#',
                    title: 'Charts',
                    icon: 'fa fa-chart-area'
                }
            ],
            theme: {
                type: 'white-theme',
                default: ''
            }
        }
    }
}
```



