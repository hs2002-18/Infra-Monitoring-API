from services.metrics import get_system_metrics

def get_alerts():

    metrics = get_system_metrics()

    alerts = []

    if metrics["cpu_percent"] > 80:
        alerts.append({
            "severity": "warning",
            "message": "CPU usage is high"
            })
    if metrics["memory_percent"] > 75:
        alerts.append({
            "severity": "warning",
            "message": "Memory usage is high"
        })
    if metrics["disk_percent"] > 70:
        alerts.append({
            "severity": "warning",
            "message": "Disk usage is high"
        })
    
    if not alerts:
        return{
            "messages": "No alerts found"
        }

    return alerts