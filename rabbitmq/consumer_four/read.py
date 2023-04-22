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

def readData():
    
    try:
        c.execute('SELECT * FROM student')
        data = c.fetchall()
        return data
    except Exception as e:
        print(f"Error reading from database: {e}")



def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq',heartbeat=1000))
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