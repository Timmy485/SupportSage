<template>
  <GDialog max-width="872" height="700" persistent>
    <div class="p-4">
      <div class="flex justify-between py-2">
        <h3 class="N900 H700">Edit User Response</h3>
        <CloseCircleSvg @click="handleCancel" class="cursor-pointer" />
      </div>
    </div>
    <div class="px-8">
      <InpuField
        label="Subject"
        type="text"
        data-cy="mailSubject"
        id="mailSubject"
        :requireTag="true"
        :showlength="false"
        v-model:modelValue="store.mailSubject"
      />

      <TextArea
        label="Body"
        :modelValue="store.mailBody"
        :maxlength="200"
        type="text"
        data-cy="mailBody"
        id="mailBody"
        :requireTag="true"
        @update:modelValue="(e) => handleModelValue(e)"
        disabled="true"
      />
      <div class="mt-4">
        <div class="flex justify-between">
          <p class="block mb-2 my-1 pt-0.5 P250 N800 dark:text-gray-300">Response</p>
          <span
            class="bg-red-100 requiredSpan rounded-lg text-[#DD5928] text-xs py-1 text-center px-2 mb-1.5 my-2 dark:bg-red-200 dark:text-red-900"
          >
            Required
          </span>
        </div>

        <QuillEditor
          contentType="html"
          theme="snow"
          style="
            .ql-editor {
              background: inherit;
              height: 200px;
            }
          "
          v-model:content="store.mailResponse"
        />
      </div>
      <div class="flex justify-end my-4">
        <ButtonsStyle :buttonLabel="'Cancel'" @submit="handleCancel" :variant="'secondary'" />
        <ButtonsStyle
          :disabled="disableSaveBtn"
          :buttonLabel="'Submit'"
          :variant="'primary'"
          @submit="handleSubmit"
        />
      </div>
    </div>
  </GDialog>
</template>

<script setup>
import InpuField from '@/uiKit/InpuField.vue'
import { GDialog } from 'gitart-vue-dialog'
import CloseCircleSvg from '@/uiKit/CloseCircleSvg.vue'
import ButtonsStyle from '@/uiKit/ButtonsStyle.vue'
import { useUserMailRequest } from '@/stores/mail_store'
import TextArea from '@/uiKit/TextArea.vue'
import { sendResponseToUser, getListOfNewMails, message } from '@/types/mailPreview'
import { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css';

const store = useUserMailRequest()
const emit = defineEmits(['closeDialog', 'errorAlert', 'successAlert', 'responseSubmit'])

const handleCancel = () => {
  emit('closeDialog')
}

const handleModelValue = (e) => {
  store.getMailBody = e
}

const dataToSend = () => {
  const data = {
    subject: store.getMailSubject,
    body: store.getMailBody,
    response: store.getMailResponse,
    id: store.getId,
    from: store.getMailFrom
  }
  return data
}

const handleSubmit = () => {
  sendResponseToUser(dataToSend())
  if (message.value !== "") {
    handleCancel()
    successNotification()
    setTimeout(() => {
      getListOfNewMails()
    }, 1500);
  } else {
    handleCancel()
    setTimeout(() => {
      errorNotification()
    }, 1500);
    
  }
}

const successNotification = () => {
  toast.success('Email sent successfully, 😉', {
    position: toast.POSITION.TOP_RIGHT,
    transition: toast.TRANSITIONS.SLIDE
  })
}

const errorNotification = () => {
  toast.error('Faile to send email, 😢', {
    position: toast.POSITION.TOP_RIGHT,
    transition: toast.TRANSITIONS.SLIDE
  })
}
</script>
