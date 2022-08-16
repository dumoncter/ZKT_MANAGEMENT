from zk import restart_zkt, ntp_sync, telegram_bot
import asyncio
import time
from datetime import datetime

count_ip = 0


def main():
    try:
        with open("zk/all_ip.txt", "r") as file:
            global count_ip
            contents = file.readlines()
            count_ip += len(contents)
            for i in range(len(contents)):
                value = str(contents[i]).strip().split()
                asyncio.run(ntp_sync.ntp_async(*value))
                time.sleep(2)
                asyncio.run(restart_zkt.restart_device(*value))
                time.sleep(2)
    except Exception as e:
        print(datetime.now(), "\nError : {}".format(e))


def send_telegram():
    try:
        if len(ntp_sync.ip_error) >= 1:
            new_line = '\n'
            without_error = count_ip - len(ntp_sync.ip_error)
            telegram_bot.send_msg(f'❗ Синхронизация выполнена {without_error} устройств. ❗\n'
                                  f'❌ Всего: {len(ntp_sync.ip_error)} устройств с ошибками ❌\n'
                                  f'{new_line.join(map(str, ntp_sync.ip_error))}'
                                  f'{ntp_sync.ip_error()}'
                                  )
        else:
            telegram_bot.send_msg(f'✅ Синхронизация {count_ip} устройств выполнена без ошибок ✅')
    except Exception as e:
        print('Telegram:', datetime.now(), "\nError : {}".format(e))


if __name__ == "__main__":
    main()
    send_telegram()
