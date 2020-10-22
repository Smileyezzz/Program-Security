#!/usr/local/bin/python3
from pwn import *

r = remote("140.112.31.97", 30000)

def xor(a, b):
    return bytes([x^y for x, y in zip(a, b)])


def oracle(c):
    r.sendlineafter('cipher = ', c.hex())
    if b'YES' in r.recvline():
        return True
    else:
        return False

def checkpadding(string):
    for i in range(15, 0, -1):
        result = []
        for k in range(256):
            test_string = string[:i] + bytes([k]) + string[i+1:]
            if oracle(test_string):
                result.append(k)
        
        if len(result) == 1:
            print(f'The padding of the flag is {16-i}')
            break
        else:
            print(f'The padding of the flag is not {16-i}, so keep on ~')


cipher = bytes.fromhex(r.recvline().strip().partition(b' = ')[2].decode())
iv = cipher[:16]
cipher_zero = cipher[16:32]
pos_cipher = cipher[16:]
checkpadding(pos_cipher)

tmp_byte = bytes([cipher[22]^0x80]) + cipher[23:]
ans = b''
for j in range(21, 15, -1):
    for i in range(256):
        test_cipher = cipher[0:j] + bytes([cipher[j]^i^0x80]) + tmp_byte 
        if oracle(test_cipher):
            tmp_byte = bytes([cipher[j]^i]) + tmp_byte
            print(bytes([i]))
            ans = bytes([i]) + ans
            break


new_cipher = b'A'*16 + iv + cipher_zero
tmp_byte = cipher_zero
for j in range(31, 15, -1):
    for i in range(256):
        test_cipher = new_cipher[0:j] + bytes([new_cipher[j]^i^0x80]) + tmp_byte 
        if oracle(test_cipher):
            tmp_byte = bytes([new_cipher[j]^i]) + tmp_byte
            print(bytes([i]))
            ans = bytes([i]) + ans
            break
print(ans)
