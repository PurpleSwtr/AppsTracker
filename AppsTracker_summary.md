
---

### 📄 `.env.example`

```ini
CHECK_INTERVAL = 1
SQLALCHEMY_ECHO = False
```

---

### 📄 `.gitignore`

```gitignore
# Python-generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# Virtual environments
.venv
.env
```

---

### 📄 `README.md`

```markdown

```

---

### 📄 `TODO.md`

```markdown
# TODO

## 1. Бэк

- [ ] Сделать слой РЕПОЗИТОРИЯ для паттернов
- [ ] Сделать слой СЕРВИСА для паттернов
- [ ] Настройки паттернов
  - [ ] Флаг повтора напоминаний
  - [ ] Интервал напоминаний о времени с прогрессом
  - [ ] Лимит времени в день
  - [ ] Напоминания о перерыве
  - [ ] Закрытие приложение при превышении
  - [ ] метрика: Время срабатывания
  - [ ] метрика: Превышение времени

## 2. Фронт

- [ ] Закрепление окна
  - [ ] Сделать функцию закрепления\открепления окна
  - [ ] Сделать также запоминанием позиции
```

---

### 📄 `pyproject.toml`

```toml
[project]
name = "appstracker"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "icoextract>=0.2.0",
    "psutil>=7.2.2",
    "python-dotenv>=1.2.2",
    "pywebview>=6.1",
    "schedule>=1.2.2",
    "sqlalchemy>=2.0.48",
    "wintoastcreator>=0.4.0",
]
```

---

### 📄 `settings.json`

```json
{
    "notifications": false
}
```

---

### 📄 `frontend/.gitignore`

```gitignore
# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

node_modules
.DS_Store
dist
dist-ssr
coverage
*.local

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?

*.tsbuildinfo

.eslintcache

# Cypress
/cypress/videos/
/cypress/screenshots/

# Vitest
__screenshots__/

# Vite
*.timestamp-*-*.mjs
```

---

### 📄 `frontend/.oxlintrc.json`

```json
{
  "$schema": "./node_modules/oxlint/configuration_schema.json",
  "plugins": ["eslint", "typescript", "unicorn", "oxc", "vue"],
  "env": {
    "browser": true
  },
  "categories": {
    "correctness": "error"
  }
}
```

---

### 📄 `frontend/.prettierrc.json`

```json
{
  "$schema": "https://json.schemastore.org/prettierrc",
  "semi": false,
  "singleQuote": true,
  "printWidth": 100
}
```

---

### 📄 `frontend/README.md`

```markdown
# appstracker

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VS Code](https://code.visualstudio.com/) + [Vue (Official)](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Recommended Browser Setup

- Chromium-based browsers (Chrome, Edge, Brave, etc.):
  - [Vue.js devtools](https://chromewebstore.google.com/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd)
  - [Turn on Custom Object Formatter in Chrome DevTools](http://bit.ly/object-formatters)
- Firefox:
  - [Vue.js devtools](https://addons.mozilla.org/en-US/firefox/addon/vue-js-devtools/)
  - [Turn on Custom Object Formatter in Firefox DevTools](https://fxdx.dev/firefox-devtools-custom-object-formatters/)

## Type Support for `.vue` Imports in TS

TypeScript cannot handle type information for `.vue` imports by default, so we replace the `tsc` CLI with `vue-tsc` for type checking. In editors, we need [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) to make the TypeScript language service aware of `.vue` types.

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Type-Check, Compile and Minify for Production

```sh
npm run build
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```
```

---

### 📄 `frontend/env.d.ts`

```typescript
/// <reference types="vite/client" />
```

---

### 📄 `frontend/eslint.config.ts`

```typescript
import { globalIgnores } from 'eslint/config'
import { defineConfigWithVueTs, vueTsConfigs } from '@vue/eslint-config-typescript'
import pluginVue from 'eslint-plugin-vue'
import pluginOxlint from 'eslint-plugin-oxlint'
import skipFormatting from 'eslint-config-prettier/flat'

// To allow more languages other than `ts` in `.vue` files, uncomment the following lines:
// import { configureVueProject } from '@vue/eslint-config-typescript'
// configureVueProject({ scriptLangs: ['ts', 'tsx'] })
// More info at https://github.com/vuejs/eslint-config-typescript/#advanced-setup

export default defineConfigWithVueTs(
  {
    name: 'app/files-to-lint',
    files: ['**/*.{vue,ts,mts,tsx}'],
  },

  globalIgnores(['**/dist/**', '**/dist-ssr/**', '**/coverage/**']),

  ...pluginVue.configs['flat/essential'],
  vueTsConfigs.recommended,

  ...pluginOxlint.buildFromOxlintConfigFile('.oxlintrc.json'),

  skipFormatting,
)
```

---

### 📄 `frontend/index.html`

```html
<!DOCTYPE html>
<html lang="">
  <head>
    <meta charset="UTF-8">
    <link rel="icon" href="/favicon.ico">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vite App</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.ts"></script>
  </body>
</html>
```

---

### 📄 `frontend/package.json`

```json
{
  "name": "appstracker",
  "version": "0.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "run-p type-check \"build-only {@}\" --",
    "preview": "vite preview",
    "build-only": "vite build",
    "type-check": "vue-tsc --build",
    "lint": "run-s lint:*",
    "lint:oxlint": "oxlint . --fix",
    "lint:eslint": "eslint . --fix --cache",
    "format": "prettier --write --experimental-cli src/"
  },
  "dependencies": {
    "pinia": "^3.0.4",
    "vue": "^3.5.31",
    "vue-router": "^5.0.4"
  },
  "devDependencies": {
    "@tailwindcss/vite": "^4.2.2",
    "@tsconfig/node24": "^24.0.4",
    "@types/node": "^24.12.0",
    "@vitejs/plugin-vue": "^6.0.5",
    "@vue/eslint-config-typescript": "^14.7.0",
    "@vue/tsconfig": "^0.9.1",
    "autoprefixer": "^10.4.27",
    "eslint": "^10.1.0",
    "eslint-config-prettier": "^10.1.8",
    "eslint-plugin-oxlint": "~1.57.0",
    "eslint-plugin-vue": "~10.8.0",
    "jiti": "^2.6.1",
    "npm-run-all2": "^8.0.4",
    "oxlint": "~1.57.0",
    "postcss": "^8.5.9",
    "prettier": "3.8.1",
    "tailwindcss": "^4.0.0",
    "typescript": "~6.0.0",
    "vite": "^8.0.3",
    "vite-plugin-vue-devtools": "^8.1.1",
    "vue-tsc": "^3.2.6"
  },
  "engines": {
    "node": "^20.19.0 || >=22.12.0"
  }
}
```

---

### 📄 `frontend/tsconfig.app.json`

```json
{
  "extends": "@vue/tsconfig/tsconfig.dom.json",
  "include": ["env.d.ts", "src/**/*", "src/**/*.vue"],
  "exclude": ["src/**/__tests__/*"],
  "compilerOptions": {
    // Extra safety for array and object lookups, but may have false positives.
    "noUncheckedIndexedAccess": true,

    // Path mapping for cleaner imports.
    "paths": {
      "@/*": ["./src/*"]
    },

    // `vue-tsc --build` produces a .tsbuildinfo file for incremental type-checking.
    // Specified here to keep it out of the root directory.
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.app.tsbuildinfo"
  }
}
```

---

### 📄 `frontend/tsconfig.json`

```json
{
  "files": [],
  "references": [
    {
      "path": "./tsconfig.node.json"
    },
    {
      "path": "./tsconfig.app.json"
    }
  ]
}
```

---

### 📄 `frontend/tsconfig.node.json`

```json
// TSConfig for modules that run in Node.js environment via either transpilation or type-stripping.
{
  "extends": "@tsconfig/node24/tsconfig.json",
  "include": [
    "vite.config.*",
    "vitest.config.*",
    "cypress.config.*",
    "playwright.config.*",
    "eslint.config.*"
  ],
  "compilerOptions": {
    // Most tools use transpilation instead of Node.js's native type-stripping.
    // Bundler mode provides a smoother developer experience.
    "module": "preserve",
    "moduleResolution": "bundler",

    // Include Node.js types and avoid accidentally including other `@types/*` packages.
    "types": ["node"],

    // Disable emitting output during `vue-tsc --build`, which is used for type-checking only.
    "noEmit": true,

    // `vue-tsc --build` produces a .tsbuildinfo file for incremental type-checking.
    // Specified here to keep it out of the root directory.
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.node.tsbuildinfo"
  }
}
```

---

### 📄 `frontend/vite.config.ts`

```typescript
import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue(), tailwindcss()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
})
```

---

### 📄 `frontend/src/App.vue`

```vue
<script setup lang="ts">
import DefaultLayout from './layouts/DefaultLayout.vue'
</script>

<template>
  <DefaultLayout />
</template>
```

---

### 📄 `frontend/src/main.ts`

```typescript
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import './assets/tailwind.css'
const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
```

---

### 📄 `frontend/src/assets/tailwind.css`

```css
@import 'tailwindcss';
```

---

### 📄 `frontend/src/components/AddAppButton.vue`

```vue
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

async function pickExeFile() {
  try {
    const selectedFiles = await window.pywebview.api.open_file_dialog()

    if (selectedFiles && selectedFiles.length > 0 && String(selectedFiles).includes('.exe')) {
      const filePath = selectedFiles[0]
      console.log('Выбранный файл:', filePath)
      window.pywebview.api.add_new_application(filePath)
    } else {
      console.log('Файл не выбран')
    }
  } catch (err) {
    console.error('Ошибка при выборе файла:', err)
  }
}
</script>
```

---

### 📄 `frontend/src/components/AppIconButton.vue`

```vue
<template>
  <div class="flex flex-col items-center gap-2 w-fit">
    <div
      class="w-20 h-20 outline-2 outline-gray-200 rounded-xl flex items-center justify-center shrink-0 hover:cursor-pointer hover:outline-red-400 hover:bg-red-100 duration-200 transition-colors"
    >
      <img :src="icon" class="w-10 h-10 object-contain" />
    </div>

    <p class="text-center text-sm font-medium max-w-[80px] line-clamp-2">{{ title }}</p>
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  icon: { type: String },
  title: { type: String },
})
</script>
```

---

### 📄 `frontend/src/components/AppStat.vue`

```vue
<template>
  <div
    class="border-2 border-gray-200 p-2 rounded-xl flex flex-row items-center gap-5 hover:cursor-pointer hover:bg-gray-50 transition-all duration-100 ease-out"
  >
    <img :src="icon" class="w-10 h-10 shrink-0 object-contain" />

    <p class="font-normal text-sm truncate flex-1 min-w-0" :title="title">{{ title }}</p>

    <div class="w-48 bg-gray-200 rounded-full h-2 overflow-hidden shrink-0">
      <div
        class="bg-orange-600 h-full rounded-full transition-all duration-300 ease-out"
        :style="{ width: value + '%' }"
      ></div>
    </div>

    <p class="text-sm whitespace-nowrap shrink-0">{{ value }}%</p>
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  icon: { type: String },
  title: { type: String },
  value: { type: Number },
})
</script>
```

---

### 📄 `frontend/src/components/BaseButton.vue`

```vue
<template>
  <button
    class="m-2 p-2 rounded-xl border-2 border-gray-300 transition-colors duration-200 hover:bg-gray-50 hover:cursor-pointer hover:border-red-400"
    :class="{ 'bg-red-100 border-orange-500 text-orange-700': active }"
  >
    <slot />
  </button>
</template>

<script setup lang="ts">
defineProps({
  active: {
    type: Boolean,
    default: false,
  },
})
</script>
```

---

### 📄 `frontend/src/components/BaseOption.vue`

```vue
<template>
  <div
    class="flex items-center justify-between py-3 px-4 bg-white rounded-lg border-2 border-gray-200 transition-opacity duration-200"
    :class="{ 'opacity-50': disabled }"
  >
    <label
      class="text-gray-700 font-medium select-none"
      :class="{ 'cursor-pointer': type === 'checkbox' }"
    >
      {{ label }}
    </label>

    <!-- Правая часть в зависимости от типа -->
    <div class="flex items-center gap-4">
      <!-- Режим чекбокса -->
      <input
        v-if="type === 'checkbox'"
        type="checkbox"
        :checked="modelValue"
        :disabled="disabled"
        @change="$emit('update:modelValue', $event.target.checked)"
        class="w-5 h-5 text-orange-600 rounded border-gray-300 focus:ring-orange-500 cursor-pointer"
      />

      <!-- Режим слайдера + числовое поле -->
      <template v-else-if="type === 'slider'">
        <input
          type="range"
          :value="modelValue"
          :min="min"
          :max="max"
          :step="step"
          :disabled="disabled"
          @input="$emit('update:modelValue', clampValue(parseFloat($event.target.value)))"
          class="w-48 h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
        />
        <input
          type="number"
          :value="modelValue"
          :min="min"
          :max="max"
          :step="step"
          :disabled="disabled"
          @input="$emit('update:modelValue', clampValue(parseFloat($event.target.value) || min))"
          class="w-20 px-2 py-1 text-sm border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-orange-500 disabled:bg-gray-100"
        />
      </template>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  label: {
    type: String,
    required: true,
  },
  type: {
    type: String,
    validator: (value) => ['checkbox', 'slider'].includes(value),
    default: 'checkbox',
  },
  modelValue: {
    type: [Boolean, Number],
    required: true,
  },
  min: {
    type: Number,
    default: 0,
  },
  max: {
    type: Number,
    default: 100,
  },
  step: {
    type: Number,
    default: 1,
  },
  disabled: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['update:modelValue'])

const clampValue = (value) => {
  if (isNaN(value)) return props.min
  return Math.min(props.max, Math.max(props.min, value))
}
</script>
```

---

### 📄 `frontend/src/components/NavigationBar.vue`

```vue
<template>
  <div class="flex flex-row gap-2 justify-center">
    <BaseButton
      v-for="pageName in pages"
      :key="pageName"
      :active="pageName === modelValue"
      @click="emit('update:modelValue', pageName)"
    >
      {{ pageName }}
    </BaseButton>
  </div>
</template>

<script setup lang="ts">
import BaseButton from './BaseButton.vue'

defineProps<{
  pages: string[]
  modelValue: string // активная страница (v-model)
}>()

const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void
}>()
</script>
```

---

### 📄 `frontend/src/layouts/DefaultLayout.vue`

```vue
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
```

---

### 📄 `frontend/src/router/index.ts`

```typescript
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
```

---

### 📄 `frontend/src/stores/counter.ts`

```typescript
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
})
```

---

### 📄 `frontend/src/views/AppsView.vue`

```vue
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

onMounted(async () => {
  if (window.pywebview?.api?.get_all_applications) {
    try {
      stats.value = await window.pywebview.api.get_all_applications()
    } catch (error) {
      console.error('Не удалось загрузить приложения:', error)
    }
  }
})
</script>

<template>
  <div class="grid grid-cols-4 gap-5 pt-3 m-5">
    <AppIconButton v-for="stat in stats" :key="stat.id" :icon="stat.icon" :title="stat.title" />
    <AddAppButton />
  </div>
</template>
```

---

### 📄 `frontend/src/views/HomeView.vue`

```vue
<script setup lang="ts">
import AppStat from '@/components/AppStat.vue'
import BaseButton from '@/components/BaseButton.vue'
import { ref } from 'vue'

const stats = ref([
  { icon: '/icons/Beltmatic.ico', title: '7 Billion Humans', value: 65 },
  { icon: '/icons/paintdotnet.ico', title: 'Godot', value: 23 },
])

// watch()
</script>

<template>
  <div>
    <div class="grid grid-cols-3 items-center justify-items-center">
      <BaseButton><-</BaseButton>
      <p class="text-center font-medium">Вчера</p>
      <BaseButton>-></BaseButton>
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
```

---

### 📄 `frontend/src/views/PatternsView.vue`

```vue
<template></template>
```

---

### 📄 `frontend/src/views/SettingsView.vue`

```vue
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
import { ref, watch } from 'vue'
import BaseOption from '@/components/BaseOption.vue'

const notificationsEnabled = ref(true)

watch(notificationsEnabled, (newVal) => {
  if (window.pywebview?.api?.set_notifications) {
    window.pywebview.api.set_notifications(newVal)
  }
})

const notificationsRepeat = ref(true)
const timeLimitEnabled = ref(true)
const closedEnabled = ref(true)

const notificationInterval = ref(75)
const timeLimit = ref(0.5)
const timeForCloseLimit = ref(60)
</script>
```

---

### 📄 `src/__init__.py`

```python

```

---

### 📄 `src/api.py`

```python
import webview

from src.applications.services import ApplicationService
from src.core.database import SessionLocal
from src import settings_manager

class Api:
    def set_notifications(self, enabled: bool):
        settings_manager.update_notifications_enabled(enabled)

    def get_all_applications(self):
        session = SessionLocal()
        try:
            app_service = ApplicationService(session)
            apps = app_service.repository.get_all()
            
            return [
                {
                    "id": app.id,
                    "title": app.name,
                    "process_name": app.process_name,
                    "icon": f"/icons/{app.name}.ico",
                    "value": int(app.total_time)
                }
                for app in apps
            ]
        finally:
            session.close()

    def open_file_dialog(self):
        result = webview.windows[0].create_file_dialog(
            dialog_type=webview.FileDialog.OPEN,
            allow_multiple=False,
            file_types=['Executables (*.exe)']
        )
        return list(result) if result else []


    def add_new_application(self, application_path):
        session = SessionLocal()
        try:
            app_service = ApplicationService(session)
            app_service.add_application(application_path=application_path)
        finally:
            session.close()
```

---

### 📄 `src/config.py`

```python
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_DIR = Path(__file__).resolve().parent.parent
    
    DATA_DIR = BASE_DIR / "data"
    DB_PATH = DATA_DIR / "data.db"
    ICONS_PATH = BASE_DIR / "frontend" / "public" / "icons"
    SETTINGS_FILE = "settings.json"

    CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 30))
    SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO", "False").lower() == "true"
    DEBUG_PYWEBVIEW_MODE = True

config = Config()
```

---

### 📄 `src/desktop.py`

```python
import threading
import time
import webview

from src.api import Api
from src.core.database import init_db, SessionLocal
from src.applications.services import ApplicationService
from src.tracking.manager import TrackerManager
from src.tracking.tracker import ProcessTracker
from src.config import config


def run_tracker():
    session = SessionLocal()
    try:
        app_service = ApplicationService(session)
        applications = app_service.repository.get_all()
        
        tracker_manager = TrackerManager()
        for app in applications:
            tracker = ProcessTracker(process_name=app.process_name, application_id=app.id)
            tracker_manager.add_application(tracker)

        while True:
            tracker_manager.update()
            time.sleep(config.CHECK_INTERVAL)
    except KeyboardInterrupt:
        pass
    finally:
        session.close()


def main():
    init_db()

    tracker_thread = threading.Thread(target=run_tracker, daemon=True)
    tracker_thread.start()

    FRONTEND_URL = "http://localhost:5173"
    
    # Когда сделаю билд
    # frontend_dist = Path(__file__).resolve().parent.parent / "frontend" / "dist"
    # FRONTEND_URL = str(frontend_dist / "index.html")
    api = Api()

    window = webview.create_window(
        title="AppsTracker",
        url=FRONTEND_URL,
        width=520,
        height=500,
        resizable=False,
        min_size=(520, 500),
        on_top=True,
        frameless=False,
        js_api=api
    )

    webview.start(debug=config.DEBUG_PYWEBVIEW_MODE)


if __name__ == "__main__":
    main()
```

---

### 📄 `src/main.py`

```python
import sys
from pathlib import Path
from typing import Sequence
from sqlalchemy import func, select
from src.core.database import engine, SessionLocal, init_db
from src.models import Base
from src.models import Application, AppSession
from enum import Enum, auto

from src.config import config
from src.utils.iconextract import save_icon


class Action(Enum):
    ADD_APPLICATION = auto()
    ADD_PATTERN = auto()
    
    START_SESSION = auto()
    END_SESSION = auto()
    
    EXIT = auto()

actions_descriptions = {
    "ADD_APPLICATION": "Добавить приложение",
    "ADD_PATTERN": "Создать паттерн отслеживания",
    "START_SESSION": "Действие начала сессии",
    "END_SESSION": "Действие конец сессии",
    "EXIT": "Выход",
}    

def get_process_name(link: str) -> str:
    link = link.strip('"').strip("'")
    return Path(link).name

def save_application_to_db(process_name: str) -> None:
    with SessionLocal() as session:
        app_name = process_name.replace(".exe", "")
        app = Application(name=app_name, process_name=process_name)
        session.add(app)
        session.commit()

def get_app_id(app_name: str) -> int | None:
    with SessionLocal() as session:
        stmt = select(Application.id).where(func.lower(Application.name) == func.lower(app_name))
        return session.execute(stmt).scalar_one_or_none()

def add_app_session(app_name: str):
    app_id = get_app_id(app_name=app_name)
    if app_id is not None:
        with SessionLocal() as session:
            app_session = AppSession(application_id=app_id, start_time=func.now())
            session.add(app_session)
            session.commit()
    else:
        raise ValueError("Запись не найдена")

def get_applications_process_names() -> list[str]:
    with SessionLocal() as session:
        names = session.scalars(select(Application.process_name)).all()
        return list(names)

def dubug_menu() -> Action:
    for i, elem in enumerate(actions_descriptions.values()):
        print(f"{i+1}. {elem}")

    user_input = input().strip()

    if user_input.isdigit():
        user_input = int(user_input)
    else: return Action.EXIT
    
    if int(user_input) > len(actions_descriptions) + 1:
        print("Ошибка ввода")
    
    match int(user_input) - 1:
        case 0: 
            return Action.ADD_APPLICATION
        case 1: 
            return Action.ADD_PATTERN
        case 2: 
            return Action.START_SESSION
        case 3: 
            return Action.END_SESSION
        case 4: 
            return Action.EXIT
        case _:
            return Action.EXIT

if __name__ == "__main__":
    init_db()
    print(get_applications_process_names())
    user_input = None
    while user_input != Action.EXIT:
        try:
            user_input = dubug_menu()
            match user_input:

                case Action.EXIT:
                    raise ValueError("Выход из программы")
                
                case Action.ADD_APPLICATION:
                    app = input("Перетащите приложение в окно программы...\n")
                    process_name = get_process_name(app)
                    save_application_to_db(process_name)
                    save_icon(Path(app), config.ICONS_PATH)

                case Action.START_SESSION:
                    app_name = input("Ожидание ввода названия приложения...\n")
                    print(get_app_id(app_name=app_name))
                    add_app_session(app_name=app_name)

        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            sys.exit(0)
```

---

### 📄 `src/models.py`

```python
from datetime import datetime

from sqlalchemy import Float, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.core.database import Base

class ApplicationPattern(Base):
    __tablename__ = "application_patterns"

    id: Mapped[int] = mapped_column(primary_key=True)
    application_id: Mapped[int] = mapped_column(ForeignKey("applications.id"))
    pattern_id: Mapped[int] = mapped_column(ForeignKey("patterns.id"))
    enabled: Mapped[bool] = mapped_column(default=True)


class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    process_name: Mapped[str] = mapped_column(String(100), nullable=False)
    total_time: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)

    sessions = relationship("AppSession", back_populates="application")
    patterns = relationship("Pattern", secondary="application_patterns", back_populates="applications")

class AppSession(Base):
    __tablename__ = "apps_sessions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    application_id: Mapped[int] = mapped_column(ForeignKey('applications.id'))
    process_id: Mapped[int] = mapped_column(nullable=True)
    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    application = relationship("Application", back_populates="sessions")

    
class Pattern(Base):
    __tablename__ = "patterns"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    title: Mapped[str] = mapped_column(String(20), nullable=False)
    message: Mapped[str] = mapped_column(String(100), nullable=False)
    
    notification_interval: Mapped[int] = mapped_column(Integer, nullable=False)
    close_interval: Mapped[int] = mapped_column(Integer, nullable=False)
    time_limit: Mapped[int] = mapped_column(Integer, nullable=False)

    repeat: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    close: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    applications = relationship("Application", secondary="application_patterns", back_populates="patterns")
```

---

### 📄 `src/process_manager.py`

```python
import time
import psutil
import sys
from enum import auto, Enum
from src.core.database import SessionLocal
from src.notifications.manager import send_notification

from src.config import config

from src.tracking.tracker import ProcessTracker
from src.tracking.manager import TrackerManager
from src.applications.services import ApplicationService

session = SessionLocal()

app_service = ApplicationService(session=session)

applications = app_service.repository.get_all()
tracker_manager = TrackerManager()
for app in applications:
    tracker = ProcessTracker(process_name=app.process_name, application_id=app.id)
    tracker_manager.add_application(tracker)

while True:
    tracker_manager.update()
    time.sleep(config.CHECK_INTERVAL)
```

---

### 📄 `src/settings_manager.py`

```python
import json
import os

from src.config import config

default_settings = {
    "notifications": True,
}

def load_settings():
    if not os.path.exists(config.SETTINGS_FILE):
        save_settings(default_settings)
        return default_settings
    
    with open(config.SETTINGS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_settings(settings):
    with open(config.SETTINGS_FILE, 'w', encoding='utf-8') as f:
        json.dump(settings, f, indent=4)

def update_notifications_enabled(enabled: bool):
    settings = load_settings()
    settings['notifications'] = enabled
    save_settings(settings)
```

---

### 📄 `src/applications/repository.py`

```python
from sqlalchemy import func, select
from src.models import Application, AppSession
from src.core.repository import BaseRepository
from sqlalchemy.orm import Session

class ApplicationRepository(BaseRepository[Application]):
    def __init__(self, session: Session):
        super().__init__(session, Application)

    def get_by_name(self, name: str) -> Application | None:
        stmt = select(Application).where(func.lower(Application.name) == func.lower(name))
        return self.session.execute(stmt).scalar_one_or_none()

    def get_by_process_name(self, process_name: str) -> Application | None:
        stmt = select(Application).where(Application.process_name == process_name)
        return self.session.execute(stmt).scalar_one_or_none()

    def create_from_process(self, process_name: str) -> Application:
        app_name = process_name.replace(".exe", "")
        return self.create(name=app_name, process_name=process_name)

    def add_session(self, application_id: int) -> AppSession:
        from datetime import datetime
        session_obj = AppSession(
            application_id=application_id,
            start_time=datetime.now()
        )
        self.session.add(session_obj)
        self.session.commit()
        return session_obj
    
    def save_application_to_db(self, process_name: str) -> None:
        app_name = process_name.replace(".exe", "")
        app = Application(name=app_name, process_name=process_name)
        self.session.add(app)
        self.session.commit()
```

---

### 📄 `src/applications/services.py`

```python
from pathlib import Path

from sqlalchemy.orm import Session
from src.applications.repository import ApplicationRepository
from src.models import Application, AppSession
from src.utils.iconextract import save_icon
from src.config import config

class ApplicationService:
    def __init__(self, session: Session):
        self.repository = ApplicationRepository(session)
        self.session = session
    
    @staticmethod
    def _get_process_name(link: str) -> str:
        link = link.strip('"').strip("'")
        return Path(link).name

    def get_all_applications_names(self) -> list[str]:
        apps = self.repository.get_all()
        apps_names = []
        for app in apps:
            apps_names.append(app.process_name)
        return apps_names

    def get_or_create_application(self, process_name: str) -> Application:
        app = self.repository.get_by_process_name(process_name)
        if not app:
            app = self.repository.create_from_process(process_name)
        return app

    def start_session(self, process_name: str) -> AppSession:
        app = self.get_or_create_application(process_name)
        return self.repository.add_session(app.id)

    def end_session(self, app_session_id: int) -> None:
        session_obj = self.session.get(AppSession, app_session_id)
        if session_obj:
            from datetime import datetime
            session_obj.end_time = datetime.now()
            self.session.commit()
    
    def add_application(self, application_path: str):
        process_name = self._get_process_name(application_path)
        self.repository.save_application_to_db(process_name)
        save_icon(Path(application_path), config.ICONS_PATH)
```

---

### 📄 `src/core/database.py`

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from src.config import config

config.DATA_DIR.mkdir(exist_ok=True)

class Base(DeclarativeBase):
    pass

engine = create_engine(
    f"sqlite:///{config.DB_PATH}",
    echo=config.SQLALCHEMY_ECHO,
)

def init_db() -> None:
    Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
```

---

### 📄 `src/core/repository.py`

```python
# src/core/repository.py
from typing import TypeVar, Generic, Type, List
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.core.database import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    def __init__(self, session: Session, model: Type[ModelType]):
        self.session = session
        self.model = model

    def get(self, id: int) -> ModelType | None:
        return self.session.get(self.model, id)

    def get_all(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        stmt = select(self.model).offset(skip).limit(limit)
        return list(self.session.execute(stmt).scalars().all())

    def create(self, **kwargs) -> ModelType:
        instance = self.model(**kwargs)
        self.session.add(instance)
        self.session.commit()
        return instance

    def update(self, id: int, **kwargs) -> ModelType | None:
        instance = self.get(id)
        if instance:
            for key, value in kwargs.items():
                setattr(instance, key, value)
            self.session.commit()
        return instance

    def delete(self, id: int) -> bool:
        instance = self.get(id)
        if instance:
            self.session.delete(instance)
            self.session.commit()
            return True
        return False
```

---

### 📄 `src/notifications/manager.py`

```python
from WinToastCreator.creator import toast


def send_notification(title: str | None, message: str | None):
    toast(
        title, 
        message, 
        duration="short"
        )
    
def progress_notification(title: str | None, message: str | None, progress: float):
        
        status = f'{int(progress * 100)} мин.'

        toast(
        title, 
        message, 
        # button="Открыть папку",
        # on_click=lambda e: print("Клик по кнопке"),
        progress={
            'value': progress,
            'title': 'Прогресс',
            'status': status
        },
        duration="short"
        )
```

---

### 📄 `src/patterns/repository.py`

```python
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models import Pattern, ApplicationPattern

class PatternRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_patterns_for_application(self, app_id: int) -> list[Pattern]:
        stmt = select(Pattern).join(ApplicationPattern).where(
            ApplicationPattern.application_id == app_id,
            ApplicationPattern.enabled == True
        )
        return list(self.session.execute(stmt).scalars().all())
```

---

### 📄 `src/patterns/services.py`

```python

```

---

### 📄 `src/session_rules/service.py`

```python
from datetime import datetime
from sqlalchemy.orm import Session
from src.patterns.repository import PatternRepository
from src.notifications.manager import send_notification, progress_notification
from src.session_rules.session_state import ActiveSession, PatternState
import psutil

class SessionRulesService:
    def __init__(self, session: Session):
        self.session = session
        self.pattern_repo = PatternRepository(session)
        self._active_sessions: dict[int, ActiveSession] = {}  # session_id -> ActiveSession

    def start_session(self, session_id: int, app_id: int, process_name: str, start_time: datetime):
        patterns = self.pattern_repo.get_patterns_for_application(app_id)
        if not patterns:
            return  # нет правил – не отслеживаем

        pattern_states = {}
        for pattern in patterns:
            pattern_states[pattern.id] = PatternState(
                pattern=pattern,
                last_notification_time=start_time
            )

        active = ActiveSession(
            session_id=session_id,
            app_id=app_id,
            process_name=process_name,
            start_time=start_time,
            pattern_states=pattern_states
        )
        self._active_sessions[session_id] = active

    def update_session(self, session_id: int, current_time: datetime):
        active = self._active_sessions.get(session_id)
        if not active:
            return

        elapsed_min = (current_time - active.start_time).total_seconds() / 60.0

        for state in active.pattern_states.values():
            pattern = state.pattern
            # 1. Проверка превышения лимита
            if elapsed_min >= pattern.time_limit:
                if not state.limit_exceeded:
                    # Первое превышение
                    self._notify_limit_exceeded(pattern, elapsed_min)
                    state.limit_exceeded = True
                    if pattern.close:
                        self._close_process(active.process_name)
                elif pattern.repeat:
                    # Повторные уведомления после превышения
                    last = state.last_notification_time
                    if (current_time - last).total_seconds() / 60.0 >= pattern.notification_interval:
                        self._notify_limit_exceeded(pattern, elapsed_min, repeat=True)
                        state.last_notification_time = current_time
                # Если repeat=False, больше ничего не делаем
                continue  # переходим к следующему паттерну (лимит уже превышен)

            # 2. Лимит не превышен – проверяем интервал напоминаний
            last = state.last_notification_time
            if (current_time - last).total_seconds() / 60.0 >= pattern.notification_interval:
                progress = elapsed_min / pattern.time_limit if pattern.time_limit > 0 else 0
                self._send_progress_notification(pattern, elapsed_min, progress)
                state.last_notification_time = current_time

    def end_session(self, session_id: int):
        self._active_sessions.pop(session_id, None)

    # ---- Приватные вспомогательные методы ----
    def _send_progress_notification(self, pattern, elapsed_min: float, progress: float):
        # Можно форматировать сообщение, добавляя elapsed_min, но для простоты используем как есть
        progress_notification(pattern.title, pattern.message, progress)

    def _notify_limit_exceeded(self, pattern, elapsed_min: float, repeat: bool = False):
        if repeat:
            msg = f"Лимит {pattern.time_limit} мин. превышен! Вы работаете {int(elapsed_min)} мин."
        else:
            msg = f"Лимит времени ({pattern.time_limit} мин.) превышен!"
            if pattern.close:
                msg += " Приложение будет закрыто."
        send_notification(pattern.title, msg)

    def _close_process(self, process_name: str):
        for proc in psutil.process_iter(['name', 'pid']):
            if proc.info['name'] == process_name:
                try:
                    proc.terminate()
                except Exception as e:
                    print(f"Не удалось закрыть {process_name}: {e}")
                break
```

---

### 📄 `src/session_rules/session_state.py`

```python
from dataclasses import dataclass, field
from datetime import datetime
from src.models import Pattern

@dataclass
class PatternState:
    pattern: Pattern
    last_notification_time: datetime
    limit_exceeded: bool = False

@dataclass
class ActiveSession:
    session_id: int
    app_id: int
    process_name: str
    start_time: datetime
    pattern_states: dict[int, PatternState] = field(default_factory=dict)
```

---

### 📄 `src/tracking/manager.py`

```python
import psutil

from datetime import datetime
from src.applications.services import ApplicationService
from src.core.database import SessionLocal
from src.notifications.manager import send_notification
from src.tracking.tracker import ProcessTracker
from src.session_rules.service import SessionRulesService

class TrackerManager:
    def __init__(self) -> None:
        self.tracked_applications: list[ProcessTracker] = []

    def add_application(self, app: ProcessTracker):
        self.tracked_applications.append(app)
    
    @staticmethod
    def check_process_exist(pid: int | None) -> bool:
        if not pid is None:
            return psutil.pid_exists(pid)
        else: return False

    @staticmethod
    def get_name_by_pid(pid: int) -> str | None:
        try:
            process = psutil.Process(pid)
            return process.name()
        except psutil.NoSuchProcess:
            return None
        except psutil.AccessDenied:
            return None

    @staticmethod
    def get_time() -> str:
        now = datetime.now()
        return now.strftime("%H:%M:%S")
    
    @staticmethod
    def watch_process(app_name: str) -> int | None:
        for p in psutil.process_iter(['name', 'pid']):
            if p.info['name'] == app_name:
                return p.info['pid']
        return None

    def update(self):


        session = SessionLocal()
        try:
            app_service = ApplicationService(session)
            rules_service = SessionRulesService(session)

            for app in self.tracked_applications:
                pid = self.watch_process(app.process_name)
                if pid is not None:
                    if not app.start_notificated:
                        app.start_triger()
                        send_notification(title=app.name, message=f"Приложение запущено в {self.get_time()}")
                        cur_session = app_service.start_session(app.process_name)
                        app.current_session_id = cur_session.id
                        rules_service.start_session(
                            session_id=cur_session.id,
                            app_id=app.application_id,
                            process_name=app.process_name,
                            start_time=datetime.now()
                        )
                    else:
                        if app.current_session_id != -1:
                            rules_service.update_session(app.current_session_id, datetime.now())
                else:
                    if app.start_notificated:
                        app.end_triger()
                        send_notification(title=app.name, message=f"Приложение закрыто в {self.get_time()}")
                        if app.current_session_id != -1:
                            app_service.end_session(app_session_id=app.current_session_id)
                            rules_service.end_session(app.current_session_id)
                        app.current_session_id = -1
        finally:
            session.close()
```

---

### 📄 `src/tracking/tracker.py`

```python
import psutil

class ProcessTracker:
    def __init__(self, process_name: str, application_id: int):
        self.process_name = process_name
        self.application_id = application_id
        self.start_notificated = False
        self.end_notificated = False
        self.current_session_id = -1
    
    @property
    def pid(self) -> int | None:
        for p in psutil.process_iter(['name', 'pid']):
            if p.info['name'] == self.process_name:
                return p.info['pid']
        return None
    
    @property
    def name(self):
        return self.process_name.replace(".exe", "")

    def check_process_exist(self) -> bool:
        if not self.pid is None:
            return psutil.pid_exists(self.pid)
        else: return False

    def start_triger(self):
        self.start_notificated = True

    def end_triger(self):
        self.end_notificated = True

    # def get_name_by_pid(pid: int) -> str | None:
    #     try:
    #         process = psutil.Process(pid)
    #         return process.name()
    #     except psutil.NoSuchProcess:
    #         return None
    #     except psutil.AccessDenied:
    #         return None
```

---

### 📄 `src/utils/iconextract.py`

```python
import icoextract
from pathlib import Path
# import sys

def save_icon(filepath: Path, output_path: Path) -> bool:
    try:
        name = filepath.stem
        icon_output_path = Path(output_path) / f"{name}.ico"
        extractor = icoextract.IconExtractor(filepath)
        extractor.export_icon(icon_output_path)
        return True
    except Exception as e:
        print(e)
        return False

# if __name__ == "__main__":
#     exe_path = sys.argv[1]
#     out_path = sys.argv[2]

#     save_icon(exe_path, out_path)
```
