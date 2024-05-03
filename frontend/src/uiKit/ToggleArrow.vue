<template>
  <div @click="$emit('show')">
    <div v-if="!isOpen">
      <svg
        :width="width"
        :height="height"
        viewBox="0 0 24 24"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M19.9201 8.95001L13.4001 15.47C12.6301 16.24 11.3701 16.24 10.6001 15.47L4.08008 8.95001"
          :stroke="stroke"
          stroke-width="1.5"
          stroke-miterlimit="10"
          stroke-linecap="round"
          stroke-linejoin="round"
        />
      </svg>
    </div>

    <div v-else>
      <svg
        :width="width"
        :height="height"
        viewBox="0 0 24 24"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M19.9201 15.05L13.4001 8.53001C12.6301 7.76001 11.3701 7.76001 10.6001 8.53001L4.08008 15.05"
          :stroke="stroke"
          stroke-width="1.5"
          stroke-miterlimit="10"
          stroke-linecap="round"
          stroke-linejoin="round"
        />
      </svg>
    </div>
  </div>
</template>

<script lang="ts" setup>
defineProps({
  isOpen: {
    type: Boolean,
    default: false
  },
  height: {
    type: String,
    default: "18"
  },
  width: {
    type: String,
    default: "18"
  },
  stroke: {
    type: String,
    default: "rgb(158, 158, 159)"
  }
});
</script>
