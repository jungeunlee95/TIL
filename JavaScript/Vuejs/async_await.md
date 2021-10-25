### Vuejs async, await

```js
export default {
    methods: {
        test () {
            let obj = this
            const data = [1,2,3,4,5]
            data.reduce((previous, current) => {
                return previous.then(async () => {
                    console.log('@@')
                    await obj.testc(current)
                })
            }, Promise.resolve())
        },
        async testc() {
            await this.$api.get('/test', {}).then(function (response) {
                if (response.status === 200) {
                    console.log('--')
                }
            }).catch(function (error) {
                console.log(error)
            })
        }
    },
        created() {
            this.test()
        }
}
```



console.log

![1635172921773](C:\Users\7040_64bit\AppData\Roaming\Typora\typora-user-images\1635172921773.png)
