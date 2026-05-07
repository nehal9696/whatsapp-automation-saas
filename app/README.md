# WhatsApp Automation SaaS Platform

A multi-tenant backend system built using FastAPI for automating customer communication workflows through WhatsApp-style messaging APIs.

## Features

- JWT-based authentication
- Multi-tenant architecture
- Protected APIs
- Business ownership enforcement
- Message lifecycle tracking
- Async message processing
- Webhook-driven status updates
- PostgreSQL integration
- Rate limiting
- Structured logging

---

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- SlowAPI
- Python

---

## Project Structure

```bash
app/
 ├── api/
 ├── core/
 ├── db/
 ├── models/
 ├── services/
 └── main.py
```

---

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/your-username/whatsapp-automation-saas.git
cd whatsapp-automation-saas
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows
```bash
venv\Scripts\activate
```

#### Linux/Mac
```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Database Setup

Create PostgreSQL database:

```sql
CREATE DATABASE whatsapp_saas;
```

Update `DATABASE_URL` in your project.

---

## Run Application

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Implemented Backend Concepts

- OAuth2 + JWT Authentication
- Dependency Injection
- Multi-Tenant SaaS Architecture
- Event-Driven Webhooks
- Async Processing
- Rate Limiting
- Structured Logging
- Database Relationships

---

## Future Improvements

- Redis Queue Integration
- Celery Workers
- Docker Support
- CI/CD Pipeline
- AWS Deployment