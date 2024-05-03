<template>
  <nav aria-label="Breadcrumb" :class="className" class="breadcrumb">
    <ol>
      <li
        v-for="(crumb, index) in breadcrumbs"
        :key="index"
        :class="{
          activePage: index === breadcrumbs.length - 1,
          notActive: index !== breadcrumbs.length - 1
        }"
      >
        <router-link :to="crumb.to"
          >{{ crumb.label }}
          <span
            class="mx-1 P100 text-[#8F95B2]"
            v-if="index !== breadcrumbs.length - 1"
          >
            >
          </span>
        </router-link>
      </li>
    </ol>
  </nav>
</template>

<script setup>
// interface Breadcrumb {
//   label: string;
//   to: string;
// }

defineProps({
  breadcrumbs: {
    type: Array ,
    required: true
  },
  className: {
    type: String
  }
});
</script>

<style scoped>
nav {
  padding: 0 !important;
}
.breadcrumb ol {
  list-style: none;
}

.breadcrumb li {
  display: inline-block;
}

.breadcrumb li.activePage {
  color: #dd5928;
}

.breadcrumb li.notActive {
  color: #8f95b2;
}
</style>
