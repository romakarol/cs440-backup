import struct
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
print("Configuring sigfox message.\n")
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
s.setblocking(True)
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

message=""
lat="53.37401"
latF=float(lat)
latF=latF*100000.0
lati=int(latF)
for i in range(4): #values 0-3
   b= lati % 256
   lati=lati>>8 #lati=lati/256
   c=chr(b)
   message+=c

print(message)
#s.send(message)

#above python code on node
#below implement in php on server

for i in range(4):
     (ord(message[i]))
     (hex(ord(message[i])))
     print((hex(ord(message[i]))))

     #flip back on php send#php vers of ord?

     #0x5173

#php python
value=0
for i in range(4):
    #inverted, low order bits first
    value+=ord(message[i])<<8*i #rotate bits back into right place
    fvalue=(float(value))
    fvalue=fvalue/100000.0

#print(fvalue)
#s.send(message)
