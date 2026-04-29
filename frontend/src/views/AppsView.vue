<script setup lang="ts">
import { ref, onMounted } from 'vue'
import AppIconButton from '@/components/AppIconButton.vue'
import AddAppButton from '@/components/AddAppButton.vue'
import BaseModal from '@/components/BaseModal.vue'
import CardApp from '@/components/CardApp.vue'

interface AppData {
  id: number
  title: string
  icon: string
  value: number
}

const isModalOpen = ref(false)
const modalData = ref({ icon: '', title: '' })

const openModal = () => (isModalOpen.value = true)
const closeModal = () => (isModalOpen.value = false)

function openApp(app: Pick<AppData, 'icon' | 'title'>) {
  modalData.value = app
  openModal()
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
    <AppIconButton
      v-for="stat in stats"
      :key="stat.id"
      :icon="stat.icon"
      :title="stat.title"
      @open-app="openApp(stat)"
    />
    <AddAppButton @app-added="loadApps" />

    <BaseModal :is-open="isModalOpen" @close="closeModal">
      <CardApp v-if="isModalOpen" :icon="modalData.icon" :title="modalData.title" />
    </BaseModal>
  </div>
</template>
