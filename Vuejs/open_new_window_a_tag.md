`<a>`를 사용해서 새 윈도우 창 열기

> `target="_blank"` 속성 넣어주면 됨

<br>

```html

<a target="_blank" :href="'http://' + item.host + ':' + item.port">{{item.host}}:{{item.port}}</a>

```