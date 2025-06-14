# 🐍 Flask MongoDB User Management API

A simple user management REST API built with Flask and MongoDB, dockerized for easy deployment.

## 🚀 Features

- RESTful CRUD API for user management
- MongoDB integration
- Rate limiting with Flask-Limiter
- Caching with Flask-Caching
- Dockerized (multi-container using `docker-compose`)
- Auto-restart & persistent data volume for MongoDB

## 🧱 Project Structure

.
├── app/
│   ├── __init__.py
│   ├── controllers/
│   │   └── user_controller.py
│   ├── models/
│   │   └── users.py
│   ├── routes/
│   │   └── user_routes.py
│   ├── services/
│   ├── utils/
│
├── run.py
├── requirements.txt
├── development.env
├── production.env
├── Dockerfile
├── .gitignore
├── .dockerignore
├── docker-compose.yml
├── config.py
└── README.md

## 📦 Requirements

- Docker
- Docker Compose

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/shivam261/CoRider-user-service.git

