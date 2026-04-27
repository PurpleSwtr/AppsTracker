<script setup lang="ts">
import { ref, onMounted } from 'vue'
import AppIconButton from '@/components/AppIconButton.vue'
import AddAppButton from '@/components/AddAppButton.vue'

interface AppData {
  id: number
  title: string
  icon: string
  value: number
}

const stats = ref<AppData[]>([])

async function loadApps() {
  if (window.pywebview?.api?.get_all_applications) {
    stats.value = await window.pywebview.api.get_all_applications()
  }
}

onMounted(loadApps)
</script>

<template>
  <div class="grid grid-cols-4 gap-5 pt-3 m-5">
    <AppIconButton v-for="stat in stats" :key="stat.id" :icon="stat.icon" :title="stat.title" />
    <AddAppButton @app-added="loadApps" />
  </div>
</template>
