FROM python:3.6.12-slim-buster
USER root

RUN rm /etc/apt/sources.list && \
    echo "deb https://mirrors.cloud.tencent.com/debian buster main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb https://mirrors.cloud.tencent.com/debian buster-updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb-src https://mirrors.cloud.tencent.com/debian buster main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb-src https://mirrors.cloud.tencent.com/debian buster-updates main contrib non-free" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y gcc libssl-dev default-libmysqlclient-dev

COPY ./ /app/
WORKDIR /app/

RUN pip install -r requirements.txt -i http://mirrors.tencent.com/pypi/simple/ --trusted-host mirrors.tencent.com

CMD ["bash", "/app/start_web.sh"]

