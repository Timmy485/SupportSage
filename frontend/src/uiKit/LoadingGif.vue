<template>
  <div
    class="fixed top-0 left-0 w-full h-full flex items-center justify-center flex-col bg-[#fff] bg-opacity-70 z-50"
  >
    <img src="../assets/LoadingIcon.gif " class="loader-logo" alt="loader-icon" />
    <p class="text-base text-gray-500">{{ label }}</p>
  </div>
</template>
<script setup lang="ts">
defineProps({
  label: {
    type: String,
    default: 'Loading...'
  }
})
</script>
<style scoped>
.loader {
  position: relative;
  margin-top: 40px;
}
</style>

