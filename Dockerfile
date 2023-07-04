FROM python:3.7
ENV PYTHONUNBUFFERED=1
WORKDIR /workspace
COPY ./workspace/. /workspace/
RUN pip install -r requirements.txt