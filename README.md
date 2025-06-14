# 🐍 Flask MongoDB User Management API

A simple user management REST API built with Flask and MongoDB, dockerized for easy deployment.

## 🚀 Features

- RESTful CRUD API for user management
- MongoDB integration
- Rate limiting with Flask-Limiter
- Caching with Flask-Caching
- Dockerized (multi-container using `docker-compose`)
- Auto-restart & persistent data volume for MongoDB
```
## 🧱 Project Structure

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
```
## 📦 Setting up Env files
make env files according to project structure
- development.env
  ```
  FLASK_ENV=development
  MONGO_URI=mongodb://localhost:27017/corider
  SECRET_KEY=supersecretkey
  HOST=127.0.0.1
  ```
- production.env
  ```
  FLASK_ENV=PRODUCTION
  SECRET_KEY=supersecretkey
  MONGO_URI=mongodb://mongo:27017/corider
  HOST=0.0.0.0

  ```
## 📦 Requirements

- Docker
- Docker Compose
- Git

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/shivam261/CoRider-user-service.git

```
make sure you are in same Repo as app

### 2 . installing dependencies
setting up venv
```
python3 -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```
installing dependencies 
```
pip install -r requirements.txt
```
## using docker 
using docker compose 
```
docker-compose up --build

```
accessing the app
```
http://localhost:5050
```
## using local setup 
### change MONGO_URI in development.env
```
FLASK_ENV=development
MONGO_URI=<your mongoDb uri>/Corider
SECRET_KEY=supersecretkey
HOST=127.0.0.1
```
### run command 
```
python run.py
```
### accessing the app
```
http://localhost:5000
```

