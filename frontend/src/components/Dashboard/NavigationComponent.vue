<template>
  <RouterLink :to="`${item?.route}`" class="">
    <div
      class="flex items-center gap-4 rounded-lg cursor-pointer my-4 py-3 px-4 hover:bg-[#e7fcff] w-auto"
      :class="$route.path === (`${item?.route}`) ? 'bg-[#e7fcff]' : ''"
    >
      <div :title="item?.label" v-if="!showSideNavList.showAll">
        <slot></slot>
      </div>
      <div v-else>
        <slot></slot>
      </div>
      <span
        class="text-base sm:hidden md:hidden lg:block xl:block whitespace-nowrap truncate w-52"
        :data-cy="dataCy"
        :class="$route.path === (`${item?.route}`) ? 'O400' : ''"
        v-if="showSideNavList.showAll"
        >{{ item?.label }}</span
      >
    </div>
  </RouterLink>
</template>
<script setup>
import { useRoute } from 'vue-router'
import { useSupportSage } from '@/stores/support_sage_store'

const $route = useRoute()
const showSideNavList = useSupportSage()
defineProps({
  item: {},
  dataCy: {
    type: String,
    default: ''
  }
})
</script>
