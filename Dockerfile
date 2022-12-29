FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN python -m pip install pyserial

CMD [ "python", "./transmitter.py" ]
