FROM python:3.10

COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN pip install gevent gunicorn
ADD . /flask
WORKDIR /flask

EXPOSE 3000

CMD gunicorn --worker-class gevent --workers 2 --bind 0.0.0.0:3000 wsgi:app