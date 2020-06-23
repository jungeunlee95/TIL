
[TOC]

------

https://github.com/gluons/vue-highlight.js/

<br>

## npm

`npm install --save vue-highlightjs`

`npm install highlight.js vue-highlight.js`

<Br>

### supported languages

https://github.com/highlightjs/highlight.js/blob/master/SUPPORTED_LANGUAGES.md



<br>

### main.js

```js
// Highlight.js languages (Only required languages)
import VueHighlightJS from 'vue-highlight.js'
import 'vue-highlight.js/lib/allLanguages'
import 'highlight.js/styles/default.css'
Vue.use(VueHighlightJS)
```



<br>

### html

```html
    <!-- Code Block -->
    <highlight-code lang="shell">
      {{podLog}}
    </highlight-code>
```

