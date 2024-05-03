<template>
  <button
    :style="buttonStyle"
    :class="classes"
    class="flex items-center justify-center gap-1"
    @click.prevent.stop="handleClick"
    :disabled="disabled"
    :data-cy="dataCy"
  >
    <slot name="leadingSlot"></slot>
    <InsideButtonLoader v-if="loading" />
    {{ buttonLabel }}
    <slot> </slot>
  </button>
</template>

<script lang="ts" setup>
import { computed } from 'vue'
import InsideButtonLoader from './InsideButtonLoader.vue'

const props = defineProps({
  variant: {
    default: 'primary'
  },
  disabled: {
    type: Boolean,
    default: false
  },
  buttonLabel: {
    type: String,
    default: ''
  },
  loading: {
    type: Boolean,
    default: false
  },
  dataCy: {
    type: String,
    default: ''
  },
  class: {
    type: String,
    default: ''
  },
  buttonStyle: {
    type: Object
  }
})

const emit = defineEmits(['submit'])

const handleClick = () => {
  if (!props.disabled) {
    emit('submit')
  }
}
const classes = computed(() => {
  return `button ${props.variant} ${props.disabled ? 'disabled' : ''} ${props.class}`
})
</script>

<style scoped>
.button {
  padding: 8px 16px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 400;
  font-size: 16px;
  text-align: center;
}

.primary {
  background-color: #192199;
  color: #fff;
}

.primary:hover {
  background: #070d59;
}

.secondary {
  color: #192199;
}

.with_border {
  border: 1px solid #c3c3c3;
  color: #fff;
}
.next {
  border: 1px solid #070d59;
  color: #192199;
}

.disabled {
  opacity: 0.5;
  cursor: not-allowed;
  color: #c1c4d6;
  border: 1px solid #f3efef;
}
</style>
