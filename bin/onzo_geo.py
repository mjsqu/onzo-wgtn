#!/usr/bin/python
import matplotlib.path as mpp
import numpy as np
import json
import sys

with open('../data/ref/Wellington_AU_Shapes.json','r') as f:
  wgtn_au = json.load(f)

geo = u'\ufeffWKT'
name = u'AU2015_V1_00_NAME'

import re
polyrx = r'\(\(([0-9,\-. ]*)\)\)'

def bike_suburb(pt1):
    for sub in wgtn_au:
        poly = sub[geo]
        n = sub[name]
        rxm = re.findall(polyrx,poly)
        # Splits the multipolygon into polygons
        # Then the points are extracted (comma delimited)
        # long/lat are delimited by space
        # ((long lat, long2 lat2, long3 lat3))
        mp_fmt = [[z2.split(' ') for z2 in z1]for z1 in [x 
                 for x in [match.split(',') for match in rxm] # x is now a list of found polygons
                 ]]
        for polygon in mp_fmt:
            path = mpp.Path(polygon)
            if path.contains_point(pt1):
                return n
