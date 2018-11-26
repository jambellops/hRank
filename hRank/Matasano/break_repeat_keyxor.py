'''
break_repeat_keyxor.py

There's a file here. It's been base64'd after being encrypted with repeating-key XOR.

Decrypt it.

Here's how:


1. Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.

2. Write a function to compute the edit distance/Hamming distance between two
strings. The Hamming distance is just the number of differing bits. The distance
between:
this is a test
and
wokka wokka!!!
is 37. Make sure your code agrees before you proceed.

3. For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second
KEYSIZE worth of bytes, and find the edit distance between them. Normalize this
result by dividing by KEYSIZE.

4. The KEYSIZE with the smallest normalized edit distance is probably the key.
You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4
KEYSIZE blocks instead of 2 and average the distances.

5. Now that you probably know the KEYSIZE: break the ciphertext into blocks of
KEYSIZE length.

6. Now transpose the blocks: make a block that is the first byte of every block,
and a block that is the second byte of every block, and so on.

7. Solve each block as if it was single-character XOR. You already have code to
do this.

8. For each block, the single-byte XOR key that produces the best looking
histogram is the repeating-key XOR key byte for that block. Put them together
and you have the key.

This code is going to turn out to be surprisingly useful later on. Breaking
repeating-key XOR ("Vigenere") statistically is obviously an academic exercise,
a "Crypto 101" thing. But more people "know how" to break it than can actually
break it, and a similar technique breaks something much more important.

No, that's not a mistake.
We get more tech support questions for this challenge than any of the other
ones. We promise, there aren't any blatant errors in this text. In particular:
the "wokka wokka!!!" edit distance really is 37.
'''
import base64
import collections

KEYSIZE = range(2,41)
mult = 1
normaldistances = collections.OrderedDict()

def xorbytestring(inp1, inp2):
    byt_in1 = [byte for byte in bytes(inp1, 'utf8')]
    byt_in2 = [byte for byte in bytes(inp2, 'utf8')]
    return bytes([b1 ^ b2 for b1, b2 in zip(byt_in1,byt_in2)])

def fixedxor(buf1, buf2):
    buffer1 = bytes.fromhex(buf1)
    buffer2 = bytes.fromhex(buf2)
    return xorbytestring(buffer1, buffer2)

with open('6.txt') as input_file:
    ciphertext = base64.b64decode(input_file.read())

def editbitdistance(string1,string2):
    distance = 0
    if isinstance(string1,str):
        if isinstance(string2, str):
            bytes_str1 = [byte for byte in bytes(string1, 'utf8')]
            bytes_str2 = [byte for byte in bytes(string2, 'utf8')]
            xor_bytes = [b1 ^ b2 for b1, b2 in zip(bytes_str1, bytes_str2)]
    else:
        xor_bytes = [b1 ^ b2 for b1, b2 in zip(string1, string2)]
    for byte in xor_bytes:
        distance += sum([1 for bit in bin(byte) if bit == '1'])
    return distance

#print(editbitdistance('this is a test', 'wokka wokka!!!'))
def normalizedbitdist(keysize, ciphertext,mult):
    return editbitdistance(ciphertext[:keysize*mult], ciphertext[keysize*mult:2*keysize*mult])//(keysize*mult)

for n in KEYSIZE:
    normaldistances[n] = normalizedbitdist(n, ciphertext, mult)

minimum_val = 255
found_key = 0
for key in normaldistances:
    if normaldistances.get(key) < minimum_val:
        minimum_val = normaldistances.get(key)
        found_key = key

print(found_key)
