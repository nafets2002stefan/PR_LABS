import time
from flask import Flask, request, jsonify
import requests


def send_foods_to_server(number_of_server, queue, url_to_send):
    while True:
        time.sleep(3)

        if not(queue.empty()):
            food = queue.get()
            requests.post(url_to_send, json=food)
            print(f"Item {food['id']} has been sent to server {number_of_server}")

def recieve_order_from_server(nr_of_server, queue):
    order = request.json
    queue.put(order)
    print(f"Recieved order {order['id']} from server {nr_of_server}")
    return jsonify(order)