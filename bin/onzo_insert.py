import MySQLdb,os,json
from datetime import datetime as dt

def onzo_insert(datafile):
    conn = MySQLdb.connect(host= "localhost",
                  user="mj2_squ",
                  passwd="NEikJemEalmOmD1",
                  db="onzo")
    x = conn.cursor()

    x.execute("select column_name from information_schema.columns where table_name = 'raw' and table_schema = 'onzo'")

    tablecols = [row[0] for row in x.fetchall()]

    inshead = "INSERT INTO raw (" + ','.join(tablecols) + ") VALUES (" + ','.join(["%s" for str in range(23)]) + ")"

    file,ext = os.path.splitext(datafile)
    if ext == '.json':
        with open(os.path.join('../data',datafile),'r') as f:
            datetime = dt.strptime(file[-15:],"%Y%m%d_%H%M%S")
            obj = json.load(f)
            onzodata = obj['data']
            valueslist = [datetime]
            for onz in onzodata:
                for c in tablecols[1:]:
                    valueslist.append(onz[c])
                x.execute(inshead,tuple(valueslist))
                conn.commit()
                valueslist=[valueslist[0]]
    else:
        print(datafile+" not a json")

    conn.close()

def onzo_direct_insert(obj,datetime):
    conn = MySQLdb.connect(host= "localhost",
                  user="mj2_squ",
                  passwd="NEikJemEalmOmD1",
                  db="onzo")
    x = conn.cursor()

    x.execute("select column_name from information_schema.columns where table_name = 'raw' and table_schema = 'onzo'")

    tablecols = [row[0] for row in x.fetchall()]

    tablecols = onzo_raw_col_list()
    onzodata = obj['data']
    valueslist = [datetime]
    for onz in onzodata:
        for c in tablecols[1:]:
            valueslist.append(onz[c])
            x.execute(inshead,tuple(valueslist))
            conn.commit()
            valueslist=[valueslist[0]]
    conn.close()
