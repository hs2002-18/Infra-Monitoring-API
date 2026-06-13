import psutil
import time

from utils.helpers import format_uptime
from services.prometheus import (
    cpu_gauge,
    memory_gauge,
    disk_gauge
)

def get_system_metrics():
    boot_time = psutil.boot_time()
    uptime_seconds = int(time.time() - boot_time)

    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage("/").percent

    cpu_gauge.set(cpu_percent)
    memory_gauge.set(memory_percent)
    disk_gauge.set(disk_percent)

    metrics={
        "cpu_percent": cpu_percent,
        "memory_percent": memory_percent,
        "disk_percent": disk_percent,
        "uptime_seconds": format_uptime(uptime_seconds)
    }

    return metrics