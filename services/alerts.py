from services.metrics import get_system_metrics

def get_alerts():

    metrics = get_system_metrics()

    alerts = []

    if not alerts:
        return{
            "messages": "No alerts found"
        }

    if metrics["cpu_usage"] > 80:
        alerts.append({
            "severity": "warning",
            "message": "CPU usage is high"
            })
    if metrics["memory_percent"] > 75:
        alerts.append({
            "severity": "warning",
            "message": "Memory usage is high"
        })
    if metrics["disk_usage"] > 70:
        alerts.append({
            "severity": "warning",
            "message": "Disk usage is high"
        })

    return alerts