## Airflow 설치하는 방법..!

![Airflow](https://airflow.apache.org/images/feature-image.png)


### Airflow란..!
Airbnb에서 제작한 workflow management tool로 특정 작업을 주기적으로 자동으로 수행하고, 모니터링이 필요할 때 사용하는 툴이다. 복잡한 Pipeline을 가진 테스크가 조금만 많아져도 crontab으로 관리하기가 힘든데, 그 부분을 쉽게 해결해줄 수 있는 관리 엔진이다.  

<br/>  


### Airflow는..
* 사용성이 용이하고
* 오픈소스이며
* Python기반이라 관리면에서도 용이하며, 복잡한 workflow의 수행이 가능하면서도 유연성까지 갖추고 있다.
* 마지막으로 시각적인 interface 환경까지 갖추고 있어,

많은 기업들이 사내 테스크들의 Schedule/Monitoring에 많이 사용중인 것으로 알고 있다.  
<br/>  


### Airflow 설치방법  

지금부터는 Airflow를 설치하고, 간단한 파일을 스케쥴 걸어보는 작업까지 진행해보려고 한다.  
아래의 코드예제는 Medium의 INSAID의 ["Setting up Apache-Airflow in MacOS"](https://insaid.medium.com/setting-up-apache-airflow-in-macos-2b5e86eeaf1) 글을 인용하였음을 미리 밝힌다.
위 링크에서 보면 훨씬 더 자세한 설명이 있으니, 꼭 한번 보는 것을 추천한다..!  

설치순서는 다음과 같다.  
1. pip3를 활용한 airflow 설치
2. 가상환경 디렉토리에 airflow용 폴더("가상환경 디렉토리"/airflow/dags) 생성
3. airflow용 db 초기화
4. airflow.cfg 파일내 디렉토리 수정
5. db 유저생성
6. webserver / schedule 실행으로 interface 환경 실행하기

<br/>    

기초적인 파일구성은 아래와 같다.  
/airflow_workspace(관리폴더)  
&ensp;&ensp;&ensp;&ensp;- /airflow  
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ㄴ /dags(스케쥴 코드관리폴더)  
&ensp;&ensp;&ensp;&ensp;ㄴ /airflow_env(가상환경 폴더)  


1. 먼저 가상환경을 활성화한 상태에서 airflow를 포함하여 필요한 패키지를 설치한다.
```bash
$ source "가상환경 디렉토리"/bin/activate
$ pip3 install apache-airflow[gcp,sentry,statsd]
$ pip3 install pyspark
$ pip3 install sklearn
```


