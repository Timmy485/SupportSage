<template>
  <svg
    width="24"
    height="25"
    viewBox="0 0 24 25"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      d="M9.02 3.69758L3.63 7.89758C2.73 8.59758 2 10.0876 2 11.2176V18.6276C2 20.9476 3.89 22.8476 6.21 22.8476H17.79C20.11 22.8476 22 20.9476 22 18.6376V11.3576C22 10.1476 21.19 8.59758 20.2 7.90758L14.02 3.57758C12.62 2.59758 10.37 2.64758 9.02 3.69758Z"
      :stroke="color"
      stroke-width="1.5"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
    <path
      d="M12 18.8477V15.8477"
      :stroke="color"
      stroke-width="1.5"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
  </svg>
</template>

<script setup lang="ts">
defineProps({
  color: {
    type: String,
    default: "none"
  }
});
</script>
