<template>
  <div>
    <vue-slider v-model="value"></vue-slider>
  </div>
</template>

<script>
  module.exports = {
    components: {
      VueSlider
    },
    data: function () {
      return {
        value: 0,
      }
    }
  }
</script>
