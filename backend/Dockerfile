FROM python:3.12

WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000"]
