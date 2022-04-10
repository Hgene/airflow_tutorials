### Python code 스케쥴 걸기

지난 [Airflow 설치하기](https://github.com/Hgene/airflow_tutorials/blob/master/install_airflow.md) 글에서 언급했듯이 Airflow의 기본적인 디렉토리 구조는 다음과 같다.  
<br/>    

> /airflow_workspace(관리폴더)  
&ensp;&ensp;&ensp;&ensp;- airflow  
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ㄴ dags(스케쥴 코드관리폴더)  
&ensp;&ensp;&ensp;&ensp;ㄴ airflow_env(가상환경 폴더)  
<br/>    

airflow_workspace를 기본 디렉토리로 봤을때 하위에 airflow 폴더가 있고 그 하위에 다시 dags 폴더가 존재하는데, 이 dags 폴더 내부에 스케쥴을 걸고 싶은 DAG파일들이 정리되어 있다.  

예를 들어 아래처럼 간단한 파이썬 함수를 스케쥴 걸고 싶다고 가정하자.


```python
def helloWorld():
    print('Hello World')
    return

```

이 함수를 스케쥴 걸기위해서는  
&ensp;&ensp;&ensp;&ensp;(1)DAG를 설정하고,  
&ensp;&ensp;&ensp;&ensp;(2)수행하고 싶은 task를 정의한 뒤에  
&ensp;&ensp;&ensp;&ensp;(3)실행 순서에 맞추어 Pipeline을 작성해주면 된다.  
스케쥴 걸고 싶은 시간은 크론탭의 시간정의방식과 동일하게 작성하면 되고, 아래의 예제는 매 15분(1시간단위)마다 helloWorld 함수를 실행하는 간단한 DAG작성 예제이다.  


```python
## hello_world_dag.py

from ast import operator
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def helloWorld():
    print('Hello World')
    return
    
#(1) DAG를 정의
with DAG(dag_id="hello_world_dag", 
        start_date=datetime(2021,1,1), 
        schedule_interval="15 * * * *", 
        catchup=False) as dag:
        
    #(2) task를 정의
    task1 = PythonOperator(
        task_id="hello_world", 
        python_callable=helloWorld
    )

#(3)실행순서에 맞추어 Pipeline 구성
task1

```
<br/>    

만약 2가지 task를 순차적으로 수행하고 싶다면 아래와 같이 코드를 수행해보자

```python
## hello_world_dag.py

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
    )
    
    task2 = PythonOperator(
        task_id="hello_world_v2", 
        python_callable=helloWorld_v2
    )

#(3)실행순서에 맞추어 Pipeline 구성
task1 >> task2

```
<br/>    

이제 이렇게 작성한 파일을 airflow_workspace/airflow/dags/ 에 위치시키고 터미널을 통해 scheduler를 실행시킨다면, interface에 해당 테스크가 정상적으로 수행되고 있는 화면을 확인할 수 있을 것이다.  

```bash
(airflow_env) $ airflow scheduler
```

