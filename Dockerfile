# ================================== BUILDER ===================================
ARG INSTALL_PYTHON_VERSION='3.11.0'

FROM python:${INSTALL_PYTHON_VERSION}-slim-buster AS builder

WORKDIR /

COPY ./app /app/
COPY ./wsgi.py /
COPY ./tests /tests

COPY ./Pipfile* ./
RUN pip install pipenv
RUN pipenv install --system --deploy

RUN pytest tests/test*.py

# EXPOSE 5000
CMD ["gunicorn", "wsgi:app", "--worker-class", "gthread", "--workers", "4", "--bind", "0.0.0.0:8080"]
