import sys
import math
import csv
import logging
import numpy as np

log = logging.getLogger(__name__)
UPTO = 100
primes = list()
factors = np.empty((0,0), dtype=int)


def factorize(n, primes_discovered) -> np.array:
    factorization = np.zeros((1, len(primes_discovered)), dtype=int)
    unfactored_quotient = n
    prime_set = set(primes_discovered)
    for i, prime in enumerate(primes_discovered):
        # Disregard possibilities that do not actually divide n
        if unfactored_quotient % prime != 0:
            continue

        # Divider is a prime factor if it is an exponential root of n
        power = 1
        while unfactored_quotient % prime ** (power + 1) == 0:
            log.debug(unfactored_quotient, prime, power)
            power += 1
        # Store the power that divides the unfactored quotient
        factorization[0,i] = power

        # Updated the unfactored quotient for later primes
        unfactored_quotient /= int(prime ** power)

    return factorization

def prime(n) -> bool:
    # Assume primality
    determined = True
    for i, j in enumerate(range(1, int(math.floor(math.sqrt(n))))):
        possible_dividor = j + 1
        # Disregard possibilities that do not actually divide n
        if n % possible_dividor != 0:
            continue
        determined = False
    return determined


# Test cases
# print(factorize(4, [2,3]))
# print(factorize(5, [2,3]))
# print(factorize(6, [2,3,5]))
# print(factorize(7, [2,3,5]))
# print(factorize(8, [2,3,5,7]))

# sys.exit(0)

for number in range(2, UPTO):
    log.debug("Primes: {}".format(primes))
    log.debug("Factors: {}".format(factors))
    log.debug("\nNumber: {}".format(number))

    is_prime = False
    factorization = factorize(number, primes)
    if (factorization == 0).all():
        is_prime = prime(number)

    # Composites just add their factorization to the array of factors
    if len(primes) > 1 and not is_prime:
        factors = np.append(factors, factorization, axis=0)
        continue

    # Add prime to primes set
    primes.append(number)

    # Add zeros array to factors
    new_column = np.zeros((factors.shape[0], 1), dtype=int)
    factors = np.append(factors, new_column, axis=1)

    # Add one to the factorization to honor its primality
    factorization = np.append(factorization, np.ones((1,1), dtype=int), axis=1)

    # Append the prime's factorization to the factors table
    factors = np.append(factors, factorization, axis=0)

with open('computed-data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(primes)
    writer.writerows(factors)
