**참고**

```
https://codepen.io/CSWApps/pen/aVoBPW
https://www.npmjs.com/package/vue-select-infinite-scroll
```

---


vuejs select box option item을 가져와서 scroll paging 처리

model-select를 썼지만 다른 것도 상관없음.. 

vue에서 되도록 jquery 사용 안하는 것이 좋지만,, 

document.querySelector를 통해 id element를 가져와서 핸들링하는 방법임

<br>

**html** 
```html
<model-select
        :options="items"
        placeholder="select item"
        class="col-3"
        id="modelSelectTest"
>
</model-select>

<div class="loading" v-show="loading">
    <span class="fa fa-spinner fa-spin"></span>
</div>
```

<br>

**js** 

```js
import { ModelSelect } from 'vue-search-select'

export default {
    ...

    components: {ModelSelect},
    
    ...

    data () {
        return {

            ...

            items: [],
            loading: false,
            userCurrentPage: 1,
            userPage: {
                size: 10,
                totalElements: 0,
                totalPages: 0,
                number: 0
            },
        }
    },
    methods: {
        getUsers () {
            let obj = this
            this.loading = true
            Api.get('/users', {size: this.userPage.size, page: this.userCurrentPage}).then(function (response) {
                if (response.status === 200) {
                    obj.userPage = response.data.page
                    if (response.data.page.totalElements === 0) {
                        obj.users = []
                    } else {
                        obj.users = response.data._embedded.users
                        obj.users.forEach(function (user) {
                            obj.items.push({value: user.id + '', text: user.name + ' (' + user.loginId  + ')'})
                        })
                        obj.loading = false
                    }
                }
            }).catch(function (error) {
                console.log(error)
            })
        },
        loadMore () {
            this.userCurrentPage += 1
            this.getUsers()
        }
    },
    created () {
        this.getUsers()
    },
    mounted () {
        const listElm = document.querySelector('#modelSelectTest')
        listElm.addEventListener('scroll', () => {
            // 스크롤 바닥에 닿으면
            if(listElm.scrollTop + listElm.clientHeight >= listElm.scrollHeight) {
                // 만약 현재까지 가져온 데이터가 전체 데이터보다 적거나 같다면
                if (this.userPage.totalElements >= this.userPage.size * this.userCurrentPage) {
                    this.loadMore()
                }
            }
        });

    }
}

```

<br>

**loading css**

```css
    .loading {
        text-align: center;
        position: fix;
        color: #fff;
        z-index: 9;
        padding: 8px 18px;
        border-radius: 5px;
        left: 50%;
        top: 300px;
        background: cadetblue;
    }
```

<br>

## scroll paging, 검색 같이 하는 경우
검색 값이 있는 경우 -> 모든 데이터 검색
검색 값이 없는 경우 -> 스크롤 페이징

```js
let obj = this
const listElm = document.querySelector('.menu')
listElm.addEventListener('scroll', () => {
    if(listElm.scrollTop + listElm.clientHeight >= listElm.scrollHeight) {
        if (obj.userPage.totalElements >= obj.userPage.size * obj.userCurrentPage) {
            if (this.searchUserInput === '') obj.loadMore()
        }
    }
})
const searchInput = document.getElementsByTagName('input')[0]
searchInput.addEventListener('input', function () {
    obj.searchUserInput = this.value
    obj.users = null
})
searchInput.addEventListener('focusout', function () {
    if (obj.seletedUser === null) obj.searchUserInput = this.value
})
searchInput.addEventListener('mouseup', function () {
    obj.searchUserInput = ''
    obj.userCurrentPage = 1
})
```

