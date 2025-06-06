FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 1234

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "1234"]
