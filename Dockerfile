FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
COPY app .
COPY models models

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "run.py"]