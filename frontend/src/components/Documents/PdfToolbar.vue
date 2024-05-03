<template>
  <div class="bg-[#f9f9f9] rounded-lg px-6 py-4 w-fit">
    <div class="flex gap-5 bg-[#302f2fea] text-white p-2">
      <div class="flex flex-col gap-2">
        <div class="flex">
          <ButtonsStyle
            :button-label="'Prev'"
            @submit="page = page > 1 ? page - 1 : page"
            :variant="'with_border'"
          />
          <span class="text-center p-2">{{ page }} / {{ pages }}</span>
          <ButtonsStyle
            :button-label="'Next'"
            @submit="page = page < pages ? page + 1 : page"
            :variant="'with_border'"
          />
        </div>
      </div>

      <div class="flex flex-col gap-2">
        <div class="flex">
          <ButtonsStyle
            :button-label="'-'"
            @submit="scale = scale > 0.25 ? scale - 0.25 : scale"
            :variant="'with_border'"
          />
          <span class="text-center p-2">{{ scale * 100 }}%</span>
          <ButtonsStyle
            :button-label="'+'"
            @submit="scale = scale < 2 ? scale + 0.25 : scale"
            :variant="'with_border'"
          />
        </div>
      </div>
    </div>
    <VuePDF v-if="pdf" :pdf="pdf" :page="page" :scale="scale" key="pdf-key" />
  </div>
</template>

<script setup>
import { ref,watch } from 'vue'
import { VuePDF, usePDF } from '@tato30/vue-pdf'
import ButtonsStyle from '@/uiKit/ButtonsStyle.vue'

const props = defineProps({
  activePdf: Object
})

const page = ref(1)
const scale = ref(1.5)
let pdf = null
let pages = 0

const loadPdf = () => {
  const { pdf: newPdf, pages: newPages } = usePDF(props.activePdf.source)
  pdf = newPdf
  pages = newPages
}

watch(() => props.activePdf, () => {
  loadPdf()
})

loadPdf()
</script>
