from prometheus_client import Gauge

cpu_gauge = Gauge(
    "cpu_usage_percent",
    "Current CPU usage percentage"
)

memory_gauge = Gauge(
    "memory_usage_percent",
    "Current memory usage percentage"
)

disk_gauge = Gauge(
    "disk_usage_percent",
    "Current disk usage percentage"
)