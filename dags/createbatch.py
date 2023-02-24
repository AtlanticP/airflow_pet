"""Имитирует API, которая возвращает список лиц с персональными данными"""

from airflow.decorators import task
from airflow import DAG
from airflow.utils.dates import days_ago
from utils import get_person
import random
import json
from constants import API_PATH 
from datetime import timedelta


@task(task_id="create_batch_API")
def create_batch() -> None:
    """Создание батча случайного размера от 1 до 10"""

    n = random.randint(1, 10)    # Кол-во заявителей
    to_dump = {"persons": [ get_person() for _ in range(n)]}

    with open(API_PATH, "w") as file:
        json.dump(to_dump, file, indent=4, ensure_ascii=False)

    if __name__ == "__main__":

        with open(API_PATH, "w") as file:
            json.dump(to_dump, file, indent=4, ensure_ascii=False)

args = {
        "owner": "Nikita Davydov",
        "start_date": days_ago(0),
        "depends_on_past": False
}

with DAG(
    dag_id="create_batch",
    default_args=args,
    schedule_interval=timedelta(seconds=5),
    catchup=False
):
    t1 = create_batch()
    t1

