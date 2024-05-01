FROM python:3.9
ENV TZ=Asia/Seoul
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV userid ''
ENV passwd ''
ENV dbname ''
ENV dbhost ''

ENTRYPOINT ["python", "main.py"]