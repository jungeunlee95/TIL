[TOC]

------

- table sort 커스텀으로 하기
  - custom sort는 Number가 아닌 특정 기준이 적용된 String
    - 해당 컬럼 외에는 모두 기본 Bootstrap용 sort 기준을 적용
  - 테스트 확인용으로 class가 아닌 style로 지정

------

```html
<b-table :items="mappingItems" :fields="mappingFields" thead-class="pointer"
         small head-variant="light" @head-clicked="setSortData">
    <template v-slot:head(testColumn)="data">
        {{data.label}}
        <div v-if="data.column !== currentSort" 
             style="display: inline-block; margin-top: 2px" 
             class="float-right">
            <!-- 부트스트랩용 이미지 그대로 사용: not select-->
            <img src="data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='101' height='101' view-box='0 0 101 101' preserveAspectRatio='none'%3e%3cpath fill='black' opacity='.3' d='M51 1l25 23 24 22H1l25-22zM51 101l25-23 24-22H1l25 22z'/%3e%3c/svg%3e" width="10" height="14" >
        </div>
        <div v-else style="display: inline-block; margin-top: 2px" class="float-right">
            <!-- 부트스트랩용 이미지 그대로 사용: top select-->
            <img v-if="currentSortDir === 'desc'" src="data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='101' height='101' view-box='0 0 101 101' preserveAspectRatio='none'%3e%3cpath fill='black' d='M51 1l25 23 24 22H1l25-22z'/%3e%3cpath fill='black' opacity='.3' d='M51 101l25-23 24-22H1l25 22z'/%3e%3c/svg%3e" width="10" height="14" >
            <!-- 부트스트랩용 이미지 그대로 사용: down select-->
            <img v-else src="data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='101' height='101' view-box='0 0 101 101' preserveAspectRatio='none'%3e%3cpath fill='black' opacity='.3' d='M51 1l25 23 24 22H1l25-22z'/%3e%3cpath fill='black' d='M51 101l25-23 24-22H1l25 22z'/%3e%3c/svg%3e" width="10" height="14" >
        </div>
    </template>

    ....
    
</b-table>
```

```js
export default {
    name: 'Test',
    data: function () {
        return {
            listItems: [
                ... data ...
            ],
            keyword1: '',
            keyword2: '',
            sortValue: {
                one: 1,
                two: 2,
                three: 3,
                four: 4,
                five: 5,
                six: 6
            },
            mappingFields: [
                {key: '#', label: '#', thStyle: {width: '50px'}},
                {key: 'id', label: 'id', sortable: true},
                {key: 'testColumn', label: 'Test column'},
                {key: 'name', label: 'name', sortable: true},
                {key: 'description', label: 'description', sortable: true}
            ],
            currentSort: '',
            currentSortDir: 'asc',
        }
    },
    methods: {
        // head 클릭시 호출되는 methods
        setSortData (name) {
            this.currentSort = name // column name
            this.currentSortDir = this.currentSortDir === 'asc' ? 'desc' : 'asc'
        }
    },
    computed: {
        // 검색과 특정 기준 sort를 적용
        mappingItems () {
            let returnItems =  this.keyword1 || this.keyword2 
            ? this.listItems.filter(
                item => item.keyword1.includes(this.keyword1) && item.keyword2.includes(this.keyword2)
            ) : this.listItems

            let obj = this
            if (this.currentSort === 'testColumn') {
                returnItems.sort(function (a, b) {
                    let modifier = 1
                    if (obj.currentSortDir === 'desc') {
                        modifier = -1
                    }
                    if (obj.sortValue[a.sortValue] > obj.sortValue[b.sortValue]) {
                        return 1 * modifier
                    }
                    if (obj.sortValue[a.sortValue] < obj.sortValue[b.sortValue]) {
                        return -1 * modifier
                    }
                    // a must be equal to b
                    return 0
                })
            }
            return returnItems
        }
    }
}
```

