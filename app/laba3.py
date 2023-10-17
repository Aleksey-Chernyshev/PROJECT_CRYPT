import os
import random

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def generate(t):
    q = random.randint(t+1, 1000000)
    r = random.randint(t+1, 1000000)
    while gcd(q, r) != 1:
        q = random.randint(t+1, 1000000)
        r = random.randint(t+1, 1000000)
    return q, r

def extendedEuclidean(a, b, x, y):
    if a == 0:
        x = 0
        y = 1
        return b
    x1, y1 = 0, 0
    gcd = extendedEuclidean(b % a, a, x1, y1)
    x = y1 - (b // a) * x1
    y = x1
    return gcd

def multiplicativeInverse(a, m):
    def extendedEuclidean(a, b):
        if b == 0:
            return a, 1, 0
        else:
            gcd, x, y = extendedEuclidean(b, a % b)
            return gcd, y, x - (a // b) * y

    gcd, x, y = extendedEuclidean(a, m)
    if gcd != 1:
        print("The multiplicative inverse does not exist.")
        return -1
    inverse = (x % m + m) % m
    return inverse

def bin2dec(s):
    n = 1
    out = 0
    for i in s[::-1]:
        if i == '1': out += n
        n <<=1
    return out

def Crypted(q,r,w, message):
    C =[]
    binar = []
    B =[]
    for i in range(len(w)):
        B.append((w[i] * r) % q)

    for c in message:
        binary = ''.join(format(ord(x), '08b') for x in c)
        binar.append(binary)
        sum = 0
        for i in range(len(binary)):
            if binary[i] == '1':
                sum += B[i]
        C.append(sum)
    return C

def Decrypted(C, inverse, q, w):
    C_hatch = []
    for i in range(len(C)):
        multi = (C[i] * inverse) % q
        C_hatch.append(multi)
    decBin =[]
    for i in range(len(C_hatch)):
        diff = C_hatch[i]
        binaryCode = ["0","0","0","0","0","0","0","0"]
        for j in range(len(w)-1, -1, -1):
            if diff >= w[j] and diff != 0:
                binaryCode[j] = '1'
                diff = diff - w[j]
        binaryCode1 = ''.join([str(e) for e in binaryCode])
        result =bin2dec(binaryCode1)
        character = chr(result)
        decBin.append(character)
    return decBin
 

w = [2, 7, 11, 21, 42, 89, 180, 354]
t = 0
for i in range(len(w)):
    t += w[i]
q, r = generate(t)
#print(q, " ", r)
message = os.getenv("key")
C = Crypted(q,r,w,message)
print("Crypted: ", C)
inverse = multiplicativeInverse(r,q)
#print(inverse)
decBin = Decrypted(C, inverse, q, w)
print("Decrypted: ", ''.join([str(e) for e in decBin]))
