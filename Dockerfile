FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app
RUN pip install -r /app/requirements.txt
EXPOSE 8000
LABEL Name="learnpath"
LABEL Version="0.1"
CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]

