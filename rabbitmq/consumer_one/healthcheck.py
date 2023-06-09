import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq',heartbeat=1000))
    channel = connection.channel()

    channel.queue_declare(queue='one')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        print("RabbitMQ up and running!!!")

    channel.basic_consume(queue='', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for healthcheck requests. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)