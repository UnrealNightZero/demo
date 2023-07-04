<template>
  <div >
    <my-chart></my-chart>
  </div>
</template>

<script>
import MyChart from './components/MyChart.vue';
export default {
  components: {
    MyChart,
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
  display:flex; 
  width: 100%;
  height: 100%;
  background-color: #fff;
  border-radius: 5px;
}
.flex-container{

flex-flow:row wrap;
align-items: flex-start;
border: 1px #555 dashed;
height:300px;
width:250px;
background-color:#aaa;
align-items: stretch;/*以每一box為單位的內部對齊方式*/
align-content:space-around;/*以每一列為單位的對齊方式*/
}
</style>
