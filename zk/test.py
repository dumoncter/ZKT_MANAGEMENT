from zk import ZK
from datetime import datetime
import time

conn = None
# create ZK instance
zk = ZK('192.168.203.124', port=4370, timeout=5, password=0, force_udp=True, ommit_ping=False)
try:
    # connect to device
    conn = zk.connect()
    # disable device, this method ensures no activity on the device while the process is run
    conn.disable_device()
    time.sleep(1)
    conn.set_time(datetime.now())
    print ("Current Time            : %s" % conn.get_time())
    # users = conn.get_users()
    # for user in users:
    #     privilege = 'User'
    #     if user.privilege == const.USER_ADMIN:
    #         privilege = 'Admin'
    #     print ('+ UID #{}'.format(user.uid))
    #     print ('  Name       : {}'.format(user.name))
    #     print ('  Privilege  : {}'.format(privilege))
    #     print ('  Password   : {}'.format(user.password))
    #     print ('  Group ID   : {}'.format(user.group_id))
    #     print ('  User  ID   : {}'.format(user.user_id))


except Exception as e:
    print("Process terminate : {}".format(e))