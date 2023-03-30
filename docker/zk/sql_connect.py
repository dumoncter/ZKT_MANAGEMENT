import json
import pyodbc
import collections
from datetime import datetime
from sys import platform

driver = 'DRIVER={ODBC Driver 17 for SQL Server}'
if platform == "linux" or platform == "linux2":
    driver = 'DRIVER={ODBC Driver 17 for SQL Server}'
elif platform == "win32":
    driver = 'DRIVER={SQL Server}'

server = 'SERVER=192.168.201.40'
port = 'PORT=1433'
db = 'DATABASE=zkt'
user = 'UID=sa'
pw = 'PWD=QApassw3'
conn_str = ';'.join([driver, server, port, db, user, pw])

conn = pyodbc.connect(conn_str)
conn.timeout = 60
cursor = conn.cursor()
cursor.execute('SELECT * FROM "dbo"."EXP_Machines"')
rows = cursor.fetchall()
objects_list = []


def sql_export():
    try:
        for row in rows:
            d = collections.OrderedDict()
            d["Name"] = row[0]
            d["IpAddress"] = row[2]
            objects_list.append(d)
        j = json.dumps(objects_list, indent=4)
        with open("zkt_ip.json", "w") as f:
            f.write(j)
    except pyodbc.Error as err:
        print(datetime.now().strftime("%m/%d/%Y %H:%M:%S"), 'Error', err)
    finally:
        f.close()
        cursor.close()
        conn.close()