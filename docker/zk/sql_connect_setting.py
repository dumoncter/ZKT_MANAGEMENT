import pyodbc

driver = 'DRIVER={SQL Server}' # ODBC Driver 17 for SQL Server - Ubuntu # SQL Server - Windows
server = 'SERVER=192.168.....'
port = 'PORT=1433'
db = 'DATABASE=zkt'
user = 'UID=USER DB'
pw = 'PWD=PASSWORD USER DB'
conn_str = ';'.join([driver, server, port, db, user, pw])

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Сhecking the server DB version
# cursor.execute("SELECT @@version;")
# row = cursor.fetchone()
# while row:
#     print(row[0])
#     row = cursor.fetchone()


conn = pyodbc.connect(conn_str)
conn.timeout = 60
cursor = conn.cursor()
cursor.execute('SELECT * FROM "dbo"."EXP_Machines"')
rows = cursor.fetchall()
objects_list = []
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