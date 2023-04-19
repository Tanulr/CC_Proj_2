import pika, sys, os
from pymongo import MongoClient

# host = MongoClient("172.17.0.2")
host = MongoClient("mongodb_micro")

db = host["studentdb"]
collection = db["student"]

def addDetails(SRN, Name):
    data = {"Name:":Name,"SRN":SRN}
    collection.insert_one(data)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.environ['RabbitMQ_host'],heartbeat=1000))
    channel = connection.channel()

    channel.queue_declare(queue='two')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        SRN = body.split(" ")[0]
        Name = body.split(" ")[1]
        addDetails(SRN, Name)
        print(" [x] Inserted into database %r" % body)

        # Have to write code for insertion into database here

    channel.basic_consume(queue='', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for insertion requests. To exit press CTRL+C')
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