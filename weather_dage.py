from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

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

