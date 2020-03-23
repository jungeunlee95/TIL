### b-tabs 리스트 타이틀 커스텀

```html
<b-tabs pills card vertical>
    <b-tab v-for="test in tests" v-bind:key="test.id"
           :title="`${test.code} [${test.name}]`">
        <b-card-text>
            <span v-if="keywordListItem(test.name).length === 0"> - </span>
            <h5>
                <span v-for="list in keywordListItem(test.name)"
                      v-bind:key="list.id">
                    <b-badge
                             v-bind:variant="list.inProgress===true ? 'danger' : 'light'"
                             class="m-1"
                             >
                        {{list.name}}
                    </b-badge>
                </span>
            </h5>
        </b-card-text>
    </b-tab>
</b-tabs>
```

```js
keywordListItem (keyword) {
    return this.testList
        ? this.testList.filter(item => item.name === keyword)
    : this.testList
}
```

