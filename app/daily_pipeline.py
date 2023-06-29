from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'your_name',
    'start_date': datetime(2023, 6, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def task1_function():
    print('task one is done')
    pass

def task2_function():
    print('task two is done')
    pass

dag = DAG('daily_pipeline', default_args=default_args, schedule_interval=timedelta(days=1))

task1 = PythonOperator(
    task_id='task1',
    python_callable=task1_function,
    dag=dag
)




