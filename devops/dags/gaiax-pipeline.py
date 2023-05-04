from datetime import timedelta
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
import logging

def extract():
    logging.info("extract process")


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 6,
    'retry_delay': timedelta(minutes=30),
}

dag = DAG('gaiax',
    default_args=default_args,
    description='gaiax pipeline',
    start_date=datetime(2023, 5, 3),
    tags=['gaiax'],
    schedule_interval="0 1 * * *") # Intervalo de ejecución)


extract_os_task = PythonOperator(task_id="extract_os", python_callable=extract, dag=dag)

extract_os_task
#process_task >> backup_task
