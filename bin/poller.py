#!/usr/bin/python
import requests
import onzo_insert, mysql_onzo
from datetime import datetime
import json,sys,os
from time import sleep

wgtn = [-41.300598, 174.780381]
dist = [100]

params = wgtn + dist

print(params)
url = "https://app.onzo.co.nz/nearby/%s/%s/%s"
url = url % tuple(params)

status = 0
while (status != 200):
  r = requests.get(url)
  status = r.status_code
  if status != 200:
     sleep(5)

datadir = os.path.dirname(sys.argv[0])
ofile = os.path.join(datadir,'..','data','onzo_%s.json' % datetime.now().strftime('%Y%m%d_%H%M%S'))

with open(ofile,'w') as f:
    f.write(r.content)

# Attempting MySQL insert
onzo_insert.onzo_insert(ofile)
conn = mysql_onzo.onzo_connect()
curs = conn.cursor()
ins = r"""
INSERT INTO onzo.bikes_suburbs 
SELECT bl.*, sh.areaunit_id, sh.areaunit_name, sm.suburb 
from bike_locations bl 
LEFT JOIN area_unit_shapes sh 
ON ST_CONTAINS(sh.shape, bl.position) LEFT JOIN submap sm 
ON sm.areaunit = sh.areaunit_name where bl.datetime > (select max(datetime) from onzo.bikes_suburbs);
"""
curs.execute(ins)
conn.commit()
curs.close()
conn.close()
