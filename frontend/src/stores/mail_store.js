import { defineStore } from 'pinia'

export const useUserMailRequest = defineStore({
  id: 'userMail',
  state: () => ({
    id: 0,
    mailBody: '',
    mailResponse: '',
    mailDate: '',
    mailSubject: '',
    mailSnippet: '',
    mailFrom: ''
  }),
  getters: {
    getId: (state) => state.id,
    getMailBody: (state) => state.mailBody,
    getMailResponse: (state) => state.mailResponse,
    getMailDate: (state) => state.mailDate,
    getMailSubject: (state) => state.mailSubject,
    getMailSnippet: (state) => state.mailSnippet,
    getMailFrom: (state) => state.mailFrom
  },
  actions: {
    setMailData(data) {
      this.id = data.id;
      this.mailBody = data.body
      this.mailResponse = data.response;
      this.mailDate = data.date;
      this.mailSubject = data.subject;
      this.mailSnippet = data.snippet;
      this.mailFrom = data.from;
    }
  }
})
