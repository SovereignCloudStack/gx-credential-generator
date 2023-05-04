from datetime import timedelta
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import logging

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 6,
    'retry_delay': timedelta(minutes=30),
}

gaiaxdag = DAG('gaiax',
               default_args=default_args,
               description='gaiax pipeline',
               start_date=datetime(2023, 5, 3),
               tags=['gaiax'],
               schedule_interval="0 1 * * *")  # Intervalo de ejecución)


def start():
    logging.info("Starting gaiax pipeline")


started_task = PythonOperator(task_id="started_task", python_callable=start, dag=gaiaxdag)


def generator():
    logging.info("Self description generator")


generator_task = PythonOperator(task_id="generator_task", python_callable=generator, dag=gaiaxdag)


def validation():
    logging.info("Validation task")


validation_task = PythonOperator(task_id="validation_task", python_callable=validation, dag=gaiaxdag)


def sign():
    logging.info("Sign task")


sign_task = PythonOperator(task_id="sign_task", python_callable=sign, dag=gaiaxdag)


def compliance():
    logging.info("Compliance task")


compliance_task = PythonOperator(task_id="compliance_task", python_callable=compliance, dag=gaiaxdag)

## TODO
# generator_task = BashOperator(
#     task_id='generator_task',
#     bash_command='python  /opt/airflow/dags/tasks/gx-sd-generator.py --gaia-x  --file=results/osdescriptor --os-cloud=gx-h61.1',
#     dag=gaiaxdag)

started_task >> generator_task >> validation_task >> sign_task >> compliance_task
