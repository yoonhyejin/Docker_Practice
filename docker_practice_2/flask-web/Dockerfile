FROM ubuntu:20.04

# image의 metadata를 설정한다.
LABEL email="dini@socar.kr"
LABEL name="dini"

# python 설치한다.
RUN apt-get update -y && \
    apt-get install -y python3.8 python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

# working directory 설정
WORKDIR /app

# requirements.txt 파일에서 flask 끌어와서 pip 설치
RUN pip install -r requirements.txt

COPY . /app

# 실행할 컨테이너를 configure한다(?)
# ENTRYPOINT [ "python3" ]

CMD [ "python3" , "app.py"]
# CMD ["python3", "-m", "flask", "run"]