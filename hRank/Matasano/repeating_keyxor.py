'''
repeating key xor
given a text, encrypt it, under the key "ICE", using repeating-key XOR. In
repeating-key XOR, you'll sequentially apply each byte of the key; the first
byte of plaintext will be XOR'd against I, the next C, the next E, then I again
for the 4th byte, and so on.

'''
'''
single-byte xor
The hex encoded string has been XOR'd against a single character. Find the key,
decrypt the message. Devise some method for "scoring" a piece of English
plaintext. Character frequency is a good metric. Evaluate each output and choose
the one with the best score.

again stealing from https://en.wikipedia.org/wiki/XOR_cipher
'''
import binascii


def xor_strings(s, t):
    """xor two strings together"""
    if isinstance(s, str):
        # Text strings contain single characters
        return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))
    else:
        # Python 3 bytes objects contain integer values in the range 0-255
        return bytes([a ^ b for a, b in zip(s, t)])

xor_key = "ICE"

strinput = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

def repeating_xor(key, string):
    length = len(string)
    keyleng = len(key)
    concatkey = key*(length//keyleng) + key[:length%keyleng]
    out = xor_strings(string, concatkey)
    return binascii.hexlify(out.encode("utf8"))

print(repeating_xor(xor_key, strinput))
