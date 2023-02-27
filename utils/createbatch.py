"""Имитирует API, которая возвращает список лиц с персональными данными"""

from person import get_person
import random
import json
from constants import API_PATH 


n = random.randint(1, 10)    # Кол-во заявителей
to_dump = {"persons": [ get_person() for _ in range(n)]}

with open(API_PATH, "w") as file:
    json.dump(to_dump, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":

    with open(API_PATH, "w") as file:
        json.dump(to_dump, file, indent=4, ensure_ascii=False)

