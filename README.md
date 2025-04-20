# Database Monitoring Project

A Kubernetes-based database application for climate data collection and monitoring, featuring advanced observability using OpenTelemetry and SigNoz.

## Project Overview

This project implements a complete database platform for climate data with the following features:

- MySQL database storing climate information (temperature, precipitation)
- Kubernetes-based deployment using Ansible playbooks
- Comprehensive monitoring with SigNoz and OpenTelemetry
- Custom SQL metric collection via OpenTelemetry Collector
- Automated CI/CD pipeline for database operations

## Components

### Database

- MySQL database with Climate Data schema
- Automated schema migrations
- Data seeding for testing and development
- Validation scripts for data integrity

### Monitoring

- MySQL Exporter for standard database metrics
- OpenTelemetry Collector for custom SQL metrics
- SigNoz dashboards for visualization and alerting
- Custom SQL query monitoring for average temperature by location

### Infrastructure

- Kubernetes deployment with Helm charts
- Ansible playbooks for environment setup and teardown
- CI/CD workflow for automated testing and deployment

## Getting Started

1. Set up environment:
   ```
   ansible-playbook up.yml
   ```

2. Access SigNoz dashboard to view metrics
   - Standard MySQL metrics via Prometheus
   - Custom temperature metrics via SQL query

3. Tear down environment when done:
   ```
   ansible-playbook down.yml
   ```

## Directory Structure

- `/k8s/` - Kubernetes manifests for MySQL, exporter, and OpenTelemetry Collector
- `/sql/` - SQL scripts for database schema, migrations, and data seeding
- `/scripts/` - Python scripts for database operations and testing
- `/.github/workflows/` - CI/CD pipeline configuration

