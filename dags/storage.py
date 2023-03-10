from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
import os

PASSWORD = os.environ["DB_USER_PASSWORD"]
HOME = os.environ["HOME"]
PATH_TO_SCRIPTS = os.path.join(os.path.join(HOME, "airflow"), "scripts")

default_args = {
        "owner": "Nikita Davydov",
        "start_date": days_ago(0),
        "depends_on_past": False
}

with DAG(
        "create_storage",
        default_args=default_args,
        schedule_interval="@once",
        catchup=False,
        template_searchpath=PATH_TO_SCRIPTS
        ):

    t1 = BashOperator(
            task_id="restart_postgreSQL",
            bash_command="restartpostgres.sh",
    )

    t2 = BashOperator(
            task_id="create_database",
            bash_command="createbase.sh",
    )
    
    t3 = BashOperator(
        task_id='create_user_table',
        bash_command="createtable.sh"
    )

    t1 >> t2 >> t3
