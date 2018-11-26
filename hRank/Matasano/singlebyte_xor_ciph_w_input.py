'''
single-byte xor
The hex encoded string has been XOR'd against a single character. Find the key,
decrypt the message. Devise some method for "scoring" a piece of English
plaintext. Character frequency is a good metric. Evaluate each output and choose
the one with the best score.

again stealing from https://en.wikipedia.org/wiki/XOR_cipher
'''
import fileinput

def xor_strings(s, t):
    """xor two strings together"""
    if isinstance(s, str):
        # Text strings contain single characters
        return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))
    else:
        # Python 3 bytes objects contain integer values in the range 0-255
        return bytes([a ^ b for a, b in zip(s, t)])

with open('hxstring.txt', mode='r', newline='\n') as f:
    lines = f.readlines()


def lineread(line):
    resultlist = []
    bytestring = bytes.fromhex(line)
    for byte in bytestring:
        resultlist.append(byte)
    return resultlist

keyset = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
          'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
          'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
          'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4',
          '5', '6', '7', '8', '9', '0', '!', '@', '$', '%', '^', '&', '*', '(',
          ')', '-', '_', '[', ']', '{', '}', ':', ';', '.', ',', '>', '<', '?',
          '~', '`', '|']

aresetsbetter = {'`', 't', '[', 'g', 'z', 'U', 'o', 'a', ',', 'N', '^', '0', '(',
            'T', ')', 'r', '9', 'Q', '|', '7', 'i', 'h', ']', 'B', '>', '&', 'p',
            'l', 'P', '%', 'x', 'F', 'k', 'K', 'V', 'W', '1', '!', 'J', 'X', 'S',
            'q', 'C', ';', '<', '?', '3', '4', 'L', 'b', 'O', '$', 'E', '}', 'f',
            '@', 'c', 'e', 'Y', '*', 'd', 'v', 'I', 'M', 'j', ':', 'u', 'A', 'm',
            'G', '.', '~', 'y', 'Z', 'R', '8', '2', '-', 'w', '6', 's', '5', 'D',
            'n', '{', '_', 'H'}

def findsinglexor(input,fit,excluded):
    top_score = 0
    top_result = ''
    top_key = ''
    bytelist = lineread(input)
    bytelen = len(bytelist)
    for c in keyset:
        attempt = ''
        for byte in bytelist:
            attempt += xor_strings(chr(byte), c)
        score = 0
        for a in attempt:
            if a in fit:
                score += 1
            elif a in excluded:
                score -= 4
        if score > top_score:
            top_score = score
            top_result = attempt
            top_key = c
    #print(top_score, top_result)
    return (top_score, top_result, top_key, input)

top_Outscore = 0
top_Outresult = ''
top_Outkey = ''
found_input = ''
for line in lines:
    line = line[:-1]
    score,result,key,lineinput = findsinglexor(line)
    if score > top_Outscore:
        top_Outscore = score
        top_Outkey = key
        top_Outresult = result
        found_input = lineinput
print(top_Outscore, top_Outkey, top_Outresult, found_input)


'''\x1b 7 7 3 1 6 ? x \x15 \x1b \x7f + x 4 1 3 = x 9 x ( 7 - 6 < x 7 > x : 9 ; 7 6'''
