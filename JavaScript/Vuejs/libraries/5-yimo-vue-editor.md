[TOC]



https://github.com/yimogit/yimo-vue-editor/tree/master/example



#### npm

`npm install yimo-vue-editor --save`

<br>

#### plugins/yimo-vue-editor.js config 설정

```js
import Vue from 'vue'
import YimoVueEditor from 'yimo-vue-editor'

Vue.use(YimoVueEditor, {
  name: 'v-editor-app',//Custom name
  config: {
    uploadImgUrl:'/api/upload', // upload api
    printLog: false, // disabled console.log
    lang: {
      bold: 'Bold',
      underline: 'Underline',
      italic: 'Italic',
      forecolor: 'Color',
      bgcolor: 'Backcolor',
      strikethrough: 'Strikethrough',
      eraser: 'Eraser',
      source: 'Codeview',
      quote: 'Quote',
      fontfamily: 'Font family',
      fontsize: 'Font size',
      head: 'Head',
      orderlist: 'Ordered list',
      unorderlist: 'Unordered list',
      alignleft: 'Align left',
      aligncenter: 'Align center',
      alignright: 'Align right',
      link: 'Insert link',
      linkTarget: 'Open mode',
      text: 'Text',
      submit: 'Submit',
      cancel: 'Cancel',
      unlink: 'Unlink',
      table: 'Table',
      emotion: 'Emotions',
      img: 'Image',
      uploadImg: 'Upload',
      linkImg: 'Link',
      video: 'Video',
      width: 'width',
      height: 'height',
      location: 'Location',
      loading: 'Loading',
      searchlocation: 'search',
      dynamicMap: 'Dynamic',
      clearLocation: 'Clear',
      langDynamicOneLocation: 'Only one location in dynamic map',
      insertcode: 'Insert Code',
      undo: 'Undo',
      redo: 'Redo',
      fullscreen: 'Full screnn',
      openLink: 'open link',
      uploadPlaceTxt: 'uploading__',
      uploadTimeoutPlaceTxt: 'upload_timeout__',
      uploadErrorPlaceTxt: 'upload_error__'
    }
  },
  uploadHandler: (type, resTxt) => {//Upload processing hook
    if (type === 'success') {
      var res = JSON.parse(resTxt)//Do not process the default look at the return value bit image path
      if (res.status !== 1) {
        return null
      }
      return res.data
    } else if (type === 'error') {
      //todo toast
    } else if (type === 'timeout') {
      //todo toast
    }
    return 'upload failed__'
  }
})

```

<br>

#### nuxt.config.js

```js
  plugins: [
    { src: '~plugins/yimo-vue-editor', ssr: false }
  ],
```

<br>

#### example

```html
<yimo-vue-editor v-model="text"></yimo-vue-editor>
```

```js
import YimoVueEditor from 'yimo-vue-editor'

export default {
    ...
    components: {
        YimoVueEditor
    },
```

