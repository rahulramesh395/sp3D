<template>
  <div>	
    <div class="slider-component">
      <div class="slidecontainer">
        <input
          ref="input"
          v-model="currentValue"
          type="range"
          :min="0"
          :max="100"
          class="slider"
          @input="onInput"
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    value: {
      type: Number,
      required: true
    },
    min: {
      type: Number,
      required: true
    },
    max: {
      type: Number,
      required: true
    },
    dof: {
      type: String,
      required: true
    }
  },
  data(){
    return {
      currentValue: ((this.value - this.min)*100)/(this.max-this.min),
      maxValue: this.max,
      minValue: this.min,
    };
  },
  methods: {
    onInput() {
     console.log(this.currentValue)
     const val = (this.minValue + (parseInt(this.currentValue)/100)*(this.maxValue - this.minValue))
     console.log(val)
     fetch('http://192.168.0.113:5000/' + this.dof + '/' + val)
        .then((response) => {
          return response.json()
        })
	.then((res) => {
	console.log(res)
	})
    }
  }
};
</script>

<style scoped>
.slider-component .slidecontainer {
	width: 100%;
}

.slider-component .slidecontainer .slider {
	-webkit-appearance: none;
	appearance: none;
	width: 100%;
	height: 4px;
	border-radius: 2px;
	background: #c2c2c2;
	outline: none;
	opacity: 0.7;
	-webkit-transition: .2s;
	transition: opacity .2s;
}

.slider-component .slidecontainer .slider:hover {
	opacity: 1;
}

.slider-component .slidecontainer .slider::-webkit-slider-thumb {
	-webkit-appearance: none;
	appearance: none;
	width: 18px;
	height: 18px;
	background: #D8A22E;
	cursor: pointer;
	border-radius: 50%;
}

.slider-component .slidecontainer .slider::-moz-range-thumb {
	width: 18px;
	height: 18px;
	background: #D8A22E;
	cursor: pointer;
	border-radius: 50%;
}
</style>
