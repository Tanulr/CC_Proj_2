FROM python:3.7-alpine

RUN mkdir /consumer_one
WORKDIR /consumer_one
ADD requirements.txt /consumer_one/
ADD healthcheck.py /consumer_one/
RUN pip install -r requirements.txt
CMD ["python", "healthcheck.py"]