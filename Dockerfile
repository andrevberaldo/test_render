FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 4000

CMD [ "opentelemetry-instrument", "uvicorn", "src.api:api", "--host", "0.0.0.0", "--port", "4000" ]