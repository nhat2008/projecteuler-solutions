# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

import math


def get_prime_v2(n):
    a = 5
    if n < 4:
        return n
    while n % 2 == 0 and n != 2:
        n /= 2
    if n < 9:
        return n
    while n % 3 == 0 and n != 3:
        n /= 3

    while a <= math.floor(math.sqrt(n)):
        while n % a == 0 and n != a:
            n /= a
        a = a + 2
    return n


def run():
    result = set()
    result.add(2)
    i = 3
    while True:
        p = get_prime_v2(i)
        if p > 2000000:
            break
        result.add(p)
        i += 2
    numbers = list(result)

    result = reduce(lambda x, y: x + y, numbers)
    return result


print run()

