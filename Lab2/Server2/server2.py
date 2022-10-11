#Server 2

import threading
from flask import Flask
import queue

from Lab2 import utils


NR_OF_THREADS_TO_SEND = 2

producer_queue = queue.Queue(5)
consumer_queue = queue.Queue(5)

URL_FOR_SERVER3 = "http://127.0.0.1:5003/consumer"
URL_FOR_SERVER1 = "http://127.0.0.1:5001/foods"

def send_foods_to_server1():
    utils.send_foods_to_server(1, consumer_queue, URL_FOR_SERVER1)

def send_foods_to_server3():
    utils.send_foods_to_server(3, producer_queue, URL_FOR_SERVER3)

app = Flask(__name__)

@app.route('/recieve_from_server3', methods=['POST'])
def recieve_order_from_server_3():
    return utils.recieve_order_from_server(3, consumer_queue)

@app.route('/recieve_from_server1', methods=['POST'])
def recieve_order_from_server_1():
    return utils.recieve_order_from_server(1, producer_queue)

# Create a list of threads and each of them runs a function
producers = [threading.Thread(target=send_foods_to_server3, daemon=True) for i in range(NR_OF_THREADS_TO_SEND)]
extractors = [threading.Thread(target=send_foods_to_server1, daemon=True) for i in range(NR_OF_THREADS_TO_SEND)]

if __name__ == '__main__':
    for thread in producers:
        thread.start()
    for thread in extractors:
        thread.start()
    app.run(debug=True,port=5002)
