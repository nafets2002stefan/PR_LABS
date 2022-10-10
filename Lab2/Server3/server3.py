#Server 3

import threading
from flask import Flask
import queue

from Lab2 import utils

NR_OF_THREADS_TO_SEND = 2
URL_FOR_SERVER2 = "http://127.0.0.1:5002/recieve_from_server3"
consumer_queue = queue.Queue(5)

def send_foods_to_server2():
    utils.send_foods_to_server(2, consumer_queue, URL_FOR_SERVER2)

extractors = [threading.Thread(target=send_foods_to_server2, daemon=True) for i in range(NR_OF_THREADS_TO_SEND)]


app = Flask(__name__)

@app.route('/consumer', methods=['POST'])
def recieve_order():
    return utils.recieve_order_from_server(2, consumer_queue)

if __name__ == '__main__':
    for thread in extractors:
        thread.start()
    app.run(debug=True, port = 5003)
