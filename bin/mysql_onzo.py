import MySQLdb,os

hdir = "/home/mj2_squ/proj/onzo/onzo-wgtn/bin"

with open(os.path.join(hdir,'../etc/mysql.sec'),'r') as f:
    pw = f.read()

pw = pw.strip()

def onzo_connect():
    conn = MySQLdb.connect(host= "localhost",
                  user="mj2_squ",
                  passwd=pw,
                  db="onzo")
    return conn

def onzo_cursor():
    c = onzo_connect()
    return c.cursor()
