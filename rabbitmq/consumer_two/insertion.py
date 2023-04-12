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

def addDetails(SRN, Name):
    c.execute('INSERT INTO Student(SRN, Name) VALUES (%s, %s)', (SRN, Name))
    mydb.commit()

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
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