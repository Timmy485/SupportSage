import { defineStore } from "pinia";


export const useSupportSage = defineStore({
  id: 'SupportSage',
  state: () => ({
    user: {},
    showAll: false
  }),
  getters: {},
  actions: {},
  persist: true
})
