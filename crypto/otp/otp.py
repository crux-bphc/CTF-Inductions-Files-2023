import random
from Crypto.Util.number import getPrime as gP


seed = random.randint(2,2**16)
mod = gP(16)
class LCG:
    def __init__(self, seed, m):
        self.m = m
        self.a = random.randint(2,self.m)
        self.b = random.randint(2,self.a)
        self.seed = seed

    def next(self):
        seed = (self.a*self.seed + self.b) % self.m
        self.seed = seed
        return seed

lcg = LCG(seed, mod)

def byte_xor(b1, b2):
    return bytes([_a ^ _b for _a, _b in zip(b1, b2)])

enc = b''
with open('flag.png', "rb") as flag:
    i = 0
    while(True):
        byte = flag.read(2)
        rand_num = lcg.next()
        rand = rand_num.to_bytes(2, 'big')
        enc += byte_xor(byte, rand)
        if len(byte) < 2:
            break

with open("enc", "wb") as enc_flag:
    enc_flag.write(enc)

print('m =', lcg.m)
