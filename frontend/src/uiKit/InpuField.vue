<template>
  <div class="input_box" :class="className">
    <div
      v-if="label"
      class="flex justify-between label-div"
      :class="labelStyle"
    >
      <label
        class="block mb-2 my-1 pt-0.5 P250 N800 dark:text-gray-300"
        :class="labelClass"
        for="department-name"
      >
        {{ label }}</label
      >

      <span
        v-if="requireTag"
        class="
          bg-red-100
          requiredSpan
          rounded-lg
          text-[#DD5928] text-xs
          py-1
          text-center
          px-2
          mb-1.5
          my-2
          dark:bg-red-200 dark:text-red-900
        "
      >
        Required
      </span>
      <span
        v-if="requireAll"
        class="
          bg-red-100
          requiredSpan
          rounded-lg
          text-[#DD5928] text-xs text-center
          px-2
          mb-1.5
          my-2
          dark:bg-red-200 dark:text-red-900
        "
      >
        All Fields Required
      </span>
    </div>
    <div class="flex relative">
      <span
        v-if="addSign"
        class="absolute pl-4 top-2 left-2 border-r-2 pr-4 text-gray-500"
        >{{ currency }}</span
      >
      <input
        :class="inputStyles"
        :style="inputFormStyle"
        :type="type"
        id="description"
        :required="requireTag"
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
        :placeholder="placeholder"
        :maxlength="maxlength"
        :value="modelValue"
        :min="minlength"
        @input="[$emit('update:modelValue', inputText?.value)]"
        ref="inputText"
        autocapitalize="off"
        v-bind="$attrs"
        :disabled="disabled"
      />
    </div>

    <div
      v-if="showlength"
      class="flex mt-1 justify-between count text-gray-400 text-xs"
    >
      <p class="flex R400 P100 w-full" v-if="modelValue?.length > maxlength">
        You have exceeded your limit
      </p>
      <p
        v-else-if="minlength && modelValue.length < minlength"
        class="flex R400 P100 w-full"
      >
        at least {{ minlength }} char
      </p>
      <div class="flex w-full justify-end" v-if="!disabled">
        {{ modelValue?.length }}/{{ maxlength }}
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { ref, watch, Ref } from "vue";

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
  label: {
    type: String,
    default: ""
  },
  requireTag: {
    type: Boolean,
    default: false
  },
  requireAll: {
    type: Boolean,
    default: false
  },
  maxlength: {
    type: Number,
    default: 50
  },
  minlength: {
    type: Number,
    required: false
  },
  showlength: {
    type: Boolean,
    default: true
  },
  inputFormStyle: {
    type: Object,
    default: {}
  },
  capitalize: {
    type: String,
    default: "on"
  },
  disabled: {
    type: Boolean,
    default: false
  },
  className: {
    type: String,
    default: ""
  },
  addSign: {
    type: Boolean,
    default: false
  },
  inputStyles: {
    type: String,
    default: ""
  },
  currency: {
    type: String,
    default: "\u20AC"
  },
  labelStyle: {
    type: String,
    default: ""
  },
  labelClass: {
    type: String,
    default: ""
  }
});

const emit = defineEmits(["update", "filled", "update:modelValue"]);

const inputText: Ref<HTMLInputElement | null> = ref(null);
watch(inputText, () => {
  emit("filled", inputText.value?.value);
});
</script>
<style scoped>
.input_box {
  width: 100%;
}
input {
  width: 100%;
  height: 42px;
}
.count {
  text-align: end;
}
.label-div {
  height: 40px;
}
input[disabled]:hover {
  border: #d8dae5;
}
</style>

<!-- Linear scale -->
