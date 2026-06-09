# Infrastructure Health Monitoring API

A beginner-friendly infrastructure monitoring API project built using Flask.

This project is being developed slowly as part of my learning journey in:
- REST APIs
- Backend Development
- DevOps
- Observability
- SRE concepts

## Project Status

🚧 Work in Progress

This project is intentionally being built step-by-step to understand the underlying concepts rather than rapidly assembling features.

## Current Features

### API Endpoints

| Method | Endpoint         | Description                 |
| ------ | ---------------- | --------------------------- |
| GET    | /                | API Welcome Message         |
| GET    | /health          | Health Check Endpoint       |
| GET    | /servers         | Retrieve Registered Servers |
| POST   | /register-server | Register a New Server       |

### Validation & Error Handling

* Request validation
* Duplicate server detection
* Custom 404 error handling
* Structured JSON responses

### Database

* SQLite database
* SQLAlchemy ORM
* Persistent server inventory

## Sample Server Registration

```json
{
    "server_name": "web-01",
    "ip_address": "10.0.0.5"
}
```

## Tech Stack

* Python
* Flask
* Flask-SQLAlchemy
* SQLite

## Project Roadmap

### Phase 1 – API Foundation ✅

* Flask Setup
* SQLite Integration
* SQLAlchemy Models
* Server Registration API
* Validation & Error Handling

### Phase 2 – System Metrics (Next)

* CPU Usage Monitoring
* Memory Usage Monitoring
* Disk Usage Monitoring
* System Uptime

### Phase 3 – Alerting

* CPU Threshold Alerts
* Memory Threshold Alerts
* Disk Usage Alerts

### Phase 4 – Containerization

* Docker
* Docker Compose

### Phase 5 – Observability

* Prometheus Integration
* Grafana Dashboards

## Learning Objectives

This project is helping me learn:

* REST API Development
* Database Design
* Infrastructure Monitoring
* Observability Concepts
* DevOps Practices
* Site Reliability Engineering (SRE)

## Author

Harsh Shrimali
