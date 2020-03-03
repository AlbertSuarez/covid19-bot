FROM python:3.7
ADD . /srv/covid19-bot
WORKDIR /srv/covid19-bot
RUN pip3 install -r requirements.lock
CMD python3 -m src