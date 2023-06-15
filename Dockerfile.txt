FROM python:3.9

WORKDIR /resultados

COPY . /resultados

EXPOSE 8000

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]

