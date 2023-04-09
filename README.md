# CC Project 2

## Installing dependencies

##### RabbitMQ docker image download
```console
docker pull rabbitmq:3-management
```
##### python dependencies
```console
pip install pika
pip install flask
pip install os
pip install logging 
pip install time
pip install python-dotenv
pip install mysql
```

## Running the application

**Step 1**:

We’ll map port 15672 for the management web app and port 5672 for the message broker.

```console
docker run --rm -it -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```

Assuming that ran successfully, you’ve got an instance of RabbitMQ running! Bounce over to http://localhost:15672 to check out the management web app.

**Step 2**

Open a terminal and split into 4 panes( <kbd>alt</kbd> + <kbd>shift</kbd> + <kbd>+</kbd> for vertical splitting and <kbd>alt</kbd> + <kbd>shift</kbd> + <kbd>-</kbd> for horizontal splitting). 
Run a consumer in each pane.

```console
python healthcheck.py
python insertion.py
python deletion.py
python read.py
```

Now run the producer file in a different terminal window.

```console
python producer.py
```
Once everything is up and running, open http://127.0.0.1:5000, navigate to the routes and enter necessary details and check the terminals where the consumers are running to see the output.





