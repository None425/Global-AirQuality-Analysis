# 세계 대기질 관측 데이터을 활용한 분석
분석 기간 2025-12-17 ~ 2025-12-20 

## 프로젝트 개요
글로벌 대기질 데이터를 활용해 
대기질(AQI)와 상관간계가 높은 초미세먼지(PM2.5)의 시간대별 수치와 국가별 비교

## 활용 데이터 
1. 세계 나라별 대기질 관측 데이터 - https://www.kaggle.com/datasets/smeet888/global-air-quality-data15-days-hourly-50-cities/data
- 주요 변수: PM2.5, PM10, NO2, AQI, 온도, 습도, 풍속
2. 외교부 국가 표준 코드 데이터 - https://www.data.go.kr/data/15091117/fileData.do
- 국가코드와 국가명(한글) 매핑을 하기위한 데이터

## 분석 과정
1. 데이터 구조 및 품질 확인
- 결측치 및 이상값 확인
- 분석 대상 기간 검증

2. 데이터 전처리
- 시간 정보 처리
- 국가 코드 문자열 정규화
- 국가명 표준화

3. 분석 내용
- AQI와 대기오염 물질 간 상관관계 분석
- 출·퇴근 시간대(07-09시,18-20시) PM2.5 변화 분석
- 국가별 평균 PM2.5 비교

## 분석 결과 및 한계
### 분석 결과
-AQI는 PM2.5와 가장 높은 상관관계를 보였다.
-출·퇴근 시간대에서 PM2.5가 다소 높은 구간이 관찰되었으나,  
다른 시간대와 비교했을 때 그 차이는 크지 않았다.(다른 다양한 배출원과 기상의 영향 변수가 존재)
-국가별 평균 PM2.5는 기존 국제기구 보고서와는 다른 결과가 나타났다.
### 분석의 한계
- 분석 기간이 제한적이라 절대적인 국가 순위가 아닌 기간내의 상대적 경향으로 해석해야된다.


## 활용 기술
- Python : 데이터 분석 및 전처리
- pandas,numpy : 데이터 처리
- SQL : Python 환경에서 데이터 구조 및 품질 확인
- Matplotlib : 데이터 시각화
- Jupyter Notebook

## 실행 방법
1. 라이브러리 설치
```bash
pip install -r requirements.txt
```
* Windows 환경에서 pip 오류가 발생할 경우, 아래 명령어 실행 후 다시 실행
```bash
python -m pip install --upgrade pip
```
2. SQLite 데이터베이스 생성
```bash
python src/create_db.py
```
3. 분석 실행

AirqualityAnalysis.ipynb 파일을 Jupyter Notebook에서 실행

