'''program to convert hex string to base64'''

from __future__ import print_function
import binascii
h = input("Enter hex string")
hex = h.decode("hex")
base64 = binascii.b2a_base64(hex)
print(base64)

