#!/usr/bin/python3
'''
hex_to_base64.py

converts input hex to base64

operate on raw bytes

'''

#test = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

def hextob64(hexstring):
    from base64 import b64encode
    bytestring = bytes.fromhex(hexstring)
    pretty = b64encode(bytestring)
    print(str(pretty)[2:-1])
    return pretty


#print(hextob64(test))


'''
fixed XOR

a function takes two equal length buffers and produces their XOR combination

'''
def o(x):
    #from https://en.wikipedia.org/w/index.php?title=XOR_cipher
    if isinstance(x,str):
        return ord(x)
    else:
        return x

def fixedxor(buf1, buf2):
    from operator import xor
    pretty = b''
    bord1 = o(buf1)
    bord2 = o(buf2)
    for b1,b2 in zip(bord1,bord2):
        pretty += bytes([b1 ^ b2])
    return pretty


    buffer1 = bytes.fromhex(buf1)
    buffer2 = bytes.fromhex(buf2)
    bitstring1 = bin()
    bitstring2 = bin()
    for type(byte) in buffer1:

    pretty = xor(buffer1, buffer2)
    return pretty
