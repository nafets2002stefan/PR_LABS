# Dinning Hall

from flask import Flask, request
import time
import threading
import requests

# Importing menus
from components.MenuList import *
NR_OF_THREADS_TO_SEND = 5


app = Flask(__name__)
menu = MenuList()

# Sends item to kitchen server
def send_foods_to_kitchen():
    while True:
        time.sleep(3)
        menu_item = create_random_food()
        if requests.post('http://127.0.0.1:5000/order', json=menu_item):
            print(f'Item {menu_item["id"]} has been sent to kitchen')

# Generates a random food item from menu list
def create_random_food():
    menu_item = menu.generate_random_food()
    return menu_item

# Recieves foods which we were sent to kitchen
@app.route('/foods', methods=['POST'])
def recieve_order_from_kitchen():
    order = request.json
    print(f"Recieved order {order['id']} from Kitchen.")
    return order

# Create a list of threads and each of them runs function
generators = [threading.Thread(target=send_foods_to_kitchen, daemon=True) for i in range(NR_OF_THREADS_TO_SEND)]

# Runs app on port 5001
def run_app():
    app.run(debug=True,port=5001)


if __name__ == '__main__':
    for thread in generators:
        thread.start()
    run_app()
