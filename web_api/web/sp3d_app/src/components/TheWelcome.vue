<script setup>
import TheSlider from './TheSliderComponent.vue'
</script>

<template>
  <h5>X - Translation</h5>
  <div class="container">
	<TheSlider v-if=load dof="xTrans" :max=10 :min=-10 :value=xTrans :key=reset />
  </div>
  <h5>Y-Translation</h5>
  <div class="container">
        <TheSlider v-if=load dof="yTrans" :max=10 :min=-10 :value=yTrans :key=reset />
  </div>
  <h5>Z-Translation</h5>
  <div class="container">
        <TheSlider v-if=load dof="zTrans" :max=40 :min=25 :value="zTrans" :key=reset />
  </div>
  <h5>X-Rotation</h5>
  <div class="container">
        <TheSlider v-if=load dof="xRot" :max=1.57 :min=-1.57 :value=xRot :key=reset />
  </div>
  <h5>Y-Rotation</h5>
  <div class="container">
        <TheSlider v-if=load dof="yRot" :max=1.57 :min=-1.57 :value=yRot :key=reset />
  </div>
  <h5>Z-Rotation</h5>
  <div class="container">
        <TheSlider v-if=load dof="zRot" :max=1.57 :min=-1.57 :value=zRot :key=reset />
  </div>
  <div class="container">
	<button class="buttonStyle" @click="resetVals()">RESET</button>
  </div>
</template>
<script>
export default {
data: function() {
        return {
          xTrans: 0,
	  yTrans: 0,
          zTrans: 0,
	  xRot: 0,
          yRot: 0,
          zRot: 0,
          reset: 0,
	  load: false,
        }
},
mounted(){
	 fetch('http://192.168.0.113:5000/setValues')
        .then(response => {
           return response.json()
        })
        .then((res) => {
           this.xTrans = parseInt(res[0])
	   this.yTrans = parseInt(res[1])
           this.zTrans = parseInt(res[2])
           this.xRot = parseInt(res[3])
           this.yRot = parseInt(res[4])
           this.zRot = parseInt(res[5])
           this.load = true
        })
},
methods: {
  resetVals() {
	fetch('http://192.168.0.113:5000/reset')
        .then((response) => {
          return response.json()
        })
        .then((res) => {
	  console.log(res)
          this.reset +=1
        })	
  }
}
};
</script>
<style>
	.container {
		width: 100%;
		height: 7.5vh;
	}
        .buttonStyle {
		width: 100%;
        }
</style>
