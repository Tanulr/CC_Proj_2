FROM python:3.7-alpine

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD [ "python", "app.py"]