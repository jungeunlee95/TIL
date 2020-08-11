docs: https://innologica.github.io/vue2-daterange-picker/#usage

![1597122786516](assets/1597122786516.png)



- time-picker

![1597135127706](assets/1597135127706.png)

## npm

`npm i vue2-daterange-picker --save`



<br>

**impoty component**

```html
<date-range-picker
                   :time-picker="true"
                   class="mr-2"
                   ref="picker"
                   :opens="'false'"
                   :maxDate="new Date()"
                   :closeOnEsc="true"
                   v-model="findQuery.date"
                   @update="getSearchActionLogs()"
                   :locale-data="locale"
                   >
    <template v-slot:input="picker" style="min-width: 350px;">
        {{ myDateFormat(picker.startDate)}} - {{ myDateFormat(picker.endDate)}}
    </template>
</date-range-picker>
```

```js
import * as Api from '@/api/index.js'
import * as moment from 'moment'
import DateRangePicker from 'vue2-daterange-picker'
import 'vue2-daterange-picker/dist/vue2-daterange-picker.css'

export default {
    components: { DateRangePicker },
    data: function () {
        return {
            locale: {
                direction: 'ltr', //direction of text
                format: 'dd/mm/yyyy', //fomart of the dates displayed
                separator: ' - ', //separator between the two ranges
                applyLabel: 'Search',
                cancelLabel: 'Cancel'
            },
            findQuery: {
                date: {
                    startDate: new Date(),
                    endDate: new Date()
                }
            }
        }
    },
    methods: {
        myDateFormat (date) {
            if (!date) date = new Date()
            return moment(date).format('YYYY-MM-DD hh:mm:ss')
        },
        getSearchActionLogs() {
            console.log(moment(this.findQuery.date.endDate).format('DD/MM/YYYY'))
            console.log(moment(this.findQuery.date.startDate).format('DD/MM/YYYY'))
        },
}
```

