from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from samples.sample_extractor_py import task_one, task_two

default_args = {
    'owner': 'admin',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


dag = DAG(
    dag_id='sample_extractor_dag_v1',
    default_args=default_args,
    description='This is first simple extractor dag',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily'
)

first_task = PythonOperator(
    task_id='first_task',
    python_callable=task_one,
    dag=dag,
)


second_task = PythonOperator(
    task_id='second_task',
    python_callable=task_two,
    dag=dag,
)

first_task >> second_task
