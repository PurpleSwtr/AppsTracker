<script setup lang="ts">
import AppStat from '@/components/AppStat.vue'
import BaseButton from '@/components/BaseButton.vue'
import { ref, onMounted } from 'vue'

interface StatData {
  title: string
  icon: string
  value: number
  time: number
}

const stats = ref<StatData[]>([])

onMounted(async () => {
  if (window.pywebview?.api?.get_all_time_stats) {
    const rawData = await window.pywebview.api.get_all_time_stats()
    const maxTime = Math.max(...rawData.map((s) => s.total_time), 1)

    stats.value = rawData.map((item) => ({
      title: item.name,
      icon: `/icons/${item.name}.ico`,
      time: item.total_time,
      value: Math.round((item.total_time / maxTime) * 100),
    }))
  }
})
</script>

<template>
  <div>
    <div class="grid grid-cols-3 items-center justify-items-center">
      <BaseButton><img src="/system_icons/arrow-left.svg" /></BaseButton>
      <p class="text-center font-medium">Всё время</p>
      <BaseButton><img src="/system_icons/arrow-right.svg" /></BaseButton>
    </div>

    <div class="mt-5 flex flex-col gap-3">
      <AppStat
        v-for="(stat, idx) in stats"
        :key="idx"
        :title="stat.title"
        :value="stat.value"
        :time="stat.time"
        :icon="stat.icon"
      />
    </div>
  </div>
</template>
