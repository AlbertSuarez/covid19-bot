FROM python:3.7
ADD . /srv/covid19-bot
WORKDIR /srv/covid19-bot
RUN apt update
RUN apt install tor -y
COPY tor/torrc /etc/tor/torrc
RUN service tor restart
RUN pip install --upgrade pip
RUN pip3 install -r requirements.lock
CMD python3 -m src