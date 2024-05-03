<template>
  <div v-for="mail in data" :key="mail.id" class="flex gap-2">
    <div class="w-full p-2 border rounded-lg cursor-pointer mb-4">
      <div
        class="flex items-center justify-between"
        :class="mail.isOpen ? 'mb-4' : ''"
        @click="toggleItems(mail)"
      >
        <div class="flex gap-2 items-center">
          <p class="text-base N800">{{ mail.subject ? mail.subject : 'No Subject' }}</p>
        </div>
        <div class="flex gap-2">
          <ToggleArrow :is-open="mail?.isOpen" />
        </div>
      </div>

      <slot v-if="mail?.isOpen">
        <p class="text-base N600 border-t pt-2">{{ mail.body }}</p>
      </slot>
    </div>
    <button @click="handlePreview(mail)">
      <svg
        width="20"
        height="20"
        viewBox="0 0 16 16"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M7.33333 1.3335H6C2.66667 1.3335 1.33333 2.66683 1.33333 6.00016V10.0002C1.33333 13.3335 2.66667 14.6668 6 14.6668H10C13.3333 14.6668 14.6667 13.3335 14.6667 10.0002V8.66683"
          stroke="#192199"
          stroke-width="1.5"
          stroke-linecap="round"
          stroke-linejoin="round"
        />
        <path
          d="M10.6933 2.0135L5.44 7.26684C5.24 7.46684 5.04 7.86017 5 8.14684L4.71333 10.1535C4.60667 10.8802 5.12 11.3868 5.84667 11.2868L7.85333 11.0002C8.13333 10.9602 8.52667 10.7602 8.73333 10.5602L13.9867 5.30684C14.8933 4.40017 15.32 3.34684 13.9867 2.0135C12.6533 0.680168 11.6 1.10684 10.6933 2.0135Z"
          stroke="#192199"
          stroke-width="1.5"
          stroke-miterlimit="10"
          stroke-linecap="round"
          stroke-linejoin="round"
        />
        <path
          d="M9.94 2.7666C10.3867 4.35993 11.6333 5.6066 13.2333 6.05993"
          stroke="#192199"
          stroke-width="1.5"
          stroke-miterlimit="10"
          stroke-linecap="round"
          stroke-linejoin="round"
        />
      </svg>
    </button>
  </div>

  <EditUserMail v-model="previewMode" @closeDialog="handleClose" />
</template>

<script setup>
import ToggleArrow from '../../uiKit/ToggleArrow.vue'
import { previewMode } from '@/types/mailPreview'
import { data, getListOfNewMails } from '@/types/mailPreview'
import EditUserMail from './EditUserMail.vue'
import { useUserMailRequest } from '@/stores/mail_store'

const userMail = useUserMailRequest()
const toggleItems = (mail) => {
  mail.isOpen = !mail.isOpen
  // Close other emails
  for (let otherMail of data.value) {
    if (otherMail !== mail) {
      otherMail.isOpen = false
    }
  }
}
// getMails
getListOfNewMails()

function handlePreview(mail) {
  userMail.setMailData(mail)
  previewMode.value = true
}

function handleClose() {
  // Close modal
  previewMode.value = false
}
</script>
