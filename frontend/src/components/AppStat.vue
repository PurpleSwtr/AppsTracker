<template>
  <div
    class="border-2 border-gray-200 p-2 rounded-xl flex flex-row items-center gap-5 hover:cursor-pointer hover:bg-gray-50 transition-all duration-100 ease-out"
  >
    <img :src="icon" class="w-10 h-10 shrink-0 object-contain" />

    <p class="font-normal text-sm truncate flex-1 min-w-0" :title="title">{{ title }}</p>

    <div class="w-48 bg-gray-200 rounded-full h-2 overflow-hidden shrink-0">
      <div
        class="bg-orange-600 h-full rounded-full transition-all duration-300 ease-out"
        :style="{ width: value + '%' }"
      ></div>
    </div>

    <p class="text-sm whitespace-nowrap shrink-0">{{ value }}%</p>
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  icon: { type: String },
  title: { type: String },
  value: { type: Number },
})
</script>
