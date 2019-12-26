## 1. coreui switch vuejs 

```html
<template>

...
    
    <c-switch class="mx-1" :class="{ 'text-primary': clusters.env==='DEV', 'text-primary': clusters.env}==='QA'" :checked=cluster.autoSync variant="pill"/>

...
</template>

<script>
    import { Switch as cSwitch } from '@coreui/vue'

    export default {
        name: "AppDeloySettingList",
        components: {cSwitch},
        ...
        ...
    }
</script>
```

## 2. bootstrap 
```html
<template>

...
    <!-- class binding not working ! :( -->
    <b-form-checkbox switch size="lg" class="mx-1" :checked=cluster.autoSync :class="{ 'primary': clusters.env==='DEV', 'warning': clusters.env}==='QA'"></b-form-checkbox>

...
</template>
```
