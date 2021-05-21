import base64
import binascii

def read_file():
  with open("b64encoded.txt","r") as f:
   return f.read()

encoded = read_file()
decoded = base64.b64decode(encoded)
print(binascii.hexlify(decoded))

