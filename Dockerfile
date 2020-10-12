FROM python:3.7

RUN mkdir /app
WORKDIR /app

COPY . .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENTRYPOINT ["python", "main.py"]