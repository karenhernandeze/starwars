FROM python:3.11.2-alpine

WORKDIR /app

ENV PORT=3000

COPY src src/
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 3000


CMD ["python", "-m", "src.app"]