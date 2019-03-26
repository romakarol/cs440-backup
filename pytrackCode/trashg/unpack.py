import struct
import binascii
from struct import *

#74657374
#lat="fd7e55425647d3c0"
lat="53.37401"
lng="-6.602458"

message=struct.pack('f',float(lat)) + struct.pack('f',float(lng))
print(struct.unpack('f',message))

print("full message:")
message=struct.pack('f',float(lat)) + struct.pack('f',float(lng))
print(message)
print("latitude packed:")
print(struct.pack('f',float(lat)))
print("latitude unpacked")
print(struct.unpack('f',lat))
print(message)
print("long packed:")
print(struct.pack('f',float(lng)))
print("long unpacked")
print(struct.unpack('f',lng))
