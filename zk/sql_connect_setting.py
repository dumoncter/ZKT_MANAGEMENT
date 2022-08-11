import pyodbc

driver = 'DRIVER={SQL Server}'
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


print("Database Table Data Info: ")
cursor.execute('SELECT ReaderIpAddress FROM "dbo"."EXP_Machines"')
f = open('all_ip', 'w')
datas = cursor.fetchall()
for data in datas:
    f.write(str(*data) +'\n')
    print(*data)

f.close()
cursor.close()
conn.close()