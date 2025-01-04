FROM python:3.11.11-alpine3.20 AS builder

ARG POETRY_VERSION=1.8.5
ENV POETRY_HOME=/opt/poetry
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_IN_PROJECT=1
ENV POETRY_VIRTUALENVS_CREATE=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_CACHE_DIR=/opt/.cache

RUN pip install "poetry==${POETRY_VERSION}"

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry install --only main --no-root && rm -rf $POETRY_CACHE_DIR

COPY ppgee /app/ppgee

RUN poetry install --without dev

FROM python:3.11.11-alpine3.20 AS runtime

ENV PATH="/app/.venv/bin:$PATH"

COPY --from=builder /app /app

ENTRYPOINT [ "ppgee" ]
