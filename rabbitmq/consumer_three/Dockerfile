FROM python:3.7-alpine

RUN mkdir /consumer_three
WORKDIR /consumer_three
ADD requirements.txt /consumer_three//
ADD deletion.py /consumer_three//
RUN pip install -r requirements.txt
CMD ["python", "deletion.py"]