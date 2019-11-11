FROM python:3.6.8

RUN mkdir app/
WORKDIR app/
COPY . .

RUN pip3 install -r requirements.txt

CMD python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000

