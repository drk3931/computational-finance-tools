FROM continuumio/miniconda3

# Grab requirements.txt.
ADD ./requirements.txt /tmp/requirements.txt

ADD ./webapp /opt/webapp/

RUN pip install -r /tmp/requirements.txt 

WORKDIR /opt/webapp

CMD gunicorn --bind 0.0.0.0:$PORT wsgi:app

