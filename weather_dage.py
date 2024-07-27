from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from extract import extract_paris_weather,extract_new_york_weather,extract_tokyo_weather
from transform import transform
from load import load

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}
dag = DAG(
    'weather_dag',
    default_args=default_args,
    description='A simple ETL DAG to retrieve weather data',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
)

# define tasks
extract_paris_weather=PythonOperator(
     task_id='extract_paris',
     python_callable=extract_paris_weather,
     dag=dag,
)
extract_new_york_weather=PythonOperator(
    task_id='extract_new_york',
    python_callable=extract_new_york_weather,
    dag=dag,
)
extract_tokyo_weather=PythonOperator(
    task_id='extract_tokyo_weather',
    python_callable=extract_tokyo_weather,
    dag=dag
)
transform=PythonOperator(
    task_id="transform",
    python_callable=transform,
    dag=dag
)
load=PythonOperator(
    task_id="load",
    python_callable=load
    dag=dag
)
# set the dependencies
[extract_paris_weather,extract_new_york_weather,extract_tokyo_weather] >> transform >> load

