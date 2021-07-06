[TOC]





------

docs: https://vue-chartjs.org/

<hr>

### npm

`npm install vue-chartjs chart.js --save`

<br>



### sample

- [coreui](https://github.com/coreui/coreui-free-vue-admin-template/blob/v1/Vue_Full_Project/src/views/dashboard/CardBarChartExample.vue)
- [demo](https://coreui.io/demo/free/3.4.0/index.html)

```vue
<script> 
    import { Bar } from 'vue-chartjs'
    export default {
        extends: Bar,
        props: {
            type: String,
            backgroundColor: String,
            borderColor: String,
            testList: Array
        },
        data () {
            return {
                labels: [],
                data: []
            }
        },
        methods: {
            setData () {
                if (this.testList !== undefined || this.testList.length !== 0) {
                    this.labels = []
                    this.data = []
                    this.testList.forEach(item => {
                        this.labels.push(item.time)
                        this.data.push(Math.round(item.value, 2))
                    })
                }
            }
        },
        mounted () {
            this.setData(),
            this.renderChart({
                labels: this.labels,
                datasets: [
                    {
                        borderSkipped: 'left',
                        backgroundColor: this.backgroundColor,
                        borderColor: this.borderColor,
                        data: this.data
                    }
                ]
            }, {
                maintainAspectRatio: false,
                cubicInterpolationMode: 'monotone',
                title: {
                    display: false
                },
                tooltips: {
                    enabled: true,
                    titleFontSize: 10,
                    bodyFontSize: 10,
                },
                legend: {
                    display: false
                },
                layout: {
                    padding: {
                        left: 10,
                        top: 10,
                        bottom: 5,
                        right: 10
                    }
                },
                scales: {
                    xAxes: [{
                        display: false,
                        gridLines: {
                            display: false
                        }
                    }],
                    yAxes: [{
                        display: false,
                        ticks: {
                            beginAtZero: true
                        },
                        gridLines: {
                            display: true
                        }
                    }]
                },
                elements: {
                    line: {
                        borderWidth: 3
                    },
                    point: {
                        radius: 4,
                        hitRadius: 10,
                        hoverRadius: 4,
                        hoverBorderWidth: 3
                    }
                },
                plugins: {
                    datalabels: {
                        formatter: function() {
                            return ''
                        }
                    }
                }
            })
        }
    }
</script>
```

