from airflow import DAG
from airflow.decorators import task
from airflow.utils.dates import days_ago
from datetime import timedelta
from airflow.providers.postgres.hooks.postgres import PostgresHook

import json
from constants import API_PATH
import psycopg2
import re

@task(task_id="extract_data_applications")
def extract_data() -> dict:
    """Извлечение json-данных о заявителях"""
    
    with open(API_PATH, "r") as json_file:
        data = json.load(json_file)

    return data

@task(task_id="transform_date_applications", multiple_outputs=True)
def transform_data(data: dict) -> dict:
    """Приводит телефонные номера к последовательности из 10 цифр"""

    def clean_phonenumber(text: str) -> str:
        "correct phone number 99911111111"
        patt = "^(\+7|8|7)?"            # удаляет первые цифры +7, 7, 8
        text = re.sub(patt, "", text)
        patt = "[^\d]?"                 # удаляет все объекты, за искл. цифр
        text = re.sub(patt, "", text)
        return text
    
    for person in data["persons"]:
        person["phone"] = clean_phonenumber(person["phone"])

    return data

@task(task_id="load_data_applications")
def load_data(data: dict) -> None:

    pg_hook = PostgresHook("postgreSQL_my1")
    conn = pg_hook.get_conn()
    conn.autocommit = True
    cursor = conn.cursor()

    for person in data["persons"]:

            columns = ','.join(tuple(person.keys()))

            request = " INSERT INTO request" + "(" + columns + ")" + \
                        " VALUES (" + "%s, "*(len(person)-1) + "%s)" + \
                        "ON CONFLICT DO NOTHING;"

            cursor.execute(request, tuple(person.values()))
        
    cursor.close()
    conn.close()

default_args = {
    'owner': 'Nikita Davydov',
    'start_date': days_ago(0),
    'depends_on_past': False, 
}

with DAG(
    'applications',
    default_args=default_args,
    schedule_interval=timedelta(seconds=10),
    catchup=False                   # нагнать текущую дату, начиная с даты старта
):
    
    t1 = extract_data()
    t2 = transform_data(t1)
    t3 = load_data(t2)

