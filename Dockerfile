FROM python:3.10

COPY . .

RUN echo tes

RUN pip install -r requirements.txt

ENTTRYPOINT [ "python", "test.py" ]