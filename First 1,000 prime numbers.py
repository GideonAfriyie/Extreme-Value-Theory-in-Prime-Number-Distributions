@author: gideonafriyie
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []
num = 2
while len(primes) < 1000:
    if is_prime(num):
        primes.append(num)
    num += 1

import csv

with open('first_1000_primes.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Prime Number'])
    for p in primes:
        writer.writerow([p])

print("First 1,000 primes saved to 'first_1000_primes.csv'")
