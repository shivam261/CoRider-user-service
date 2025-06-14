# Stage 1: Build
FROM python:3.12-slim AS build

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev

COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# Stage 2: Clean final image
FROM python:3.12-slim

WORKDIR /app

COPY --from=build /install /usr/local
COPY . .

EXPOSE 5000

CMD ["python", "run.py"]
