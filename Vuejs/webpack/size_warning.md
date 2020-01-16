참고:

https://github.com/webpack/webpack/issues/3486

https://webpack.js.org/configuration/performance/#performance-maxentrypointsize

https://github.com/webpack/webpack/issues/3216


#### warning

```
WARNING in asset size limit: The following asset(s) exceed the recommended size limit (250 kB). This can impact web performance. Assets: bundle.js (10.3 MB)
```


### vue.config.js 추가

```js

const path = require('path')

module.exports = {
    outputDir: path.resolve(__dirname, '../src/main/resources/static'),
    assetsDir: 'static',
    chainWebpack: config => {
        config.performance
            .hints(false)
            .maxEntrypointSize(512000)
            .maxAssetSize(512000)
    }
}

```