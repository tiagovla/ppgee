FROM python:3.11-slim

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir poetry==1.8.5 && \
    poetry install --no-interaction --no-dev

CMD ["sh", "-c", "poetry run ppgee $USERNAME $PASSWORD"]
