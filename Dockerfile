FROM python:3.12-slim

WORKDIR /app

RUN pip install Flask

COPY . .

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]
