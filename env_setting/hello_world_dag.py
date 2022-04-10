from ast import operator
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def helloWorld():
    print('Hello World')
    return 0
    
def helloWorld_v2():
    print('Hello World V2')
    return 1
    
    
#(1) DAG를 정의
with DAG(dag_id="hello_world_dag", 
        start_date=datetime(2021,1,1), 
        schedule_interval="15 * * * *", 
        catchup=False) as dag:
        
    #(2) task를 정의
    task1 = PythonOperator(
        task_id="hello_world", 
        python_callable=helloWorld
        
    task2 = PythonOperator(
        task_id="hello_world_v2", 
        python_callable=helloWorld_v2
    )

#(3)실행순서에 맞추어 Pipeline 구성
task1 >> task2
        
        
