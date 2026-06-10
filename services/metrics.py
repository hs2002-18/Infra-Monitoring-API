import psutil
import time

def get_system_metrics():
    boot_time = psutil.boot_time()
    uptime_seconds = int(time.time() - boot_time)

    metrics={
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
        "uptime_seconds": uptime_seconds
    }

    return metrics