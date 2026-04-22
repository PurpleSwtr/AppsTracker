<template>
  <div class="flex flex-row gap-2 justify-center">
    <BaseButton
      v-for="pageName in pages"
      :key="pageName"
      :active="pageName === modelValue"
      @click="emit('update:modelValue', pageName)"
    >
      {{ pageName }}
    </BaseButton>
  </div>
</template>

<script setup lang="ts">
import BaseButton from './BaseButton.vue'

defineProps<{
  pages: string[]
  modelValue: string // активная страница (v-model)
}>()

const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void
}>()
</script>
