<template>
  <div class="flex gap-6">
    <div
      class="bg-white border border-[#E6E8F0] rounded-lg shadow-md w-80 overflow-y-scroll h-[60vh]"
    >
      <div class="flex flex-col p-4 cursor-pointer">
        <div v-for="(pdf, index) in documents" :key="index" class="mb-2">
          <div
            class="flex gap-2 p-4 rounded-lg"
            :style="{ backgroundColor: pdf.isActive ? '#F4F6FA' : '' }"
            @click="setActivePdf(index)"
          >
            <div><PDFSvg /></div>
            <div>
              <p class="text-[#667085] P200">{{ pdf.title }}</p>
              <p class="N600 P100">{{ pdf.duration }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="flex-1 flex flex-wrap justify-center gap-6 w-fit overflow-scroll h-[75vh]">
      <div v-if="activePDF"><PdfToolbar :active-pdf="activePDF"/></div>
    </div>
  </div>
</template>

<script setup>
import PdfToolbar from './PdfToolbar.vue'
import PDFSvg from '@/uiKit/PDFSvg.vue'
import { ref, computed } from 'vue'

const documents = ref([
  {
    title: 'About Us and Services',
    duration: '2 min read',
    source: './src/assets/pdfs/about_us_and_services.pdf',
    isActive: true
  },
  {
    title: 'Terms and Conditions',
    duration: '2 min read',
    source: './src/assets/pdfs/terms_and_conditions.pdf',
    isActive: false
  },
  {
    title: 'Pricing',
    duration: '2 min read',
    source: './src/assets/pdfs/pricing.pdf',
    isActive: false
  }
])

const activePDF = computed(() => {
  return documents.value.find((doc) => doc.isActive)
})
const setActivePdf = (index) => {
  documents.value.forEach((pdf, i) => {
    pdf.isActive = i === index
  })
}
</script>
