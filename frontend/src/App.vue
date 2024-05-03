<template>
  <div class="mobile_div main_view layout pb-4">
    <SideNav />
    <div class="larg_screen w-[95%] mx-auto pb-4 overflow-auto" :class="main_page">
      <div class="px-10 py-10 rounded-lg -z-50">
        <router-link to="/"></router-link>
        <router-view v-slot="{ Component }">
          <keep-alive>
            <component :is="Component" :key="Component" />
          </keep-alive>
        </router-view>
      </div>
    </div>
  </div>
</template>

<script setup>
import SideNav from './components/Dashboard/SideNav.vue'
</script>

<style lang="scss">
body {
  overflow-y: hidden;
 ::-webkit-scrollbar {
    width: 0;
    height: 0;
  }
}
::-webkit-scrollbar {
  width: 0;
  height: 0;
}
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 100%;
}
.main_view {
  background-color: #edeff5;
  background-repeat: no-repeat;
  background-position: center bottom;
  background-attachment: fixed;
  background-size: contain;
}
.main_page {
  box-sizing: border-box;
  margin-left: 100px;
  margin-top: 23px;
  height: 100vh;
  overflow: hidden;
}
/* SPACING */
/* Margin top scales */
.SPC-MT-100 {
  margin-top: 8px;
}
.SPC-MT-200 {
  margin-top: 16px;
}
.SPC-MT-300 {
  margin-top: 24px;
}
.SPC-MT-400 {
  margin-top: 32px;
}
.SPC-MT-500 {
  margin-top: 40px;
}
.SPC-MT-600 {
  margin-top: 48px;
}
/* Margin bottom Scales */
.SPC-MB-100 {
  margin-bottom: 8px;
}
.SPC-MB-200 {
  margin-bottom: 16px;
}
.SPC-MB-300 {
  margin-bottom: 24px;
}
.SPC-MB-400 {
  margin-bottom: 32px;
}
.SPC-MB-500 {
  margin-bottom: 40px;
}
.SPC-MB-600 {
  margin-bottom: 48px;
}
/* Margin Left Scales */
.SPC-ML-100 {
  margin-left: 8px;
}
.SPC-ML-200 {
  margin-left: 16px;
}
.SPC-ML-300 {
  margin-left: 24px;
}
.SPC-ML-400 {
  margin-left: 32px;
}
.SPC-ML-500 {
  margin-left: 40px;
}
.SPC-ML-600 {
  margin-left: 48px;
}
/* Margin Right Scales */
.SPC-MR-100 {
  margin-right: 8px;
}
.SPC-MR-200 {
  margin-right: 16px;
}
.SPC-MR-300 {
  margin-right: 24px;
}
.SPC-MR-400 {
  margin-right: 32px;
}
.SPC-MR-500 {
  margin-right: 40px;
}
.SPC-MR-600 {
  margin-right: 48px;
}
/* FONTSTYLES */
.H900 {
  font-weight: 700;
  font-size: 2.074rem;
  line-height: 40px;
}
.H800 {
  font-weight: 700;
  font-size: 1.728rem;
  line-height: 32px;
}
.H700 {
  font-weight: 700;
  font-size: 1.44rem;
  line-height: 28px;
}
.H600 {
  font-weight: 700;
  font-size: 1.2rem;
  line-height: 24px;
}
.H500 {
  font-weight: 700;
  font-size: 1rem;
  line-height: 24px;
}
.H400 {
  font-weight: 700;
  font-size: 0.833rem;
  line-height: 16px;
}
.H300 {
  font-weight: 700;
  font-size: 0.694rem;
  line-height: 12px;
}
.H200 {
  font-weight: 500;
  font-size: 0.694rem;
  line-height: 12px;
}
.H100 {
  font-weight: 700;
  font-size: 0.579rem;
  line-height: 12px;
}
.P300 {
  font-weight: 400;
  font-size: 1.2rem;
  line-height: 24px;
}
.P250 {
  font-weight: 600;
  font-size: 1rem;
  line-height: 24px;
}
.P200 {
  font-weight: 400;
  font-size: 1rem;
  line-height: 24px;
}
.P100 {
  font-weight: 400;
  font-size: 0.833rem;
  line-height: 16px;
}
.P50 {
  font-weight: 400;
  font-size: 0.5813rem;
  line-height: 12px;
}
/* COLOURS */
/* Neutrals */
.N900 {
  color: #101840;
}
.N800 {
  color: #474d66;
}
.N700 {
  color: #696f8c;
}
.N600 {
  color: #8f95b2;
}
.N500 {
  color: #c1c4d6;
}
.N400 {
  color: #d8dae5;
}
.N300 {
  color: #e6e8f0;
}
.N200 {
  color: #edeff5;
}
.N100 {
  color: #f4f6fa;
}
.N75 {
  color: #f9fafc;
}
.N50 {
  color: #fafbff;
}
.N0 {
  color: #ffffff;
}
.BG-N50 {
  background-color: #fafbff;
}
/* Orange (ACCENT COLOR) */
.O600 {
  color: #893516 !important;
}
.O500 {
  color: #b5461d !important;
}
.O400 {
  color: #192199 !important;
}
.O300 {
  color: #e47a53 !important;
}
.O200 {
  color: #eb9c7f !important;
}
.O100 {
  color: #f2beab !important;
}
.O50 {
  color: #fff0ea !important;
}
/* Red */
.R600 {
  color: #7d2828 !important;
}
.R500 {
  color: #a73636 !important;
}
.R400 {
  color: #d14343 !important;
}
.R300 {
  color: #ee9191 !important;
}
.R200 {
  color: #f4b6b6 !important;
}
.R100 {
  color: #f9dada !important;
}
.R50 {
  color: #fdf4f4 !important;
}
/* Green */
.G600 {
  color: #317159 !important;
}
.G500 {
  color: #429777 !important;
}
.G400 {
  color: #52bd94 !important;
}
.G300 {
  color: #a3e6cd !important;
}
.G200 {
  color: #dcf2ea !important;
}
.G100 {
  color: #eef8f4 !important;
}
.G50 {
  color: #f5fbf8 !important;
}
.mobile_div {
  display: flex;
}
.BG0 {
  background-color: #ffffff;
}
.BG-R400 {
  background-color: #d14343;
}
.BG-O50 {
  background-color: #fff0ea;
}
.BG-N600 {
  background-color: #d8dae5;
}
</style>
