#Server 1

import threading
from flask import Flask
import requests
import queue
import time

from Lab2 import utils
from components.MenuList import *

server1_queue = queue.Queue()
NR_OF_THREADS_TO_SEND = 5
URL_FOR_SERVER2 = "http://127.0.0.1:5002/recieve_from_server1"

menu = MenuList()
def create_random_food():
    menu_item = menu.generate_random_food()
    return menu_item


def send_foods_to_server2():
    while True:
        time.sleep(3)

        menu_item = create_random_food()
        if requests.post('http://127.0.0.1:5002/recieve_from_server1', json=menu_item):
            print(f'Item {menu_item["id"]} has been sent to server 2')

app = Flask(__name__)

@app.route('/foods', methods=['POST'])
def recieve_order_from_server2():
    return utils.recieve_order_from_server(2, server1_queue)

generators = [threading.Thread(target=send_foods_to_server2, daemon=True) for i in range(NR_OF_THREADS_TO_SEND)]

def run_app():
    app.run(debug=True,port=5001)


if __name__ == '__main__':
    for thread in generators:
        thread.start()
    run_app()
