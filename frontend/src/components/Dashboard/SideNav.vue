<template>
  <div class="settings h-[100vh] p-1 text-gray-500 bg-white border border-[#e6e8f0]">
    <div class="flex items-center cursor-pointer relative">
      <a href="javascript:void(0)" @click="routeUrl()" class="flex items-center">
        <div class="-ml-25 mt-4">
          <LogoSvg />
        </div>
        <p
          class="mt-4 text-[27px] N700 font-bold sm:hidden md:hidden lg:block xl:block mr-24"
          v-if="store.showAll"
        >
          supportSage
        </p>
      </a>
      <span
        class="absolute h-6 w-6 rounded-full flex items-center py-0 px-2 shadow-md BG0 top-10 -right-5"
        @click="store.showAll = !store.showAll"
      >
        <ArrowLeft v-if="store.showAll" />
        <ArrowRight v-else />
      </span>
    </div>
    <div class="flex flex-col justify-between">
      <NavigationComponent
        :item="{ label: 'Dashboard', route: '/' }"
        @mouseover="toggleOnDashboad(true)"
        @mouseout="toggleOnDashboad(false)"
        data-cy="dashboard"
      >
        <HomeIcon :color="onDashboard || $route.path === '/' ? '#192199' : '#c9cfd7'" />
      </NavigationComponent>
      <NavigationComponent
        :item="{ label: 'Document Preview', route: '/document-preview' }"
        @mouseover="toggleonDocument(true)"
        @mouseout="toggleonDocument(false)"
        data-cy="preview"
      >
        <DocumentSvg
          :color="onDocument || $route.path === '/document-preview' ? '#192199' : '#c9cfd7'"
        />
      </NavigationComponent>
    </div>
  </div>
</template>

<script setup>
import { useSupportSage } from '@/stores/support_sage_store'
import ArrowLeft from '@/uiKit/ArrowLeft.vue'
import ArrowRight from '@/uiKit/ArrowRight.vue'
import LogoSvg from '@/uiKit/LogoSvg.vue'
import DocumentSvg from '@/uiKit/DocumentSvg.vue'
import HomeIcon from '@/uiKit/HomeIcon.vue'
import NavigationComponent from './NavigationComponent.vue'
import { ref } from 'vue'

const store = useSupportSage()
const onDashboard = ref(false)
const onDocument = ref(false)
const toggleOnDashboad = (status) => {
  onDashboard.value = status
}
const toggleonDocument = (status) => {
  onDocument.value = status
}
</script>
