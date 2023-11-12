<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="railway">
    <PersonCardVue />
  </div>
</template>

<script setup lang="ts">
import PersonCardVue from './PersonCard.vue'
</script>

<style>
.railway {
  background: url("../../../assets/img/railways.png") center center/66% no-repeat;
}
</style>
