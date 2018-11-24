import MySQLdb

def onzo_connect():
    conn = MySQLdb.connect(host= "localhost",
                  user="mj2_squ",
                  passwd="NEikJemEalmOmD1",
                  db="onzo")
    return conn

def onzo_cursor():
    c = onzo_connect()
    return c.cursor()
