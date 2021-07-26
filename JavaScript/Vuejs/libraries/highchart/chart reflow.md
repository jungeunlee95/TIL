- 차트 반응형 적용
  - 사이드바 클릭시 반응형 사이즈가 적용이 안되는 현상

**sidebar event**

- 컴포넌트 이벤트 적용: `v-on:click.native`

```vue
<template>
    <AppHeader fixed>
      <SidebarToggler v-on:click.native="setSidebarToggle" class="d-lg-none" display="md" mobile />
    </AppHeader>
</template>
<script>
import { Header as AppHeader, SidebarToggler } from '@coreui/vue'
import DefaultHeaderDropdownAccnt from './DefaultHeaderDropdownAccnt'

export default {
  name: 'DefaultHeader',
  data(){
    return {
    }
  },
  methods: {
    setSidebarToggle () {
        this.$store.commit('setSidebarToggle', {sidebarToggle: !this.$store.getters.getSidebarToggle})
    }
  },
  components: {
    AppHeader,
    DefaultHeaderDropdownAccnt,
    SidebarToggler
  }
}
</script>
```



**chart**

```js
<template>
    <div class="text-center">
        <b-spinner v-if="loading" label="Loading..."></b-spinner>
    	<highcharts :options="chartOptions"></highcharts>
    </div>
</template>

<script>
import {Chart} from 'highcharts-vue'
import * as moment from 'moment'

export default {
    name: 'Reflow',
    components: {
        highcharts: Chart
    },
    props: {
        regionCode: String,
        clusterId: Number,
        collapsed: Boolean,
        proxyBackend: String
    },
    data: function () {
        return {
            loading: false,
            selectTime: 1,
            selectType: 'day',
            selectStep: 240,
            chartOptions: {
                chart: {
                    type: 'area',
                    // height: 300
                },
                title: {
                    text: 'Reflow'
                },
                xAxis: {
                    type: 'datetime',
                    minPadding: 0,
                    maxPadding: 0
                },
                yAxis: {
                    title: {
                        text: ''
                    },
                    labels: {
                        format: '{value} s'
                    }
                },
                plotOptions: {
                    series: {
                        fillOpacity: 0.1
                    }
                },
                tooltip: {
                    shared: true,
                    formatter: function () {
                        let text = moment(this.points[0].x).format('YYYY-MM-DD H:mm:ss')
                        this.points.forEach(data => {
                            text += `<br><span style="color:${data.color}">●</span> ${data.series.name}: <b>${Math.abs(data.y)}</b>`
                        })
                        return text
                    }
                },
                series: [{
                    name: 'title',
                    data: [],
                    color: 'white'
                }]
            }
        }
    },
    methods: {
        reflowChart () {
            if (this.$children.length === 0 || !this.$children[1] || !this.$children[1].chart) return
            this.$children[1].chart.reflow()
        }
    },
    watch: {
        sidebarToggle: function () {
            setTimeout(() => { this.reflowChart() }, 300)
        }
    },
    computed: {
        sidebarToggle: function () {
            return this.$store.getters.getSidebarToggle
        }
    }
}
</script>

<style scoped>

    </style>

```



