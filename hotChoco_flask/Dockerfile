FROM python:3.12-slim

WORKDIR /app

# requirements.txt는 상위 디렉토리에 있으므로 별도 복사
COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Flask 소스 복사
COPY hotChoco_flask/src /app

ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask", "run"]
