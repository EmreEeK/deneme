
import struct

from numpy import byte
import binascii
# Format: h is short in C type
# Format: l is long in C type
# Format 'hhl' stands for 'short short long'

# declaring an integer value
integer_val = 5
  
# converting int to bytes with length 
# of the array as 2 and byter order as big
bytes_val = integer_val.to_bytes(8, 'little')
print('1st loop')
for i in bytes_val:
    print(i)
a=struct.Struct('I')

bb=8
print('2nd loop')
for i in a.pack(bb):
    print(i)
binascii.hexlify(a.pack(bb))
print(a.pack(8))


print('3rd loop')
for i in b'\x01':
    print(i)
print(bytearray([8]))

def return_one_byte():
    return b'\x01'

print('4th loop')
for i in return_one_byte():
    print(i)
print(return_one_byte())