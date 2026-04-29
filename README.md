# AppsTracker

Это мой проект для отслеживания времени, которое я провожу за приложениями на Windows. Также есть возможность просматривать статистику активности приложений. Планируется множество гибких настроек, возможность устанавливать лимиты на использование приложений.

## Превью



### Стек

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F1C?style=flat&logo=sqlalchemy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![pywebview](https://img.shields.io/badge/pywebview-000000?style=flat&logo=webview&logoColor=white)
![Vue 3](https://img.shields.io/badge/Vue_3-4FC08D?style=flat&logo=vue.js&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat&logo=tailwindcss&logoColor=white)

### Фичи

- Ловит запуск и закрытие программ
- Считает сессии и показывает статистику
- Шлёт системные уведомления Windows
- Позволяет задавать паттерны поведения (в разработке)

### Запуск

```bash
uv sync
uv run python -m src.desktop
```

```bash
cd frontend
npm install
npm run dev
```
