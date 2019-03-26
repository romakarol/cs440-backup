from network import Sigfox
import socket
import ubinascii

print("SiPy test program.\n")
​
# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# make the socket blocking
s.setblocking(True)

# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

# send some bytes
msg="ABCD"
print("Sending message")
print(msg)
s.send(msg)
print("sent.\n")
