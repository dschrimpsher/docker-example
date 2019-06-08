import requests
from time import sleep
import logging


def get(server, body):
    r = requests.get(server, verify=False)
    if r.status_code < 400:
        logging.info('Success %d' % r.status_code)
    else:
        logging.error('Error on Get %d' % r.status_code)


def run():
    logging.basicConfig(level=logging.DEBUG)
    body = dict(data="1234")
    while True:
        sleep(1)
        get('http://server:8000', body)


if __name__ == '__main__':
    run()
