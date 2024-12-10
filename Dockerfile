FROM python:3.12

ADD pyproject.toml /app/
WORKDIR /app/

RUN mkdir src && pip install -e .

ADD . /app/
