<template>
  <div class="relative flex flex-row p-1">
    <div
      class="absolute top-1 bottom-1 bg-white rounded-xl border-2 border-orange-500 shadow-sm transition-all duration-300 ease-out"
      :style="{
        left: `${activeIndex * 25}%`,
        width: '25%',
      }"
    ></div>

    <button
      v-for="(page, index) in pages"
      :key="page.name"
      @click="emit('update:modelValue', page.name)"
      class="relative z-10 flex-1 flex items-center justify-center gap-2 py-2 px-3 text-xs font-medium transition-colors duration-200"
      :class="
        activeIndex === index
          ? 'text-orange-600'
          : 'text-gray-600 hover:text-gray-800 hover:cursor-pointer'
      "
    >
      <img :src="page.icon" class="w-4 h-4" />
      <span>{{ page.name }}</span>
    </button>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  pages: Array<{ name: string; icon: string }>
  modelValue: string
}>()

const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void
}>()

const activeIndex = computed(() => {
  return props.pages.findIndex((page) => page.name === props.modelValue)
})
</script>
