<template>
  <div
    class="border-2 border-gray-200 p-2 rounded-xl flex flex-row items-center gap-5 hover:cursor-pointer hover:bg-gray-50 transition-all duration-100 ease-out"
  >
    <img :src="icon" class="w-10 h-10 shrink-0 object-contain" />
    <p class="font-semibold text-sm truncate flex-1 min-w-0" :title="title">{{ title }}</p>

    <div class="flex flex-col items-center shrink-0 pr-4">
      <p class="text-sm whitespace-nowrap mb-1">{{ formattedTime }}</p>
      <div class="w-48 bg-gray-200 rounded-full h-2 overflow-hidden">
        <div
          class="bg-orange-600 h-full rounded-full transition-all duration-300 ease-out"
          :style="{ width: value + '%' }"
        ></div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps({
  icon: { type: String },
  title: { type: String },
  value: { type: Number },
  time: { type: Number, default: 0 },
})

const formatTime = (minutes: number): string => {
  if (minutes < 60) {
    return `${Math.round(minutes)} мин.`
  }
  const hours = Math.floor(minutes / 60)
  const mins = Math.round(minutes % 60)
  return `${hours} ч. ${mins} мин.`
}

const formattedTime = computed(() => formatTime(props.time))
</script>
