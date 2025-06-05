from math import gcd
from sympy import isprime

def wheel_sieve(k, max_prime):
    c_values = [c for c in range(1, k) if gcd(c, k) == 1]
    primes = []
    t = 0
    while True:
        for c in c_values:
            p = k * t + c
            if p > max_prime:
                return primes
            if isprime(p):
                primes.append(p)
        t += 1
