FROM python:3.9-slim

COPY app.py /app/

CMD ["python", "-u", "/app/app.py"]
