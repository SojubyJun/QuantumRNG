import cirq
import random
import secrets
from math import gcd

#prime checker (miller-rabin?)

num_bits = 4
#random number generator functions
def make_classical_bit(num_bits):
    return random.getrandbits(num_bits)
def make_qrng_bit(num_bits):
    pass
#qrng

def make_csprng_bit(num_bits):
    return secrets.randbits(num_bits)

def generate_prime(rng_choice):   #(rng choice):
    pass

#Convert to integer
  