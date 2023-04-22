FROM python:3.7-alpine

RUN mkdir /listener
WORKDIR /listener
ADD requirements.txt /listener/
ADD listener.py /listener/
RUN pip install -r requirements.txt
CMD ["python", "listener.py"]