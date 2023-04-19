FROM python:3.7-alpine

RUN mkdir /consumer_two
WORKDIR /consumer_two
ADD requirements.txt /consumer_two/
ADD insertion.py /consumer_two/
RUN pip install -r requirements.txt
CMD ["python", "insertion.py"]