FROM python:3.12

RUN pip install poetry==1.8.5

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

COPY src/dtw_lab ./src/dtw_lab

RUN poetry install 

ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT ["poetry", "run", "start-server"]