FROM python:3.12-slim

WORKDIR /app
COPY . /app/

EXPOSE 5173

# Checkov test
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
    CMD python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:5173/', timeout=5)" || exit 1

CMD ["python3", "-m", "http.server", "5173", "--bind", "0.0.0.0"]
