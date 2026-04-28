/// <reference types="vite/client" />

interface Window {
  pywebview: {
    api: {
      open_file_dialog: () => Promise<string[] | null>
      add_new_application: (path: string) => Promise<void>
      get_all_applications: () => Promise<
        Array<{
          id: number
          title: string
          icon: string
          value: number
          process_name?: string
        }>
      >
      set_notifications: (enabled: boolean) => void
      set_start_end_notifications: (enabled: boolean) => void
      get_all_time_stats: () => Promise<Array<{ name: string; total_time: number }>>
    }
  }
}
