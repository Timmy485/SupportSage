<template>
  <div v-if="isLoading">
    <LoadingGif label="Getting documents..." />
  </div>
  <div class="mt-2 px-6 py-10 rounded-lg BG0 h-[90vh]">
    <p class="H700 N900">Available Documents</p>

    <div class="SPC-MT-500 ">
      <DocumentPreview />
    </div>
  </div>
</template>

<script setup>
import LoadingGif from '@/uiKit/LoadingGif.vue'
import DocumentPreview from '@/components/Documents/DocumentPreview.vue'
</script>
