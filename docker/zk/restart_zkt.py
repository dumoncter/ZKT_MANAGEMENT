from datetime import datetime
from .reboot_web import selenium_open
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from .base import ZK

ip_error = []
restart_web = 0


def restart_device(ip, name):
    global ip_error
    zk = ZK(ip, port=4370, timeout=10)
    try:
        conn = zk.connect()
        print(f'Reboot: {ip}')
        conn.restart()
    except Exception:
        reboot_page(ip, name)


def reboot_page(ip, name):
    global restart_web
    try:
        selenium_open(ip)
        restart_web += 1
    except Exception as e:
        print(datetime.now().strftime("%m/%d/%Y %H:%M:%S"), ip, "\nError : {}".format(e))
        ip_error.append(name+ip)
        # if 'timed out' in connect:
        #     ip_error.append({'ip_adress': ip, 'error_log': e})


# print(restart_device("192.168.202.111"))
