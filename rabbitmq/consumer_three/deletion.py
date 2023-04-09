import pika, sys, os
import mysql.connector 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Apravamthe@98",
    database = "animalshelter"
)

c = mydb.cursor()

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='three')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        # Have to write code for deletion from database here

    channel.basic_consume(queue='', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
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