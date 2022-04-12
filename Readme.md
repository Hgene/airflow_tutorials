## Airflow 경험해보기..!

<p align="center">
  <img src="https://airflow.apache.org/images/feature-image.png" width="80%" height="80%" />
</p>

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

Ariflow를 설치하는 방법은 따로 정리해놓은 [Airflow 설치하기](https://github.com/Hgene/airflow_tutorials/blob/master/install_airflow.md) 글을 참고해보자..!
<br/>  
<br/>  

### Airflow로 스케쥴 걸어보기..!

첫번째로는 간단한 Python 코드를 Airflow를 통해 스케쥴 걸어보는 작업을 진행해볼까 한다..!  
차차 시리즈로 만들어볼 생각인데, 천천히 하나씩 해보시길!!ㅎ

* [[1] Airflow로 Python code 스케쥴 걸기](https://github.com/Hgene/airflow_tutorials/blob/master/rec1_scheduling.md)
* [[2] Operator 구성하기(pythonOperator/bashOperator)](https://github.com/Hgene/airflow_tutorials/blob/master/rec2_operator.md)
* [3] 책에서 해보고 싶은 내용 참고해서 추가해보기




