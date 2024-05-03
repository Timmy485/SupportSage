<template>
  <div v-if="isLoading">
    <LoadingGif label="Loading email..." />
  </div>
  <div class="mt-2 px-6 py-10 rounded-lg BG0">
    <div class="flex justify-between items-center">
      <p class="H700 N900">Mailing List</p>
      <ButtonComponent text="Get New Mail" data-cy="getNewMail" @click="getUpdate()" />
    </div>
    <div class="SPC-MT-500 overflow-scroll h-[70vh]">
      <AccordionComponent />
    </div>
  </div>
</template>

<script setup>
import ButtonComponent from '@/uiKit/ButtonComponent.vue'
import AccordionComponent from '@/components/Dashboard/AccordionComponent.vue'
import { getListOfNewMails, isLoading } from '@/types/mailPreview'
import LoadingGif from '@/uiKit/LoadingGif.vue'
const getUpdate = () => {
  getListOfNewMails()
  isLoading.value = false
}
</script>
