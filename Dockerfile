
FROM python:3.8-alpine3.15

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=unicorn.py

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
