<template>
  <div class="w-115 m-5">
    <NavigationBar v-model="activePage" :pages="pages" />
    <RouterView />
  </div>
</template>

<script setup lang="ts">
import NavigationBar from '@/components/NavigationBar.vue'
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

const pages = ['Главная', 'Приложения', 'Паттерны', 'Настройки']

const activePage = computed({
  get: () => (route.name as string) ?? 'Главная',
  set: (page: string) => {
    const pathMap: Record<string, string> = {
      Главная: '/',
      Приложения: '/apps',
      Паттерны: '/patterns',
      Настройки: '/settings',
    }
    const path = pathMap[page]
    if (path) {
      router.push(path)
    }
  },
})
</script>
