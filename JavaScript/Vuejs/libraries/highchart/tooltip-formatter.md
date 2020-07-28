```js
<script>
import {Chart} from 'highcharts-vue'
import * as Api from '@/api/index.js'
import * as moment from 'moment'

export default {
    components: {
        highcharts: Chart
    },
    data: function () {
        return {
            chartOptions: {
                chart: {
                    type: 'line',
                    height: 300
                },
                title: {
                    text: 'Title'
                },
                xAxis: {
                    type: 'datetime',
                    minPadding: 0.05,
                    maxPadding: 0.05
                },
                yAxis: {
                    title: {
                        text: ''
                    },
                    min: 0
                },
                tooltip: {
                    shared: true,
                    formatter: function() {
                        const weekdayNames = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                        const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "June",
                                            "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
                        const date = new Date(this.x)
                        return `<small>${weekdayNames[date.getDay()]}, ${monthNames[date.getMonth()]} ${date.getDate()},
${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}</small> <br>
<span style="color:${this.points[0].color}">●</span> ${this.points[0].series.name}:
<b>${parseFloat(this.y / Math.pow(1024, i)).toFixed(3) + sizes[i]}</b>`
                    }
                },
                series: []
            }
        }
    }


    ...

```

```js
formatter: function() {
    const weekdayNames = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "June",
                        "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
    const date = new Date(this.x)
    let sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB']
    if (this.y === 0) return '0 Byte'
    let i = parseInt(Math.floor(Math.log(this.y) / Math.log(1024)))
    return `<small>${weekdayNames[date.getDay()]}, ${monthNames[date.getMonth()]} ${date.getDate()},
${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}</small> <br>
<span style="color:${this.points[0].color}">●</span> ${this.points[0].series.name}:
<b>${parseFloat(this.y / Math.pow(1024, i)).toFixed(3) + sizes[i]}</b>`
}
```

