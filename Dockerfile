FROM python:3.10

WORKDIR /config
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade  -r requirements.txt

# default location of pretrained weights from torchvision
RUN mkdir -p /.cache
RUN chmod 777 /.cache

RUN useradd -m -u 1000 user

USER user 

ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH 

WORKDIR $HOME/app

COPY --chown=user app .
COPY --chown=user models models

EXPOSE 5000

CMD ["python", "run.py"]