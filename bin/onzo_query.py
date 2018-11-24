#!/usr/bin/python
import onzo_geo, json, sys
with open(sys.argv[1],'r') as f:
  bikes = json.load(f) 
  bikes = bikes['data']

pt1 = [(b['longitude'],b['latitude']) for b in bikes]

print([(p[1],p[0],onzo_geo.bike_suburb(p)) for p in pt1])
