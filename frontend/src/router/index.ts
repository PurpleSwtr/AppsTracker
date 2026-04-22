import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AppsView from '@/views/AppsView.vue'
import PatternsView from '@/views/PatternsView.vue'
import SettingsView from '@/views/SettingsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'Главная', component: HomeView },
    { path: '/apps', name: 'Приложения', component: AppsView },
    { path: '/patterns', name: 'Паттерны', component: PatternsView },
    { path: '/settings', name: 'Настройки', component: SettingsView },
  ],
})

export default router
