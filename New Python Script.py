
import random
import requests
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
    qubits = [cirq.LineQubit(i) for i in range(num_bits)]
    circuit = cirq.Circuit()
    circuit.append(cirq.H.on_each(*qubits))
    circuit.append(cirq.measure(*qubits, key='result'))
    simulator = cirq.Simulator()
    result = simulator.run(circuit)
    measured_bits = result.measurements['result'][0]
    random_number = int("".join(str(bit) for bit in measured_bits[::-1]), 2)  # little endian
    return random_number
#qrng

def make_csprng_bit(num_bits):
    return secrets.randbits(num_bits)

def make_trng_bit(num_bits):
    """TRNG: Fetches true physical entropy/randomness from Random.org."""
    # Calculate max possible value for given bit size (e.g., 8 bits -> 0 to 255)
    max_val = (1 << num_bits) - 1

    url = f"https://www.random.org/integers/?num=1&min=0&max={max_val}&col=1&base=10&format=plain&rnd=new"

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return int(response.text.strip())
    except Exception as e:
        print(f"TRNG network fetch failed ({e}), using fallback.")
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

my_choice = (input("Choose a random number generator (PRNG, CSPRNG, TRNG, QRNG): ").strip().upper())
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

#print results
print("\n=== RSA KEYS GENERATED ===")
print(f"Prime p: {p}")
print(f"Prime q: {q}")
print(f"Public Key  (n, e): ({n}, {e})")
print(f"Private Key (n, d): ({n}, {d})")





  