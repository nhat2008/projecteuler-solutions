# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

import math


def get_prime(n):
    x = 3
    while n % 2 == 0 and n != 2:
        n /= 2
    while x < n and n / x > 0:
        while n % x == 0 and n != x:
            n /= x
        x += 2
    return n


def run():
    result = set()
    i = 3
    while len(result) < 10001:
        result.add(get_prime(i))
        i += 2
    ans = max(result)
    return ans


print run()