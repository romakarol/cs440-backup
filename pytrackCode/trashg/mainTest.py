import machine
import math
import network
import os
import time
import utime
import gc
from machine import RTC
from machine import SD
from L76GNSS import L76GNSS
from pytrack import Pytrack
from network import Sigfox
import struct
import socket
import ubinascii
from machine import Timer
import pycom

gc.enable()

py = Pytrack()
l76 = L76GNSS(py, timeout=30)

# sd = SD()
# os.mount(sd, '/sd')
# f = open('/sd/gps-record.txt', 'w')

coord = l76.coordinates()
print(coord)

print("Configuring sigfox message.\n")
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
# make the socket blocking
s.setblocking(True)
# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)
#msg =  bytearray([l76.coordinates()])

#16/12/18
#lat, lon = coord
#print(lat, lon)
#print(type(lat))
#print(type(lon))
#latS=(str(lat)).replace(".","")
#print(latS)


#lat=53.37401
#long=-6.602458
#st = list(msg) -s.send(st[0])
#print(st[0])

message=""
lat="53.37401"
latF=float(lat)
latF=latF*100000.0
lati=int(latF)

for i in range(4): #values 0-3
   b= lati % 256
   #print(b)
   lati=lati>>8 #lati=lati/256
   #print(lati)
   c=chr(b)
   #print(c)
   #print(ord(c))
   message+=c

print("Sending message")
print(str(lat)+str(lon))
#s.send(b''+str(lat)+','+str(lon)) ## Send last known coordinates
s.send(int(latS))
#s.send(int(lat))

#s.send(msg)
print("sent.\n")
