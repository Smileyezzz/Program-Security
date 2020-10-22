#!/usr/bin/env python3
from functools import reduce

class LFSR:
    def __init__(self, init, feedback):
        self.state = init
        self.feedback = feedback
    def getbit(self):
        nextbit = reduce(lambda x, y: x ^ y, [i & j for i, j in zip(self.state, self.feedback)])
        self.state = self.state[1:] + [nextbit]
        return nextbit

class MYLFSR:
    def __init__(self, inits):
        inits = [[int(i) for i in f"{init:016b}"] for init in inits]
        self.l1 = LFSR(inits[0], [int(i) for i in f'{39989:016b}'])  # 39989 => \x9c\x35 == \x9c5
        self.l2 = LFSR(inits[1], [int(i) for i in f'{40111:016b}'])  # 40111 => \x9c\xaf
        self.l3 = LFSR(inits[2], [int(i) for i in f'{52453:016b}'])  # 52453 => \xcc\xe5
    def getbit(self):
        x1 = self.l1.getbit()
        x2 = self.l2.getbit()
        x3 = self.l3.getbit()
        return (x1 & x2) ^ ((not x1) & x3)
    def getbyte(self):
        b = 0
        for i in range(8):
            b = (b << 1) + self.getbit()
        return bytes([b])

def guess(mask):
    result = 0
    pre_count = 0
    for k in range(65536):      # \xff\xff is 65535
        count = 0
        test_lfsr = LFSR([int(x) for x in f'{k:016b}'], \
                        [int(y) for y in f'{mask:016b}'])
        for i in range(100):    # the len of the output
            test_bit = test_lfsr.getbit()
            count += (test_bit == output[i])
        if count > pre_count:
            pre_count = count
            result = k
            print(f'the probability of {k} is {count/100}')
    return result

def search(a,b):
    for k in range(65536):
        flag = True
        count = 0
        test_lfsr = MYLFSR([k, a, b])
        for i in range(100):
            test_bit = test_lfsr.getbit()
            if(test_bit != output[i]):
                flag = False
                break
        if flag:
            print(f'x1 is {k}')
            r1 = k.to_bytes(2, 'big')
            r2 = a.to_bytes(2, 'big')
            r3 = b.to_bytes(2, 'big')
            print(f'the flag is {r1 + r2 + r3}')
        


output = [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1]
x2 = guess(40111)
b2 = x2.to_bytes(2, 'big')
print(f'x2 might be {b2}')
x3 = guess(52453)
b3 = x3.to_bytes(2, 'big')
print(f'x3 might be {b3}')
search(x2, x3)
