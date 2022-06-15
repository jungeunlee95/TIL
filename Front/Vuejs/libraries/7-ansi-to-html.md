
[TOC]

------

https://www.npmjs.com/package/ansi-to-html

<br>

## npm

`npm i ansi-to-html`

<Br>

```html
<div class="log-scroll text-left">
    <pre class="bg-log">
        <span v-html="convertAnsiCode(logData)"></span>
        <span v-if="logData == null || logData.length===0">Log does not exist.<br></span>
      </pre>
</div>
```

```js
convertAnsiCode (log) {
    if (log === null) return
    const convert = new Convert()
    return convert.toHtml(log)
}
```

```css
.log-scroll {
    height: 79vh; 
    overflow-y: auto;
}
.bg-log {
    color: #DDDDDD;
    background-color: #444444;
}
```



