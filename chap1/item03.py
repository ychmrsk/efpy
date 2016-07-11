#! /usr/bin/env python
# -*- coding:utf-8 -*-

# bytes, str, unicode
# bytes: raw 8bit-value (binary)
# str  : unicode character

# unicode => binary : utf-8 encode
# binary  => unicode:       decode

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # instance of str

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # instance of bytes

# !!! using binary mode to open file objects
# # error 
# with open('random.bin', 'w') as f:
#     f.write(os.urandom(10))
#  
# >>> TypeError: must be str, not bytes
#  
# # ok
# with open('random.bin', 'wb') as f:
#     f.write(os.urandom(10))
