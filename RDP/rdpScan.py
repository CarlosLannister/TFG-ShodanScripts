from __future__ import with_statement
import time
import re,socket
import sys
import gevent
import os
from gevent import socket
from gevent.pool import Pool
from gevent import monkey


pool = Pool(1000)

def checkRdp(ip):
	bash = 'phantomjs url-to-image.js "http://127.0.0.1:8080/rdpdirect.html?gateway=127.0.0.1:8080&server=%s&width=800&height=600&color=16" %s.jpg 800 600' % (ip, ip) 
	os.system(bash)


f = open('rdp1-106.txt')
lines = f.readlines()

for line in lines:
	pool.apply_async(checkRdp(line.rstrip('\n').strip()),)

