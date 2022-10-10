import threading
import time

from flask import Flask, request, jsonify
import queue
import requests

app = Flask(__name__)

NR_OF_THREADS_TO_SEND = 2

# How big is queue
producer_queue = queue.Queue(5)
consumer_queue = queue.Queue(5)

def send_foods_to_server3():
    while True:
        time.sleep(3)

        if not(producer_queue.empty()):
            food = producer_queue.get()
            requests.post("http://127.0.0.1:5003/consumer", json=food)
            print(f"Item {food['id']} has been sent to server3")

def send_foods_to_server1():
    while True:
        time.sleep(3)

        if not (consumer_queue.empty()):
            food = consumer_queue.get()
            requests.post("http://127.0.0.1:5001/foods", json=food)
            print(f"Item {food['id']} has been sent to server1")

# Here takes food from dinning hall and
# puts in a queue

@app.route('/recieve_from_server1', methods=['POST'])
def recieve_order_from_server_1():
    order = request.json
    producer_queue.put(order)
    print(f"Recieved order {order['id']} from server1")
    return jsonify(order)

@app.route('/recieve_from_server3', methods=['POST'])
def recieve_order_from_server_3():
    order = request.json
    consumer_queue.put(order)
    print(f"Recieved order {order['id']} from server3.")
    return jsonify(order)

# Create a list of threads and each of them runs a function
producers = [threading.Thread(target=send_foods_to_server3, daemon=True) for i in range(NR_OF_THREADS_TO_SEND)]
extractors = [threading.Thread(target=send_foods_to_server1, daemon=True) for i in range(NR_OF_THREADS_TO_SEND)]

if __name__ == '__main__':
    for thread in producers:
        thread.start()
    for thread in extractors:
        thread.start()
    app.run(debug=True,port=5002)