FROM python:3.10.14

COPY . .

RUN pip install -r requirements.txt

ENTTRYPOINT [ "python", "app.py" ]