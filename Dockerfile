FROM python:3.11-alpine3.17

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /requirements.txt

WORKDIR /app

RUN pip install -r /requirements.txt &&\
    sudo apt install ffmpeg

COPY . /app

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]



