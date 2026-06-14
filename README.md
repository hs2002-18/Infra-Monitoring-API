# Infrastructure Monitoring API

A lightweight Infrastructure Monitoring API built using Flask, Docker, Prometheus, and Grafana.

This project was created to learn and understand core observability and monitoring concepts commonly used in SRE, DevOps, and Cloud Engineering roles.

## Features

* Health Check Endpoint
* System Metrics Collection

  * CPU Usage
  * Memory Usage
  * Disk Usage
  * System Uptime
* Alert Generation
* Docker Containerization
* Docker Compose Orchestration
* Prometheus Metrics Export
* Prometheus Monitoring Integration
* Grafana Deployment Support

## Project Structure

```text
api-infra-monitor/
│
├── routes/
│   ├── health.py
│   ├── metrics.py
│   └── alert_routes.py
│
├── services/
│   ├── metrics.py
│   └── alerts.py
│
├── prometheus/
│   └── prometheus.yml
│
├── instance/
│   └── monitor.db
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .gitignore
└── app.py
```

## API Endpoints

### Health Check

```http
GET /health
```

Example Response:

```json
{
  "status": "healthy"
}
```

### System Metrics

```http
GET /metrics
```

Example Response:

```json
{
  "cpu_percent": 5.6,
  "memory_percent": 30.3,
  "disk_percent": 75.6,
  "uptime_seconds": "0 days, 1 hours, 56 minutes"
}
```

### Alerts

```http
GET /alerts
```

Example Response:

```json
[
  {
    "severity": "warning",
    "message": "Disk usage is high"
  }
]
```

### Prometheus Metrics

```http
GET /prometheus
```

Used by Prometheus to scrape application metrics.

## Monitoring Dashboard
<img width="949" height="634" alt="image" src="https://github.com/user-attachments/assets/5ba51f38-7077-4b81-b041-4691c84ea6ca" />


## Technologies Used

* Python
* Flask
* SQLite
* Docker
* Docker Compose
* Prometheus
* Grafana
* psutil

## Running the Project

### Clone Repository

```bash
git clone <repository-url>
cd api-infra-monitor
```

### Start Services

```bash
docker compose up -d
```

### Verify Containers

```bash
docker compose ps
```

### Access Services

API:

```text
http://localhost:5000
```

Prometheus:

```text
http://localhost:9090
```

Grafana:

```text
http://localhost:3000
```

## Learning Goals

This project was built to gain hands-on experience with:

* REST API Development
* Infrastructure Monitoring
* Observability Concepts
* Docker Containerization
* Metrics Collection
* Prometheus Monitoring
* Grafana Visualization
* SRE and DevOps Practices

## Future Enhancements

* Multi-server Monitoring
* Server Registration API
* Slack/Email Alerting
* CI/CD Pipeline
* Kubernetes Deployment
* Terraform Integration
* Cloud Deployment (AWS/GCP)

## Project Status

Version: **v1.0**

Core monitoring functionality is complete and operational. Future updates will focus on advanced monitoring, automation, and cloud-native deployment patterns.

---

Built as a learning project for SRE, DevOps, and Cloud Engineering.
