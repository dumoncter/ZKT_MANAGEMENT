import sys
import os
from datetime import datetime

CWD = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)

from zk import ZK, reboot_web

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
        reboot_web.selenium_open(ip)
        restart_web += 1
    except Exception as e:
        print(datetime.now().strftime("%m/%d/%Y %H:%M:%S"), ip, "\nError : {}".format(e))
        ip_error.append(name+ip)
        # if 'timed out' in connect:
        #     ip_error.append({'ip_adress': ip, 'error_log': e})


# print(restart_device("192.168.202.111"))
