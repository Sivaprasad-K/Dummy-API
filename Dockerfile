FROM python:3.8.5-slim


COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

WORKDIR src

COPY . .


ENTRYPOINT uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

