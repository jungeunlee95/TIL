[TOC]

https://yaminncco.github.io/vue-sidebar-menu/#/

https://github.com/yaminncco/vue-sidebar-menu/blob/master/src/components/SidebarMenu.vue

https://github.com/yaminncco/vue-sidebar-menu#item-properties

<br>

## npm

`npm i vue-sidebar-menu --save`



<br>



## main.js

```js
import VueSidebarMenu from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'

Vue.use(VueSidebarMenu)
```



<br>

## component

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



## list로 메뉴 만드는 경우 (match path only)

`exactPath: true` > match path only (ignore query and hash)

```html
<sidebar-menu 
              :menu="menus" 
              class="vsm_white-theme" 
              style="height: 100%; position: relative; background-color: #f4f4f4">
    
    <span slot="toggle-icon" @click="collapse = !collapse">
        <div style="width: 100%; height: 100%;">
            <font-awesome-icon icon="arrows-alt-h" class="text-muted mt-3" />
        </div>
    </span>
    
</sidebar-menu>
```

```js
computed: {
    menus: function () {
        const menu = []
        for (let menu of this.$store.getters.getMenus) {
            menu.push({
                href: {path: adminMenu.path}, 
                title: adminMenu.title, 
                icon: 'icon', 
                exactPath: true
            })
        }
        return menu
    }
```



<br>

## Alias (Menu path 추가)

```js
menu.push({
    href: {path: menu.path},
    title: menu.title,
    icon: 'icon',
    exactPath: true,
    alias: ['Side01', 'Side02'].includes(menu.title) ? menu.path + '/:sideMenu' : ''
})
```

