<template>
  <div
    class="flex items-center justify-between py-3 px-4 bg-white rounded-lg border-2 border-gray-200 transition-opacity duration-200"
    :class="{ 'opacity-50': disabled }"
  >
    <label
      class="text-gray-700 font-medium select-none"
      :class="{ 'cursor-pointer': type === 'checkbox' }"
    >
      {{ label }}
    </label>

    <!-- Правая часть в зависимости от типа -->
    <div class="flex items-center gap-4">
      <!-- Режим чекбокса -->
      <input
        v-if="type === 'checkbox'"
        type="checkbox"
        :checked="modelValue"
        :disabled="disabled"
        @change="$emit('update:modelValue', $event.target.checked)"
        class="w-5 h-5 text-orange-600 rounded border-gray-300 focus:ring-orange-500 cursor-pointer"
      />

      <!-- Режим слайдера + числовое поле -->
      <template v-else-if="type === 'slider'">
        <input
          type="range"
          :value="modelValue"
          :min="min"
          :max="max"
          :step="step"
          :disabled="disabled"
          @input="$emit('update:modelValue', clampValue(parseFloat($event.target.value)))"
          class="w-48 h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
        />
        <input
          type="number"
          :value="modelValue"
          :min="min"
          :max="max"
          :step="step"
          :disabled="disabled"
          @input="$emit('update:modelValue', clampValue(parseFloat($event.target.value) || min))"
          class="w-20 px-2 py-1 text-sm border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-orange-500 disabled:bg-gray-100"
        />
      </template>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  label: {
    type: String,
    required: true,
  },
  type: {
    type: String,
    validator: (value) => ['checkbox', 'slider'].includes(value),
    default: 'checkbox',
  },
  modelValue: {
    type: [Boolean, Number],
    required: true,
  },
  min: {
    type: Number,
    default: 0,
  },
  max: {
    type: Number,
    default: 100,
  },
  step: {
    type: Number,
    default: 1,
  },
  disabled: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['update:modelValue'])

const clampValue = (value) => {
  if (isNaN(value)) return props.min
  return Math.min(props.max, Math.max(props.min, value))
}
</script>
