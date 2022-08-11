import sys
import os

CWD = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)

from zk import ZK


async def restart_device(ip):
    zk = ZK(ip, port=4370)
    try:
        conn = zk.connect()
        print(f'Перезагрузка устройства: {ip}')
        conn.restart()
    except Exception as e:
        print("Process terminate : {}".format(e))
    finally:
        if conn:
            conn.disconnect()

