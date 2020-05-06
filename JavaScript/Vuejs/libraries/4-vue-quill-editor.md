[TOC]

------

https://github.com/surmon-china/surmon-china.github.io/tree/source/projects/vue-quill-editor/nuxt

<br>

### npm

`npm install vue-quill-editor --save`

<br>

#### plugins/nuxt-quill-plugin.js

```js
import Vue from 'vue'
import VueQuillEditor from 'vue-quill-editor'

Vue.use(VueQuillEditor)
```

<br>

#### nuxt.config.js

```js
  css: [
    /* Import vue-quill-editor */
    '~/node_modules/quill/dist/quill.core.css',
    // for snow theme
    '~/node_modules/quill/dist/quill.snow.css',
    // for bubble theme
    '~/node_modules/quill/dist/quill.bubble.css'
  ],
  plugins: [
    { src: '~plugins/nuxt-quill-plugin', ssr: false }
  ],
```

<br>

#### example

```html
<template>
  <section class="container">
    <client-only>
      <quill-editor
        ref="editor"
        v-model="content"
        :options="editorOption"
        @blur="onEditorBlur($event)"
        @focus="onEditorFocus($event)"
        @ready="onEditorReady($event)"
      />
    </client-only>
  </section>
</template>

<script>
  export default {
    name: 'quill-example-nuxt',
    data () {
      return {
        content: '<p>I am Example</p>',
        editorOption: {
          // Some Quill options...
          theme: 'snow',
          modules: {
            toolbar: [
                ['bold', 'italic', 'underline', 'strike'],
                ['blockquote', 'code-block'],
                [{ 'header': 1 }, { 'header': 2 }],
                [{ 'list': 'ordered' }, { 'list': 'bullet' }],
                [{ 'script': 'sub' }, { 'script': 'super' }],
                [{ 'indent': '-1' }, { 'indent': '+1' }],
                [{ 'direction': 'rtl' }],
                [{ 'size': ['small', false, 'large', 'huge'] }],
                [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
                [{ 'color': [] }, { 'background': [] }],
                [{ 'font': [] }],
                [{ 'align': [] }],
                ['clean'],
                ['link', 'image', 'video']
            ]
          }
        }
      }
    },
    mounted() {
      console.log('App inited, the Quill instance object is:', this.$refs.editor.quill)
      setTimeout(() => {
        this.content = 'I was changed!'
      }, 3000)
    },
    methods: {
      onEditorBlur(editor) {
        console.log('editor blur!', editor)
      },
      onEditorFocus(editor) {
        console.log('editor focus!', editor)
      },
      onEditorReady(editor) {
        console.log('editor ready!', editor)
      }
    }
  }
</script>

<style lang="scss" scoped>
  .container {
    width: 60%;
    margin: 0 auto;
    padding: 50px 0;
    .quill-editor {
      min-height: 200px;
      max-height: 400px;
      overflow-y: auto;
    }
  }
</style>
```

