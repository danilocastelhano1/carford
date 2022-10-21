# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR ./
COPY requiriments.txt .
RUN pip install -r requiriments.txt
COPY . ./