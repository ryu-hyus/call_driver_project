# call_driver_project
# 대리운전 모바일 주문을 위한 애플리케이션

python version 3.8.2

사용을 위해서 가상환경 설정 및 requirements.txt에 기재된 라이브러리를 설치해주세요.
 - 가상환경을 만들 디렉토리로 이동
 - python -m venv venv  ## 가상환경 생성
 - venv\Scripts\activate ## 가상환경 실행
 - cd call_driver_project
 - pip install -r requirements.txt ## 라이브러리 설치

-------------------------------------------------------------------
시스템 사용 전 체크사항
- Price Table 업데이트
- Operationday 업로드

-------------------------------------------------------------------

Price Table(요금표) DB업뎃 방법
- calldriverapp/uploads 디렉토리에 fare_table.csv 파일 수정
- 터미널에 python manage.py shell 입력
- exec(open("./calldriverapp/makepricetable.py").read()) 명령어 입력

장고 Admin을 이용한 Price Table(요금표) DB업뎃 방법
- host/admin 접속 및 superuser 로그인
- pricefile에 add
- fare_table.csv 업로드 및 save

