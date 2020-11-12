from pwn import *
from Crypto.Util.number import *

#p = remote('140.112.31.97', 30001)
p = remote('localhost', 8787)

p.recvuntil("n = ")
n = int(p.recvline().strip())
p.recvuntil("c = ")
c = int(p.recvline().strip())

e = 65537

lower_b = 0
upper_b = n

chaox_r = (-n) % 3

mod_c = (pow(3, e, n)*c)%n

while(1):
    p.sendline(str(mod_c))
    p.recvuntil("m % 3 = ")
    r = int(p.recvline().strip())
    if(r == 0):
        upper_b = (upper_b + 2*lower_b) // 3 
        print(f'the upper bound is {upper_b}')
    elif(r == chaox_r):
        tmp_upper_b = upper_b
        upper_b = (2*upper_b + lower_b) // 3 
        lower_b = (tmp_upper_b + 2*lower_b) // 3 + 1
        print(f'the upper bound is {upper_b}')
        print(f'the lower bound is {lower_b}')
    else:
        lower_b = (2*upper_b + lower_b ) // 3 + 1
        print(f'the lower bound is {lower_b}')

    mod_c = (pow(3, e, n)*mod_c)%n

    if(upper_b == lower_b):
        break



print(f'========FINAL========')
print(f'the guess plain is {upper_b}')
guess_plain = upper_b

for i in range(-128, 128):
    guess_c = pow(guess_plain+i, e, n)
    if(c == guess_c):
        print(long_to_bytes(guess_plain+i))
        break

