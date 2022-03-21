FROM python:3.10-slim
# RUN adduser -D -g '' fielddata-user
RUN useradd -ms /bin/bash fielddata-user
RUN apt-get update && \
    apt-get -y install gcc
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
USER fielddata-user
WORKDIR /home/fielddata-user
