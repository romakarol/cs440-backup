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
import struct

gc.enable()
py = Pytrack()
l76 = L76GNSS(py, timeout=30)
print("Configuring sigfox message.\n")
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
s.setblocking(True)
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

lat="53.37401"
#latF=float(lat)

lng="-6.602458"
#lngF=float(lng)

print(str(lat), ":", str(lng))
s.send(struct.pack('f',float(lat)) + struct.pack('f',float(lng)))
