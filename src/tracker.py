import psutil

class ProcessTracker:
    def __init__(self, process_name: str):
        self.process_name: str = process_name
        self.start_notificated: bool = False
        self.end_notificated: bool = False
    
    @property
    def pid(self):
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