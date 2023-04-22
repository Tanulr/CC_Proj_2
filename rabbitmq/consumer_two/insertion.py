import pika, sys, os
import psycopg2


mydb = psycopg2.connect(
    host="postgres",
    user="root",
    database="student_db",
    password="password",
    port = 5432
)

c = mydb.cursor()

def addDetails(SRN, Name):
    try:
        c.execute('INSERT INTO Student(SRN, sname) VALUES (%s, %s)', (SRN, Name))
        mydb.commit()
    except Exception as e:
        print(f"Error inserting into database: {e}")
        mydb.rollback()
    

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq',heartbeat=1000))
    channel = connection.channel()

    channel.queue_declare(queue='two')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        body = body.decode()
        SRN = body.split(" ")[0]
        Name = body.split(" ")[1]
        addDetails(SRN, Name)
        print(" [x] Successfully inserted into database %r" % body)
        # ch.basic_ack(delivery_tag=method.delivery_tag)
        

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