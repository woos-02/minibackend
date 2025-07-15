# FROM python:3.10.12

# ENV PYTHONUNBUFFERED 1

# RUN apt-get -y update
# RUN apt-get -y install vim

# RUN mkdir /app
# WORKDIR /app

# # requirements.txt 복사 및 pip 설치
# COPY requirements.txt /app/
# RUN pip install --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt

# # gunicorn 설치 확인
# RUN which gunicorn && ls -l $(which gunicorn)
# # 전체 프로젝트 복사
# COPY . /app/
# COPY .env /app/
# COPY .env .

FROM python:3.10.12
ENV PYTHONUNBUFFERED=1

# 시스템 의존성 설치 (vim은 예시입니다)
RUN apt-get update \
 && apt-get install -y --no-install-recommends vim \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 1) requirements만 복사 → 의존성 설치
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# 2) 나머지 소스코드 복사
COPY . .

# (선택) ENTRYPOINT/CMD 설정
CMD ["gunicorn", "modelproject.wsgi:application", "--bind", "0.0.0.0:8000"]
