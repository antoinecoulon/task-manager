FROM python:3.12@sha256:df3b7c223e6fee2bd45166f5ebd3fd9d2c09d5e5f8b62b36f4c5d72fc63dc8a1

# Metadonnées
LABEL maintainer="Antoine Coulon"
LABEL description="DevSecOps ENI TP - Backend"
LABEL version=1.0

# Checkov test
RUN useradd -m appuser
USER appuser

WORKDIR /app
COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Checkov test
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
    CMD python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health', timeout=5)" || exit 1

CMD ["python3", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
