import threading
import time

from flask import Flask, request, jsonify
import queue
import requests

app = Flask(__name__)

NR_OF_THREADS_TO_SEND_BACK = 2

# How big is queue
queue = queue.Queue(5)
mutex = threading.Lock()

def send_foods_to_dinning_hall():
    while True:

        mutex.acquire()
        time.sleep(3)

        if not(queue.empty()):
            food = queue.get()
            requests.post("http://127.0.0.1:5001/foods", json=food)
            print(f"Item {food['id']} has been sent back to Dinning Hall")
        mutex.release()
# Here takes food from dinning hall and
# puts in a queue

@app.route('/order', methods=['POST'])
def recieve_order():
    order = request.json
    queue.put(order)
    print(f"Recieved order {order['id']} from Dinning Hall.")
    return jsonify(order)

# Create a list of threads and each of them runs a function
extactors = [threading.Thread(target=send_foods_to_dinning_hall, daemon=True) for i in range(NR_OF_THREADS_TO_SEND_BACK)]

if __name__ == '__main__':
    for thread in extactors:
        thread.start()
    app.run(debug=True)