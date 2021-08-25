FROM python:3.8

# image의 메타데이터를 설정한다.
LABEL email="myemail@gmail.com"
LABEL name="me"

# local . -> container /app 복사
COPY . /app 

# We copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt /app/requirements.txt

# ENV FLASK_APP=./src/app.py

# working directory 설정
WORKDIR /app

# requirements.txt 파일에서 flask 끌어와서 pip 설치
RUN pip install -r requirements.txt 

# RUN flask db upgrade && flask db migrate

# 절대경로, 상대경로 둘다 가능 (WORKDIR 고려)
CMD [ "python", "/app/src/app.py" ] 
# CMD ["python", "-m", "flask", "run"]