# Dockerfile for Seyitan's Flask Blog
FROM python:3.14-alpine
LABEL maintainer="Seyitan Oluwaseitan"

# Install build dependencies for Python packages
RUN apk add --no-cache gcc musl-dev libffi-dev

COPY . /app
WORKDIR /app

RUN python -m pip install --upgrade pip \
    && python -m pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "src/app.py"]
