# Tested on Python 3.12.3, but should in theory work on any Python 3. I think.
# If it throws an error on a normal run, fall back to Python 3.12.3.
import zlib

def mix_xor(b):
  for i in range(len(b)):
    b[i] ^= 0b10100101

def mix_add(b):
  for i in range(len(b)):
    b[i] = (b[i] - 0b11001100) & 0xff

def mix_sub(b):
  for i in range(len(b)):
    b[i] = (b[i] + 0b00110011) & 0xff

def mix_ror(b):
  for i in range(len(b)):
    b[i] = ((b[i] << 1) | (b[i] >> 7)) & 0xff

def mix_rol(b):
  for i in range(len(b)):
    b[i] = ((b[i] >> 1) | (b[i] << 7)) & 0xff

#Old function
#def transform_0(b):
  #mix_xor(b) or mix_add(b) or mix_add(b) or mix_sub(b) or mix_ror(b)

#New function
def transform_0(b):
  mix_xor(b)
  mix_add(b)
  mix_sub(b)
  mix_sub(b)
  mix_ror(b)

#Old function
#def transform_1(b):
  #mix_add(b) or mix_ror(b) or mix_ror(b) or mix_ror(b) or mix_xor(b)

#New function
def transform_1(b):
  mix_add(b)
  mix_ror(b)
  mix_ror(b)
  mix_ror(b)
  mix_xor(b)

#Old function
#def transform_2(b):
  #mix_sub(b) or mix_xor(b) or mix_sub(b) or mix_xor(b) or mix_sub(b)

#New function
def transform_2(b):
  mix_xor(b)
  mix_sub(b)
  mix_xor(b)
  mix_sub(b)
  mix_xor(b)

#Old function
#def transform_3(b):
  #mix_rol(b) or mix_add(b) or mix_rol(b) or mix_rol(b) or mix_xor(b)

#New function
def transform_3(b):
  mix_rol(b)
  mix_xor(b)
  mix_xor(b)
  mix_add(b)
  mix_xor(b)

#Old function
#def transform_4(b):
  #mix_add(b) or mix_add(b) or mix_add(b) or mix_xor(b) or mix_sub(b)

#New function
def transform_4(b):
  mix_add(b)
  mix_xor(b)
  mix_sub(b)
  mix_sub(b)
  mix_sub(b)

def main():

  b = bytearray(b'K\xe4\xf9\xb1Nhn\x82\xbd\xa4\x88\x99\xa4n\xb1\xa8d\xe7D\xc7\xe4\xebd\xf9BD\x8e')

  transform_4(b)
  transform_3(b)
  transform_2(b)
  transform_1(b)
  transform_0(b)

  print(b)

  if b == bytearray(b'K\xe4\xf9\xb1Nhn\x82\xbd\xa4\x88\x99\xa4n\xb1\xa8d\xe7D\xc7\xe4\xebd\xf9BD\x8e'):
    print("Correct flag!")
  else:
    print("Wrong flag!")

if __name__ == "__main__":
  main()