from zk import restart_zkt, ntp_sync, telegram_bot, sql_connect
import time
import json
from datetime import datetime

count_ip = 0


def main():
    try:
        with open("zkt_ip.json", 'r', encoding='utf-8') as json_file:
            global count_ip
            contents = json.load(json_file)
            count_ip += len(contents)
            for i in range(len(contents)):
                ip_device = contents[i]['IpAddress']
                name_device = contents[i]['Name'] + ' = '
                ntp_sync.ntp_async(ip_device)
                time.sleep(2)
                restart_zkt.restart_device(ip_device, name_device)
                time.sleep(2)
    except Exception as e:
        print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), "\nError : {}".format(e))


def send_telegram():
    try:
        if len(restart_zkt.ip_error) >= 1:
            new_line = '\n'
            without_error = count_ip - len(restart_zkt.ip_error)
            telegram_bot.send_msg(f'''
❌ {len(restart_zkt.ip_error)} из {without_error} ZKT имеют ошибки
🔥 {restart_zkt.restart_web} перезапущенно через WEB
{new_line.join(list(map(str, restart_zkt.ip_error)))}
                                ''')
        else:
            telegram_bot.send_msg(f'✅ {count_ip} ZKT прошла синхронизацию')
    except Exception as e:
        print('Telegram:', datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), "\nError : {}".format(e))


if __name__ == "__main__":
    sql_connect.sql_export()
    main()
    send_telegram()
