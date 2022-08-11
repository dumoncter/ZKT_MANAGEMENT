from zk import ntp_sync, restart_zkt
import asyncio
import time


if __name__ == "__main__":
    with open("zk/all_ip", "r") as file:
        contents = file.readlines()
        for i in range(len(contents)):
            value = str(contents[i]).strip().split()
            asyncio.run(ntp_sync.ntp_async(*value))
            time.sleep(2)
            asyncio.run(restart_zkt.restart_device(*value))
            time.sleep(2)
