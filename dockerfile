FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y tesseract-ocr tesseract-ocr-tur

COPY . .

CMD ["python", "app.py"]
