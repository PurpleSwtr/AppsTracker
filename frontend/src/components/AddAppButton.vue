<template>
  <div>
    <AppIconButton
      icon="src/assets/plus.svg"
      title="Добавить"
      @click="pickExeFile"
      style="cursor: pointer"
    />
  </div>
</template>

<script setup lang="ts">
import AppIconButton from '@/components/AppIconButton.vue'

const emit = defineEmits<{
  (e: 'app-added'): void
}>()

async function pickExeFile() {
  try {
    const selectedFiles = await window.pywebview.api.open_file_dialog()

    if (selectedFiles?.[0]?.toLowerCase().endsWith('.exe')) {
      const filePath = selectedFiles[0]
      await window.pywebview.api.add_new_application(filePath)
      emit('app-added')
    }
  } catch (err) {
    console.error(err)
  }
}
</script>
