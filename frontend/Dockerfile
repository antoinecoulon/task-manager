FROM python:3.12-slim@sha256:df3b7c223e6fee2bd45166f5ebd3fd9d2c09d5e5f8b62b36f4c5d72fc63dc8a1

# Metadonnées
LABEL maintainer="Antoine Coulon"
LABEL description="DevSecOps ENI TP - Frontend"
LABEL version=1.0

# Checkov test
RUN useradd -m appuser
USER appuser

WORKDIR /app
COPY . /app/

EXPOSE 5173

# Checkov test
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
    CMD python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:5173/', timeout=5)" || exit 1

CMD ["python3", "-m", "http.server", "5173", "--bind", "0.0.0.0"]
