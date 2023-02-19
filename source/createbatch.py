"""Имитирует API, которая возвращает список лиц с персональными данными"""

from person import get_person
import os
import random
import json


API_DIR = "api"
API_FILENAME = "api.json"
API_PATH = os.path.join(API_DIR, API_FILENAME)

if not os.path.exists(API_DIR): 
    os.makedirs(API_DIR)

n = random.randint(1, 10)    # Кол-во заявителей
n = 1
to_dump = {"persons": [ get_person() for _ in range(n)]}

with open(API_PATH, "w") as file:
    json.dump(to_dump, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":

    with open(API_PATH, "w") as file:
        json.dump(to_dump, file, indent=4, ensure_ascii=False)

