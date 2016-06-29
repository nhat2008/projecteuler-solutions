# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def get_biggest_prime(n):
    x = 3
    while n % 2 == 0 and n != 2:
        n = n / 2
    while x < n ** 0.5:
        if n % x == 0:
            n = n / x
        x = x + 2
    return n

print get_biggest_prime(600851475143)