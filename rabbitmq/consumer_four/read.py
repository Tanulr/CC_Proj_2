import pika, sys, os
from dotenv import load_dotenv
import mysql.connector 

load_dotenv()

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = os.getenv("MYSQL_PASSWORD"),
    database = "studentdb"
)

c = mydb.cursor()

def readData():
    c.execute('SELECT * FROM student')
    data = c.fetchall()
    return data

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='four')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        data = readData()
        print(data)


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