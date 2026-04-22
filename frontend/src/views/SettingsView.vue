<template>
  <div class="max-w-md mx-auto mt-8 p-4 space-y-3">
    <BaseOption v-model="notificationsEnabled" label="Включить уведомления" type="checkbox" />
    <BaseOption
      v-model="notificationsRepeat"
      label="Повтор напоминаний"
      type="checkbox"
      :disabled="!notificationsEnabled"
    />

    <BaseOption
      v-model="notificationInterval"
      label="Интервал напоминаний"
      type="slider"
      :min="0"
      :max="100"
      :step="1"
      :disabled="!notificationsEnabled"
    />

    <BaseOption v-model="timeLimitEnabled" label="Установить лимит времени" type="checkbox" />

    <BaseOption
      v-model="timeLimit"
      label="Лимит времени"
      type="slider"
      :min="0"
      :max="1"
      :step="0.01"
      :disabled="!timeLimitEnabled"
    />

    <BaseOption v-model="closedEnabled" label="Закрытие при превышении" type="checkbox" />

    <BaseOption
      v-model="timeForCloseLimit"
      label="Лимит превышения"
      type="slider"
      :min="0"
      :max="1"
      :step="0.01"
      :disabled="!closedEnabled"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import BaseOption from '@/components/BaseOption.vue'

const notificationsEnabled = ref(true)
const notificationsRepeat = ref(true)
const timeLimitEnabled = ref(true)
const closedEnabled = ref(true)

const notificationInterval = ref(75)
const timeLimit = ref(0.5)
const timeForCloseLimit = ref(60)
const disabledSetting = ref(false)
</script>
