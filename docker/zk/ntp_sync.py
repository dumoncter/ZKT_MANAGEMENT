# -*- coding: utf-8 -*-
import os
import sys
from datetime import datetime

CWD = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)
from zk import ZK


def ntp_async(ip):
    conn = None
    zk = ZK(ip, port=4370, timeout=1)
    try:
        conn = zk.connect()
        print(f'Synchronization is successful {ip}')
        conn.set_time(datetime.now())
    except Exception as e:
        print(datetime.now().strftime("%m/%d/%Y %H:%M:%S"), ip, "\nError : {}".format(e))
    finally:
        if conn:
            conn.disconnect()
