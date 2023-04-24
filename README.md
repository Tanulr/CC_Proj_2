# CC Project 2

## Running the application

Open a terminal and navigate to the **rabbitmq** directory.
Run the following command to run the application
```console
docker-compose up
```

The individual microservices might give errors for upto a minute because rabbitMQ takes a while to start-up completely. Once rabbitMQ is up and running you can see that the consumers are waiting for messages from the producer and the producer flask app is live.

To look at individual queues created on the rabbitMQ message broker, open http://127.0.0.1:15672 where the rabbitMQ management app is deployed. Use credentials **guest** for both username and password.

Open http://127.0.0.1:8080 where the flask app is deployed.

## Microservices

1. **Healthcheck**
    Checks whether the connection to RabbitMQ brocker is established.
2. **Insert into database**
    Insert tuples into the database. The two values are SRN and Student Name.
3. **Delete from database**
    Deletes tuples based on the SRN given.
4. **Read database**
    Reads the database and prints the values on the terminal.

