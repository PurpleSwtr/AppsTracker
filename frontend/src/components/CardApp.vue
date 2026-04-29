<template>
  <div class="w-100 h-70 bg-white rounded-2xl shadow-2xl outline-2 outline-gray-200 p-5 flex items">
    <img :src="icon" class="w-16 h-16 object-contain" />
    <p class="font-semibold text-lg pl-4">{{ title }}</p>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  icon: string
  title: string
}>()
</script>
