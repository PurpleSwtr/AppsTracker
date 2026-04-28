<script setup lang="ts">
import AppStat from '@/components/AppStat.vue'
import BaseButton from '@/components/BaseButton.vue'
import { ref } from 'vue'

const stats = ref([
  { icon: '/icons/Beltmatic.ico', title: '7 Billion Humans', value: 65 },
  { icon: '/icons/paintdotnet.ico', title: 'Godot', value: 23 },
])
</script>

<template>
  <div>
    <div class="grid grid-cols-3 items-center justify-items-center">
      <BaseButton><img src="/system_icons/arrow-left.svg" /></BaseButton>
      <p class="text-center font-medium">Вчера</p>
      <BaseButton><img src="/system_icons/arrow-right.svg" /></BaseButton>
    </div>

    <div class="mt-5 flex flex-col gap-3">
      <AppStat
        v-for="(stat, idx) in stats"
        :key="idx"
        :title="stat.title"
        :value="stat.value"
        :icon="stat.icon"
      />
    </div>
  </div>
</template>
