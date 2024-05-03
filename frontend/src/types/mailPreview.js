import { ref } from 'vue'
import axios from 'axios'

export const previewMode = ref(false)
export const isLoading = ref(false)

export const data = ref([])
export const message = ref('')
export async function getListOfNewMails() {
  isLoading.value = true
  try {
    const response = await axios.get('https://supportsage.onrender.com/read_emails')
    data.value = response.data
  } catch (error) {
    isLoading.value = false
    axios.error('Error fetching data:', error)
  }
  isLoading.value = false
}

export async function sendResponseToUser(data) {
  isLoading.value = true
  try {
    const response = await axios.post('https://supportsage.onrender.com/send_email', data)
    message.value = response.message
  } catch (error) {
    isLoading.value = false
    message.value = error
    axios.error('Error posting data:', error)
  }
  isLoading.value = false
}
