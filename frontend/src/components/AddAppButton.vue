<template>
  <div>
    <label :for="fileInputId" style="cursor: pointer">
      <AppIconButton icon="src/assets/plus.svg" title="Добавить" />
    </label>

    <input type="file" :id="fileInputId" style="display: none" @change="onFileChanged" />
  </div>
</template>

<script setup lang="ts">
import AppIconButton from '@/components/AppIconButton.vue'

const fileInputId = 'hidden-file-input'

const onFileChanged = (event: Event) => {
  const file = (event.target as HTMLInputElement)?.files?.[0]
  console.log(file)
}
</script>
