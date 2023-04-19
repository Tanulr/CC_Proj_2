from flask import Flask, render_template, request
import pika, os, logging
logging.basicConfig()
 
# url = os.environ.get('CLOUDAMQP_URL','amqp://guest:guest@localhost/%2f')
# params = pika.URLParameters(url)
# params.socket_timeout = 5

connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.environ['RabbitMQ_host'],heartbeat=1000))
channel = connection.channel()

channel.queue_declare(queue = 'one')
channel.queue_declare(queue = 'two')
channel.queue_declare(queue = 'three')
channel.queue_declare(queue = 'four')


# for x in range(1000):
#     bodys = 'data ke' + str(x+1)
#     channel.basic_publish(exchange='', routing_key='pdfprocess', body = bodys)
#     print("[x] message sent to consumer = "+bodys)
#     a = x%100
#     if a==0:
#         time.sleep(2)
# connection.close()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/one', methods=['GET'])
def healthcheck():
    bodys = "Consumer 1"
    channel.basic_publish(exchange='', routing_key='one', body = bodys)
    print("[x] message sent to consumer = "+bodys)
    return "healthcheck"

@app.route('/two', methods = ['POST', 'GET'])
def insert():
    
    if request.method == "POST":
        SRN = request.form.get("SRN")
        name = request.form.get("Name")
        bodys = SRN + " " + name
        channel.basic_publish(exchange='', routing_key='two', body = bodys)

        return render_template("insert.html")
        #    return "Your name is "+SRN + name
    return render_template("insert.html")
    
    

@app.route('/three', methods = ['POST', 'GET'])
def delete():
    if request.method == "POST":
        SRN = request.form.get("SRN")

        bodys = SRN 
        channel.basic_publish(exchange='', routing_key='three', body = bodys)

        return render_template("delete.html")
        #    return "Your name is "+SRN + name
    return render_template("delete.html")

@app.route('/four', methods = ['POST', 'GET'])
def read():
    if request.method == "POST":
        bodys = "Read database request received"
        channel.basic_publish(exchange='', routing_key='four', body = bodys)

        return render_template("read.html")
        #    return "Your name is "+SRN + name
    return render_template("read.html")

if __name__ =='__main__':
    app.run(debug = True, port=8080)