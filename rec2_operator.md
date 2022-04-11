## Airflow Operator 실행해보기..!  

혹시 Airflow를 설치하는 방법을 모른다면, [Airflow 설치하기](https://github.com/Hgene/airflow_tutorials/blob/master/install_airflow.md) 와 
[Airflow에 Python 스케쥴 거는 법](https://github.com/Hgene/airflow_tutorials/blob/master/rec1_.md) 글을 보고 오길 권장한다.  
<br/>    


이번시간에는 Operator를 구성하는 요소를 살펴보고, Python에 이어 bashOperator를 수행하는 방법을 공유할까 한다. 
대부분의 상황에서 python과 bash만 수행할 수 있어도 해결되기 때문에, 이 두가지 Operator는 필수적으로 알고 있어야한다.    
<br/>    


먼저 첫번째는 bash명령어를 테스크로 만들어보자..!  아래는 현재날짜를 추출하는 아주 간단한 bash명령어이다. 
```bash
$ date
```

위의 bash 명령어를 DAG객체로 변환하는 것은 아래와 같이 수행하면 된다. 

```python
## hello_world_dag_bash.py

from ast import operator
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

    
#(1) DAG를 정의
with DAG(dag_id="print_date", #Airflow에서 보이는 DAG(테스크) 이름
        start_date=datetime(2021,1,1), 
        schedule_interval="16 * * * *", #crontab 문법에 맞추어 작성, 매시간 16분에 실행
        catchup=False) as dag:
        
    #(2) task를 정의
    task1 = BashOperator(
        task_id="hello_world", 
        bash_command='date'
    )

#(3)실행순서에 맞추어 Pipeline 구성
task1

```
<br/>   

> 혹시 크론탭 시간설정에 익숙하지 않다면 [crontab guru](https://crontab.guru/) 사이트를 통해 쉽게 확인 가능하니, 참고하면 좋다!  
파라미터로 `@hourly` 와 같이 간단하게 주기배치를 설정할 수도 있지만, 결국 나중에 작업이 많아지게 되면 크론탭의 시간설정방식을 사용하게 되기에, 미리 익숙해지는 것도 나쁘지 않은 거 같다ㅎㅎ
<br/>   


이제 이렇게 작성한 파일을 airflow_workspace/airflow/dags/ 에 위치시키고 터미널을 통해 scheduler를 실행시킨다면, interface에 해당 테스크가 정상적으로 수행되고 있는 화면을 확인할 수 있을 것이다.  

```bash
(airflow_env) $ airflow scheduler
(airflow_env) $ airflow webserver
```
<br/>    
<br/>    


이렇게 bashOperator를 사용해야하는 이유는 가끔은 서로다른 가상환경의 파이썬 구동을 필요로 할 때도 있기 때문이다.  
앞서 나온 bash 예제에 더하여, 1부터 10까지 더하고, 해당값을 return 하는 함수가 있다고 가정하자  

```python
## src/exam_py/add_to_ten.py

def add_int(x_int):
    return sum([x for x in range(int(x_int)+1)])

if __name__=='__main__':
    print(add_int(10))
```

<br/>    

```python
from ast import operator
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


#(1) DAG를 정의
with DAG(dag_id="hello_world_dag_bash", #Airflow에서 보이는 DAG(테스크) 이름
        start_date=datetime(2021,1,1), 
        schedule_interval="16 * * * *", #crontab 문법에 맞추어 작성, 매시간 16분에 실행
        catchup=False) as dag:
        
    #(2) task를 정의
    task1 = BashOperator(
        task_id="hello_world", 
        bash_command='date'
    )
    
    task2 = BashOperator(
        task_id="add_ten_py", 
        bash_command='~/airflow_workspace/airflow_env/bin/python  ~/airflow_workspace/airflow/dags/src/exam_py/add_to_ten.py'
        #bash_command= '파이썬가상환경_디렉토리  실행할.py위치 '
    )

#(3)실행순서에 맞추어 Pipeline 구성
task1 >> task2

```
<br/>    

위의 스케쥴 DAG의 구조는 터미널에서도 쉽게 확인이 가능하다.
```bash
(airflow_env) $ airflow tasks list hello_world_dag_bash --tree

>> OUTPUT은 아래와 같다.
<Task(BashOperator): hello_world>
    <Task(BashOperator): add_ten_py>
```
<br/>    

이렇게 생성된 DAG는 아래와 같이 정상적으로 `Airflow schedule` 에 올라가고,   
로그(log) output값에도 1부터 10까지의 합인 `55` 가 정상적으로 실행되었음을 확인할 수 있다.  
<br/>    

<img width="1680" alt="hello_world_dag_bash" src="https://user-images.githubusercontent.com/47958965/162745350-9d4413aa-8494-436d-a686-f7dfe49c3da3.png" >
<br/>    

<img width="1680" alt="hello_world_dag_bash_log" src="https://user-images.githubusercontent.com/47958965/162745954-b4ff2ac2-5b38-4389-9c8e-a02303fe5e90.png">





