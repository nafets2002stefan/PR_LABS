import threading
import time

from flask import Flask, request, jsonify
import queue
import requests


app = Flask(__name__)

NR_OF_THREADS_TO_SEND = 2

consumer_queue = queue.Queue(5)

def send_foods_back_to_server2():
    while True:
        time.sleep(3)

        if not(consumer_queue.empty()):
            food = consumer_queue.get()
            requests.post("http://127.0.0.1:5002/recieve_from_server3", json=food)
            print(f"Item {food['id']} has been sent to server2")


@app.route('/consumer', methods=['POST'])
def recieve_order():
    order = request.json
    consumer_queue.put(order)
    print(f"Recieved order {order['id']} from server2")
    return jsonify(order)

extractors = [threading.Thread(target=send_foods_back_to_server2, daemon=True) for i in range(NR_OF_THREADS_TO_SEND)]

if __name__ == '__main__':
    for thread in extractors:
        thread.start()
    app.run(debug=True, port = 5003)
