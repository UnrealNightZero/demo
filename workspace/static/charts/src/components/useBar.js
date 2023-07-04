// 按需引入
import * as echarts from 'echarts/core'
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent
} from 'echarts/components'

import { BarChart } from 'echarts/charts';
import { CanvasRenderer } from 'echarts/renderers';


echarts.use(
  [TitleComponent, TooltipComponent, LegendComponent, GridComponent, CanvasRenderer,BarChart]
)

const useBar = (element) => {
  // 初始化，傳入HTML element
  const barChart = echarts.init(element)

  // 封裝相關參數依需求訂製
  const setOption = data => {
    const option = {
      title: {
        text: '年齡分布',
        // subtext: '人氣角色統計',
        left: 'center'
      },
      xAxis: {
        type: 'category',
        data: ['18~24歲', '24~40歲', '40以上']
      },
      yAxis: {
        type: 'value'
      },
      series: [
        {
          name: '比例',
          type: 'bar',
          radius: '50%',
          data: data
        }
      ]
    }
    return barChart.setOption(option)
  }

  // 封裝resize，RWD會使用到
  const resize = () => barChart.resize()

  return { setOption, resize }
}

export default useBar