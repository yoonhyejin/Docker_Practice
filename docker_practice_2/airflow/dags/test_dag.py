import time
import requests
from datetime import datetime

from airflow import models
from airflow.operators.python_operator import PythonOperator
from pendulum import timezone

def insert_data(url, text):
    datas = { 'text' : text }
    requests.post(url=url, json=datas)

with models.DAG(
    dag_id="test_dag",
    tags=[],
    description="Dag for HTTP request",
    schedule_interval="@once",
    default_args={
        "owner": "dini",
        "depends_on_past": False,
        "start_date": datetime(2021, 8, 25, tzinfo=timezone("Asia/Seoul")),
        "retries": 0,
    },
    catchup=False,
) as dag:

    _ = PythonOperator(
        task_id="t1",
        python_callable=insert_data,
        op_kwargs={
            'url' : 'http://app:5000/insert',
            'text': 'first data using airflow'
            }
    )
