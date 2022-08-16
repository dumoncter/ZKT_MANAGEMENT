import sys
import os
from datetime import datetime

CWD = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)

from zk import ZK


async def restart_device(ip):
    zk = ZK(ip, port=4370, timeout=10)
    try:
        conn = zk.connect()
        print(f'Reboot: {ip}')
        conn.restart()
    except Exception as e:
        print(datetime.now(), ip, "\nError : {}".format(e))

