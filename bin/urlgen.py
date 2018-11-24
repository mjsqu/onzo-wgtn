#!/usr/bin/python
import requests
from datetime import datetime
import json,sys,os
from time import sleep

wgtn = [-41.300598, 174.780381]
zoom = [11]

params = wgtn + zoom

print(params)
url = "https://36wish.github.io/onzomap/#%s/%s/%s"
url = url % tuple(params)

print(url)
