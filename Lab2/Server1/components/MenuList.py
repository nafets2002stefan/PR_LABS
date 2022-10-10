import json
import random


class MenuList:
    def __init__(self):
        self.foods = []

        with open('components/menu.json') as file:
            data = json.load(file)

        self.foods = data

    def generate_random_food(self):
        random_item = random.randint(0,len(self.foods) - 1)
        return self.foods[random_item]

