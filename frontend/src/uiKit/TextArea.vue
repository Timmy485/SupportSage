<template>
  <div class="input_box" :class="className">
    <div class="mb-2 mt-4">
      <div class="flex justify-between labelDiv">
        <label
          :class="labelStyles"
          class="block mb-2 my-1 pt-0.5 P250 N800 dark:text-gray-300"
          for="branchName"
        >
          {{ label }}
        </label>
        <span
          v-if="requireTag"
          class="
            bg-red-100
            requiredSpan
            rounded-lg
            text-[#DD5928] text-xs
            px-1.5
            py-1.5
            mb-1.5
            my-2
            dark:bg-red-200 dark:text-red-900
          "
        >
          Required
        </span>
      </div>
      <textarea
        :class="textAreaHeight"
        id="default-input"
        :required="requireTag"
        :placeholder="placeholder"
        class="
         N800
          bg-gray-50
          border border-[#192199] 
          hover:border-[#8F95B2]
          rounded-lg
          focus:outline-[#192199] focus:ring-[#c9cfd7] focus:ring
          peer
          block
          dark:placeholder-gray-400
          dark:text-white
          dark:focus:ring-[#c9cfd7]
          p-2
        "
        :maxlength="maxlength"
        :value="modelValue"
        :disabled="disabled"
        @input.prevent="$emit('update:modelValue', $event.target.value)"
        v-bind="$attrs"
      >
      </textarea>
      <div
        v-if="showlength"
        class="flex mt-1 mb-3 justify-between count text-gray-400 text-xs"
      >
        <p
          class="flex R400 P100 w-full"
          v-if="modelValue && modelValue.length === maxlength"
        >
          You have reached your limit
        </p>
        <div class="flex w-full justify-end">
          {{ modelValue ? modelValue.length : 0 }}/{{ maxlength }}
        </div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
defineProps({
  type: {
    type: String,
    default: "text"
  },
  modelValue: {
    type: String,
    default: ""
  },
  placeholder: {
    type: String,
    default: ""
  },
  maxlength: {
    type: Number,
    default: 500
  },
  label: {
    type: String,
    default: ""
  },
  requireTag: {
    type: Boolean,
    default: false
  },
  className: {
    type: String,
    default: ""
  },
  labelStyles: {
    type: String,
    default: ""
  },
  textAreaHeight: {
    type: String,
    default: ""
  },
  showlength: {
    type: Boolean,
    default: true
  },
  disabled: {
    type: Boolean,
    default: false
  },
});
</script>
<style scoped>
.input_box {
  width: 100%;
}

textarea {
  width: 100% !important;
}

.count {
  text-align: end;
}

.identification {
  box-sizing: border-box;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding: 8px 16px;
  background: #ffffff;
  border: 0.5px solid #d8dae5;
  border-radius: 4px;
  width: 80%;
}

.identification:hover {
  cursor: pointer;
}

.titleSecond {
  font-family: "Work Sans", sans-serif;
  font-style: normal;
  font-weight: 700;
  font-size: 19.2px;
  line-height: 24px;
  color: #101840;
}

.requiredSpan {
  margin-bottom: 5px;
}

.inputdiv {
  width: 95%;
}
</style>
