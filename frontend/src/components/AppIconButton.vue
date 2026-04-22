<template>
  <div class="flex flex-col items-center gap-2 w-fit">
    <div
      class="w-20 h-20 outline-2 outline-gray-200 rounded-xl flex items-center justify-center shrink-0 hover:cursor-pointer hover:outline-red-400 hover:bg-red-100 duration-200 transition-colors"
    >
      <img :src="icon" class="w-10 h-10 object-contain" />
    </div>

    <p class="text-center text-sm font-medium max-w-[80px] line-clamp-2">{{ title }}</p>
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  icon: { type: String },
  title: { type: String },
})
</script>
