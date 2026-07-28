
import random
import cirq
import secrets
from math import gcd

#prime checker 
def is_prime(n):
    if n <2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num_bits = 8

#random number generator functions
def make_classical_bit(num_bits):
    return random.getrandbits(num_bits)
def make_qrng_bit(num_bits):
    pass
#qrng

def make_csprng_bit(num_bits):
    return secrets.randbits(num_bits)

def make_trng_bit(num_bits):
    #get from random.org
    pass

#rng_choice = 
def generate_prime(rng_choice):   #(rng choice):
    pass

#Convert to integer

#generate prime:
def generate_prime(rng_choice):
    while True:
        if rng_choice == 'PRNG':
            candidate = make_classical_bit(num_bits)
        elif rng_choice == 'CSPRNG':
            candidate = make_csprng_bit(num_bits)
        elif rng_choice == 'TRNG':
            candidate = make_trng_bit(num_bits)
        elif rng_choice == 'QRNG': 
            candidate = make_qrng_bit(num_bits)

        candidate |= 1
        if is_prime(candidate):
            return candidate

# RSA Key Generation

my_choice = input("Choose a random number generator (PRNG, CSPRNG, TRNG, QRNG): ")
p = generate_prime(my_choice)
q = generate_prime(my_choice)
while p == q:
    q = generate_prime(my_choice)

n = p * q
phi = (p - 1) * (q - 1)
e = 65537 
if gcd(e, phi) != 1:
    e = 3
d = pow(e, -1, phi)






  