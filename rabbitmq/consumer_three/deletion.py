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

def deleteData(SRN):
    try:
        c.execute('DELETE FROM student WHERE SRN="{}"'.format(SRN))
        mydb.commit()
    except Exception as e:
        print(f"Error deleting from database: {e}")
        mydb.rollback()

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq',heartbeat=1000))
    channel = connection.channel()

    channel.queue_declare(queue='three')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        body = body.decode()
        SRN = body.split(" ")[0]
        deleteData(SRN)
        print(" [x] Successfully deleted from database %r" % body)
        # ch.basic_ack(delivery_tag=method.delivery_tag)
        
    
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