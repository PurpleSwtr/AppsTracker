<script setup lang="ts">
import AddAppButton from '@/components/AddAppButton.vue'
import AppIconButton from '@/components/AppIconButton.vue'
import { ref } from 'vue'

const stats = ref([
  { icon: '/icons/Beltmatic.ico', title: '7 Billion Humans', value: 65 },
  { icon: '/icons/paintdotnet.ico', title: 'Godot', value: 23 },
  { icon: '/icons/Beltmatic.ico', title: '7 Billion Humans', value: 65 },
  { icon: '/icons/paintdotnet.ico', title: 'Godot', value: 23 },
  { icon: '/icons/Beltmatic.ico', title: '7 Billion Humans', value: 65 },
  { icon: '/icons/paintdotnet.ico', title: 'Godot', value: 23 },
])
</script>

<template>
  <div class="grid grid-cols-4 gap-5 pt-3 m-5">
    <AppIconButton
      v-for="(stat, idx) in stats"
      :icon="stat.icon"
      :title="stat.title"
    ></AppIconButton>

    <AddAppButton></AddAppButton>
  </div>
</template>
