<template>
  <button
    class="m-2 p-2 rounded-xl border-2 border-gray-300 transition-colors duration-200 hover:bg-gray-50 hover:cursor-pointer hover:border-red-400"
    :class="{ 'bg-red-100 border-orange-500 text-orange-700': active }"
  >
    <slot />
  </button>
</template>

<script setup lang="ts">
defineProps({
  active: {
    type: Boolean,
    default: false,
  },
})
</script>
