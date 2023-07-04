<template>
    <div>
        <div ref="chart1" style="width: 300px; height: 300px; float: left;"></div>
        <div ref="chart2" style="width: 300px; height: 300px; float: left;"></div>
        <div ref="chart3" style="width: 300px; height: 250px; float: left;"></div>
    </div>
</template>

<script>
import * as echarts from 'echarts/core'
import axios from 'axios';


export default {
    mounted() {
        // 在mounted鉤子中進行圖表渲染
        this.renderChart1();
        this.renderChart2();
        this.renderChart3();
    },
    methods: {
        renderChart1() {
            // 使用ECharts的API來渲染圖表
            const chart1 = echarts.init(this.$refs.chart1);
            // 設置圖表的配置選項
            const option1 = {
                title: {
                    text: '柱狀圖',
                    // subtext: '人氣角色統計',
                    left: 'center'
                },
                xAxis: {
                    type: 'category',
                    data: ['18~24歲', '24~40歲', '40~65歲', '65歲以上']
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                        name: '比例',
                        type: 'bar',
                        radius: '50%',
                        data: [150, 230, 224, 218],
                        showBackground: true,
                        backgroundStyle: {
                            color: 'rgba(180, 180, 180, 0.2)'
                        }
                    }
                ]
            }
            // 使用設置選項渲染圖表
            chart1.setOption(option1);
        },
        renderChart2() {
            // 使用ECharts的API來渲染圖表
            const chart2 = echarts.init(this.$refs.chart2);
            // 設置圖表的配置選項
            const option2 = {
                title: {
                    text: '折線圖',
                    // subtext: '人氣角色統計',
                    left: 'center'
                },
                xAxis: {
                    type: 'category',
                    data: ['18~24歲', '24~40歲', '40~65歲', '65歲以上']
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                        data: [150, 230, 224, 218],
                        type: 'line'
                    }
                ]
            };
            // 使用設置選項渲染圖表
            chart2.setOption(option2);
        },
        renderChart3() {
            // 使用ECharts的API來渲染圖表
            const chart3 = echarts.init(this.$refs.chart3);
            // 設置圖表的配置選項
            const option3 = {
                title: {
                    text: '條狀'
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'shadow'
                    }
                },
                legend: {},
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                xAxis: {
                    type: 'value',
                    boundaryGap: [0, 0.01]
                },
                yAxis: {
                    type: 'category',
                    data: ['18~24歲', '24~40歲', '40~65歲', '65歲以上']
                },
                series: [
                    {
                        // name: '2011',
                        type: 'bar',
                        data: [150, 230, 224, 218]
                    }
                ]
            };
            // 使用設置選項渲染圖表
            chart3.setOption(option3);
        },
    },
};
</script>

<style>
* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}

html,
body {
    width: 100%;
    height: 100%;
    background-color: #e9e9e9;
    display: flex;
    justify-content: center;
    align-items: center;
}

#app {
    width: 100%;
    height: 100%;
    padding: 80px;
}

.container {
    width: 100%;
    height: 100%;
    background-color: #fff;
    border-radius: 5px;
}</style>
