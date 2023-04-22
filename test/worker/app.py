from flask import Flask
app = Flask(__name__)
import pika, os
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
if(connection.is_open):
    print("RabbitMQ conenction established")
else:
    print("RabbitMQ connection failed")
channel = connection.channel()


channel.queue_declare(queue = 'one')

bodys = "Consumer 1"
channel.basic_publish(exchange='', routing_key='one', body = bodys)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'


if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0')