FROM python:3.7-alpine

RUN mkdir /producer
WORKDIR /producer
EXPOSE 8080
ADD requirements.txt /producer/
ADD producer.py /producer/
COPY templates /producer/templates
RUN pip install -r requirements.txt
CMD ["python", "producer.py"]