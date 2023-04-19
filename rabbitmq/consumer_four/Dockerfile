FROM python:3.7-alpine

RUN mkdir /consumer_four
WORKDIR /consumer_four
ADD requirements.txt /consumer_four/
ADD read.py /consumer_four/
RUN pip install -r requirements.txt
CMD ["python", "read.py"]